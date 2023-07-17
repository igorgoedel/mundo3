#Faça um programa que leia 5 valores números e guarde-os em uma lista. No final mostre qual foi o maior e quel foi o menor
#Valor digitado e sua respectivas posiçoes na lista.
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores [c] > mai:
            mai = valores[c]
        if valores [c] < men:
            men = valores[c]
print('=-' * 30)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor digitado foi {mai}, nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == mai:
        print(f'{indice}... ', end='')
print()
print(f'O menor valore digitado foi {men}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}... ', end='')
print()