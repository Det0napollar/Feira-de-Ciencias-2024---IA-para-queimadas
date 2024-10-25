# Função para normalizar valores entre 0 e 1
def normalizar(valor, min_val, max_val):
    return (valor - min_val) / (max_val - min_val)

# Função para ajustar pesos dinamicamente
def ajustar_pesos(temperatura, estacao):
    # Ponderação padrão
    peso_vegetacao = 0.3
    peso_temperatura = 0.3
    peso_umidade = 0.2
    peso_vento = 0.2

    # Ajuste de pesos para estações secas
    if estacao in ["verao", "outono"] and temperatura > 35:
        peso_temperatura += 0.1
        peso_umidade -= 0.1

    return peso_vegetacao, peso_temperatura, peso_umidade, peso_vento

# Função para prever queimada com base em várias variáveis
def prever_queimada(indice_vegetacao, temperatura, umidade, vento, estacao="verao"):
    # Normalizar os valores
    indice_vegetacao_normalizado = normalizar(indice_vegetacao, 0, 1)
    temperatura_normalizada = normalizar(temperatura, 20, 50)
    umidade_normalizada = normalizar(umidade, 10, 100)
    vento_normalizado = normalizar(vento, 0, 100)

    # Ajustar pesos dinamicamente
    peso_vegetacao, peso_temperatura, peso_umidade, peso_vento = ajustar_pesos(temperatura, estacao)

    # Calculando pontuação de risco
    risco_queimada = (
        peso_vegetacao * (1 - indice_vegetacao_normalizado) +
        peso_temperatura * temperatura_normalizada +
        peso_umidade * (1 - umidade_normalizada) +
        peso_vento * vento_normalizado
    )

    # Definir threshold para queimada
    if risco_queimada > 0.6:
        return 1  # Queimada detectada
    else:
        return 0  # Sem queimada

# Função para avaliar o modelo e registrar métricas detalhadas
def avaliar_modelo(dados):
    verdadeiro_positivo = 0
    falso_positivo = 0
    verdadeiro_negativo = 0
    falso_negativo = 0

    for amostra in dados:
        indice_vegetacao, temperatura, umidade, vento, estacao, queimada_real = amostra
        previsao = prever_queimada(indice_vegetacao, temperatura, umidade, vento, estacao)

        # Contabilizar métricas
        if previsao == 1 and queimada_real == 1:
            verdadeiro_positivo += 1
        elif previsao == 1 and queimada_real == 0:
            falso_positivo += 1
        elif previsao == 0 and queimada_real == 0:
            verdadeiro_negativo += 1
        elif previsao == 0 and queimada_real == 1:
            falso_negativo += 1

    # Calcular precisão, revocação e F1-score
    acuracia = (verdadeiro_positivo + verdadeiro_negativo) / len(dados)
    precisao = verdadeiro_positivo / (verdadeiro_positivo + falso_positivo) if (verdadeiro_positivo + falso_positivo) > 0 else 0
    revocacao = verdadeiro_positivo / (verdadeiro_positivo + falso_negativo) if (verdadeiro_positivo + falso_negativo) > 0 else 0
    f1_score = 2 * (precisao * revocacao) / (precisao + revocacao) if (precisao + revocacao) > 0 else 0

    # Exibir resultados detalhados
    print(f"Acurácia do modelo: {acuracia * 100:.2f}%")
    print(f"Precisão: {precisao:.2f}")
    print(f"Revocação: {revocacao:.2f}")
    print(f"F1-Score: {f1_score:.2f}")
    print("\nDetalhes:")
    print(f"Verdadeiros Positivos: {verdadeiro_positivo}")
    print(f"Falsos Positivos: {falso_positivo}")
    print(f"Verdadeiros Negativos: {verdadeiro_negativo}")
    print(f"Falsos Negativos: {falso_negativo}")

# Dados de exemplo com a nova estrutura (inclui vento e estação do ano)
dados_treinamento = [
    (0.6, 30, 70, 15, "inverno", 0),  # Sem queimada
    (0.2, 45, 20, 30, "verao", 1),  # Queimada
    (0.7, 25, 85, 10, "primavera", 0),  # Sem queimada
    (0.3, 40, 25, 50, "outono", 1),  # Queimada
    (0.8, 20, 90, 5, "inverno", 0),  # Sem queimada
    (0.9, 35, 75, 20, "primavera", 0),  # Sem queimada
    (0.1, 50, 10, 60, "verao", 1),  # Queimada
    (0.4, 32, 50, 25, "outono", 0),  # Sem queimada
    (0.2, 42, 30, 40, "verao", 1),  # Queimada
    (0.5, 28, 65, 15, "primavera", 0)   # Sem queimada
]

# Avaliar o modelo
avaliar_modelo(dados_treinamento)

# Testar o modelo com novos dados
novos_dados = [
    (0.3, 38, 40, 25, "verao"),  # Esperado: Queimada
    (0.7, 25, 80, 10, "inverno"),  # Esperado: Sem queimada
    (0.4, 44, 15, 45, "verao")   # Esperado: Queimada
]

print("\nPrevisões para novos dados:")
for novo_dado in novos_dados:
    indice_vegetacao, temperatura, umidade, vento, estacao = novo_dado
    previsao = prever_queimada(indice_vegetacao, temperatura, umidade, vento, estacao)
    resultado = "Queimada" if previsao == 1 else "Sem queimada"
    print(f"Índice de Vegetação: {indice_vegetacao}, Temperatura: {temperatura}, Umidade: {umidade}, Vento: {vento}, Estação: {estacao} -> {resultado}")
