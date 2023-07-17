#Faça um programa que leia uma função contador(), que receba três parâmentros:início, fim, passo. Seu programa tem que realizar
#Três contagens através da função criada:
#a)De 1 até 10, de 1 em 1.
#b)De 1o até 0, de 2 em 2.
#c)Uma contagem personalizada.
from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até o {f} de {p} em {p}.')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += 1
            print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}, ',end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem! ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)