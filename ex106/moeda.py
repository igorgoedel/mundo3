#Crie um módulo chamado moeda.py que tenha as funçoes incorporadas aumentas(), diminuir(), dobro().
#Faça também um programa que importe esse módulo e use alghumas dessas funções.
def aumentar(preco, taxa):
    res = preco + (preco * taxa/100)
    return res

def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res

def dobro(preco):
    res = preco * 2
    return res

def metade(preco):
    res = preco / 2
    return res
#Control + s, salva o código.
#Utilizei a pasta teste para fazer o meu código principal.

