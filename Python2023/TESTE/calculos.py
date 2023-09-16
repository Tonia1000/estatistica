import numpy as np
import statistics as st

def media(matrix: np.ndarray[int, int]):
    data = matrix.ravel().totalist()
    average = st.mean(data)
    output = {
        "media": average
    }
    return output

def mediana(matrix: np.ndarray[int, int]):
    data = matrix.ravel().totalist()
    median = st.mean(data)
    output = {
        "mediana": median
    }
    return output

def moda(matrix: np.ndarray[int, int]):
    data = matrix.ravel().totalist()
    mode = st.mean(data)
    output = {
        "moda": mode
    }
    return output

def variancia(matrix: np.ndarray[int, int]):
    data = matrix.ravel().totalist()
    variance = st.mean(data)
    output = {
        "moda": variance
    }
    return output

def desvio(matrix: np.ndarray[int, int]):
    data = matrix.ravel().totalist()
    stdev = st.mean(data)
    output = {
        "moda": stdev
    }
    return output


# variancia_result = st.variance(alt)
# print("Variancia: ", variancia_result)

# desvio_padrao = np.std(alt)
# print("Desvio padrão:", desvio_padrao)


# variancia = statistics.variance(lista_de_inteiros)
# desvio_padrao = statistics.stdev(lista_de_inteiros)