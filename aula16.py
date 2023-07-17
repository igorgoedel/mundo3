lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])#O elemnto 3 é ignorado na hora do fatiamento.
print(lanche[:2])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi demais.')

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(cont)

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(lanche[cont])

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posiçao {cont}')

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')#Aqui ele mostra a tupla em ordem.
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(d)
print(c)

#Aqui ele vai mostrar quantas vezes aparecem o 5 em c.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))

#Aqui ele vai mostrar em que posição está o número 8.
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.index(8))