#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
#e mostrea a área do terreno.
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno com {larg}x{comp} é de {a}m ')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)