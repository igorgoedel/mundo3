#Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre nat ela algumas informações
#geradas pelas funções que já temos o módulo criado até aqui.
def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a porcentagem do aumento
    :param formato: quer saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
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


def resumo(preco=0, taxaa=10, taxar=5):
    print('=-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-=' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'O dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print('=-' * 30)

