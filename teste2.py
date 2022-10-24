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

media_amostra = 485
desvio_padrao_populacional = 20
#desvio_padrao_amostral = amostra.std()[0]

media = 500 
significancia= 0.05
confianca = 1 - significancia
n = 30

probabilidade = 0.5 + (confianca/2)

valor_de_z = norm.ppf(probabilidade)
print(valor_de_z)



zc = (media_amostra - media) / (desvio_padrao_populacional/np.sqrt(n))
print(zc)

p_valor = 2 * (1-norm.cdf(zc))
print(p_valor)
print(p_valor <= significancia)