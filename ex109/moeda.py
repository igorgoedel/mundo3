#Modifique as funções que foram criadas no desafio 106 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 107.
def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0,taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$', formato=False):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

#Control + s, salva o código.
#Utilizei a pasta teste para fazer o meu código principal.

