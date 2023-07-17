#Faça um programa que leia nome e peso de varias pessoas, guardadno tudo em uma lista e no final mostre:
#a)Quantas pessoas foram cadastradas.
#b)Uma listagem com as pessoas mais pesadas.
#c)Uma listagem com as pessoas mais leves.
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:#Se eu não cadrastrei ninguém ainda.
        mai = men = temp[1]#O meu maior e a mesma coisa que o meu menor que é a mesma coisa que o temp na posição 1 , que é o meu peso.
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar ?[S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {princ}.')
print(f'Ao todo você cadrastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}kg. Pseo de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()