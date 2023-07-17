num = [2, 5, 9, 1]
num[2]= 3#Jeito de alterar uma lista.
num.append(7)#Jeito de adicionar um item a lista.
num.sort()#Jeito de colocar os elementos da lista em ordem crescente.
#num.sort(reverse=True)Jeito de colocar os elemtos da lista em ordem decrescente.
num.insert(2,0)#Jeito de inserir na posiçao dois o número zero.
num.pop(2)#Comando que elimina o elemento da posição 2 da lista, o zero que foi acabado de ser colocado.
num.remove(2)#Comando que elimina o primero número colocado em parenteses, mas ele eleimina apenas um número.
print(num)
print(f'Essa lista tem {len(num)} elementos.')

#Um jeito novo de apresentar uma lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao fnail da lista')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Cheguei ao fnail da lista')

#Quando você iguala uma lista na outra, o pyhon as motifica igualmente.
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#Aqui é um exemplo de quando você faz uma copia de uma lista. Não cria uma ligação como o exemplo acima, apenas copia os itens de uma para a outra.
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
