Previsão de Queimadas com Inteligência Artificial Simples
Descrição
Este projeto utiliza uma abordagem simples de inteligência artificial para prever o risco de queimadas em determinadas regiões. Com base em variáveis ambientais como o índice de vegetação, temperatura e umidade relativa do ar, o modelo calcula uma pontuação de risco e determina a probabilidade de uma queimada. O objetivo é fornecer uma ferramenta básica que possa ser aplicada ao monitoramento de áreas propensas a incêndios florestais, utilizando apenas operações matemáticas e lógica de programação sem dependência de bibliotecas externas.

Funcionalidades
Previsão de Queimadas: O modelo utiliza dados de vegetação, temperatura e umidade para prever se há risco de queimada.
Modelo Baseado em Regras: Usa uma combinação ponderada das variáveis para calcular a probabilidade de queimada.
Sem Dependência de Bibliotecas: Todo o código foi escrito usando apenas operações matemáticas e variáveis básicas, sem bibliotecas externas.
Como Funciona
Coleta de Dados: O modelo recebe como entrada três variáveis: índice de vegetação (0 a 1), temperatura (em graus Celsius) e umidade relativa do ar (%).
Normalização: Os dados são normalizados para que todas as variáveis estejam em uma escala de 0 a 1.
Cálculo de Risco: Através de uma fórmula que combina os valores normalizados com pesos específicos para cada variável, o modelo calcula o risco de queimada.
Classificação: Se o risco for maior que 0.6, o modelo prevê a ocorrência de uma queimada. Caso contrário, prevê que não haverá queimada.
