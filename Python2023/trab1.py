import random
# Atividade 1
# Escreva um algoritmo em python, que salve na memória ram uma matriz com 1M de elementos inteiros gerados aleatoriamente.
def atv1(x):
    t_elementos = 1000000
    l = 1000
    c = 1000
    m=[
        [random.randint(0,100)for i in range(c)]
        for j in range(l)
        
        ]

    x = x-7
    print(x)

''''
# Atividade 2
# Escreva uma função em python que receba como entrada uma matriz de inteiros e retorne como saída um dicionário contendo os valores de média, mediana e moda da matriz de entrada
def atv2():
    m =  [ [0 for i in range(4)] for j in range(4)]
    d = ({"Media":'', "Mediana":'', "Moda":''})

    for posicao, x in enumerate(range(0,10)):
       print(posicao, x)



# Atividade 3
# Escreva um algoritmo que receba uma matriz de inteiros como entrada e retorne um array contendo as medianas de cada linha da matrix. 
def atv3():
    m = [[]]
'''
# Atividade 4
# Escreva um algoritmo principal que execute e teste os algoritmos das questões anteriores (1, 2, 3)
def main():
    x = 8
    atv1(x)

