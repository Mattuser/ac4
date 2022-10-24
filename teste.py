import pandas as pd
import numpy as np
from scipy.stats import norm

amostra = [509, 505, 495, 510, 496, 509, 497, 502, 503, 505,
           501, 505, 510, 505, 504, 497, 506, 506, 508, 505,
           497, 504, 500, 498, 506, 496, 508, 497, 503, 501,
           503, 506, 499, 498, 509, 507, 503, 499, 509, 495,
           502, 505, 504, 509, 508, 501, 505, 497, 508, 507]

amostra = pd.DataFrame(amostra, columns=['Amostra'])
print(amostra.head())

media_amostra = amostra.mean()[0]
desvio_padrao_amostral = amostra.std()[0]

media = 500 
significancia= 0.05
confianca = 1 - significancia
n = 50

#passo 2 (responder as perguntas)
#caso n conheço o desvio padrão populacional, calculo o desvio padrão amostral


#passo 3 fixação da significância do teste
#quando o problema é bicaudal a gente faz isso
#quando não é, a gente da direto o valor de confiança
probabilidade = 0.5 + (confianca/2)

#obtendo za/2
valor_de_z = norm.ppf(probabilidade)
print(valor_de_z)


#passo 4 - cálculo da estatística-teste e verificação desse valor com as áreas de aceitação e rejeição do teste
#estatistica teste é uma segunda forma de aceitar ou rejeitar uma hipótese
#z_critico = media amostral - media populacional dividido pelo desvio amostral sobre a raiz do tamanho da minha população
#quando cai na zona critica, rejeito o H0

zc = (media_amostra - media) / (desvio_padrao_amostral/np.sqrt(n))
print(zc)