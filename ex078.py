#Crie um programa onde o usuário possa digitar vários valores numéricos e cadraste-os em uma lista. caso Caso o número já exista lá dentro
#Ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem decrescente.
números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar[S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')