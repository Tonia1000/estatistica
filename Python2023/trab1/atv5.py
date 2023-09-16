#calcular a variancia e o desvio padrão
import statistics
import numpy as np

alt = [1.73, 1.81, 1.63, 1.80, 1.9, 1.73, 1.7, 0.2, 1.7, 1.93, 1.75, 1.78, 1.68, 1.7, 1.67]

variancia_result = statistics.variance(alt)
print("Variancia: ", variancia_result)

desvio_padrao = np.std(alt)
print("Desvio padrão:", desvio_padrao)

