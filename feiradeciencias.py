
# Função para normalizar valores entre 0 e 1
def normalizar(valor, min_val, max_val):
    return (valor - min_val) / (max_val - min_val)

# Função para classificar queimada com base em regras simples
def prever_queimada(indice_vegetacao, temperatura, umidade):
    # Normalizar os valores (ajustar a escala)
    indice_vegetacao_normalizado = normalizar(indice_vegetacao, 0, 1)  # Considerando que o índice vai de 0 a 1
    temperatura_normalizada = normalizar(temperatura, 20, 50)  # Temperatura em graus Celsius
    umidade_normalizada = normalizar(umidade, 10, 100)  # Umidade relativa do ar

    # Definindo pesos (importância de cada variável)
    peso_vegetacao = 0.4
    peso_temperatura = 0.4
    peso_umidade = 0.2

    # Calculando uma pontuação de risco de queimada
    # Quanto menor o índice de vegetação e maior a temperatura, maior o risco
    # Quanto maior a umidade, menor o risco
    risco_queimada = (peso_vegetacao * (1 - indice_vegetacao_normalizado)) + \
                     (peso_temperatura * temperatura_normalizada) + \
                     (peso_umidade * (1 - umidade_normalizada))

    # Threshold para definir se há queimada ou não
    if risco_queimada > 0.6:
        return 1  # Queimada detectada
    else:
        return 0  # Sem queimada

# Função para avaliar o modelo com base nos dados de teste
def avaliar_modelo(dados):
    acertos = 0
    total = len(dados)

    for amostra in dados:
        indice_vegetacao, temperatura, umidade, queimada_real = amostra
        previsao = prever_queimada(indice_vegetacao, temperatura, umidade)

        if previsao == queimada_real:
            acertos += 1

    # Calculando a acurácia
    acuracia = acertos / total
    return acuracia

# Dados de exemplo (índice de vegetação, temperatura, umidade, presença de queimada)
dados_treinamento = [
    (0.6, 30, 70, 0),  # Sem queimada
    (0.2, 45, 20, 1),  # Queimada
    (0.7, 25, 85, 0),  # Sem queimada
    (0.3, 40, 25, 1),  # Queimada
    (0.8, 20, 90, 0),  # Sem queimada
    (0.9, 35, 75, 0),  # Sem queimada
    (0.1, 50, 10, 1),  # Queimada
    (0.4, 32, 50, 0),  # Sem queimada
    (0.2, 42, 30, 1),  # Queimada
    (0.5, 28, 65, 0)   # Sem queimada
]

# Avaliando o modelo com os dados de treinamento
acuracia = avaliar_modelo(dados_treinamento)
print(f"Acurácia do modelo: {acuracia * 100:.2f}%")

# Testando o modelo com um novo conjunto de dados
novos_dados = [
    (0.3, 38, 40),  
    (0.7, 25, 80),
    (0.7, 25, 50), 
    (0.4, 44, 15) 

]

print("\nPrevisões para novos dados:")
for novo_dado in novos_dados:
    indice_vegetacao, temperatura, umidade = novo_dado
    previsao = prever_queimada(indice_vegetacao, temperatura, umidade)
    resultado = "Queimada" if previsao == 1 else "Sem queimada"
    print(f"Índice de Vegetação: {indice_vegetacao}, Temperatura: {temperatura}, Umidade: {umidade} -> {resultado}")
