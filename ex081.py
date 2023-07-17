#Crie um programa que vai ler vários números e colocar em um lista. Depois disso, crie duas listas extras que vão contar
#apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas gereadas
num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'Alsita de pares é {pares}')
print(f'A lista de ímpares é {impares}')