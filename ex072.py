#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
#Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostra-lo por extenso.
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Desenove', 'Vinte')
while True:
    numero = int(input('Digite um número de 0 até 20: '))
    if 0 <= numero <= 20:
        break
        print('Tente novamente. ',end='')
print(f'Você digitou o número {tupla[numero]}')

#Com o desfio da aula de perguntar se ele quer continuar
num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dizaseis', 'Dizasete', 'Dizaoito', 'Dizanove', 'vinte')

while True:
    n = int(input('Digite um número: '))
    if 0 <= n <= 20:
          print(f'Digitaste o número {num[n]}')
          per = ' '
          while per not in 'SN':
                per = input('Queres continuar? ').upper().strip()
          if per in 'N':
               break
    else:
             print('Tente novamente.', end='')
print('Fim do Programa. Volte sempre')