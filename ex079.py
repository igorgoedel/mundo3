#Crie um programa aond eo usuario possa digitar cinco valores números e cadrastre-os em uma lista, já na posição correta
#de inserção sem usar o sort(). No final mostre a lista ordenada na tela.
lista = list()#Ou lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:#Posso juntar esse if com o elif de baixo: if c == 0 or n > lista[-1]:
        lista.append(n)
    elif n > [len(lista)-1]:#Se lista for maior que do que o número que está no ultimo elemento. Esse comando pode ser também elif n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):#Enquanto a posição for menor do que len de lista. Ele vai da posição zero até a ultima posição
            if n <= lista[pos]:#Se o n é menor ou igual a lsita na posição pos, Ou seja, ele vai verificar dentro de cada posição se o número que eu quero inserir é menor ou igual a ele.
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')

#O Jeito mais simples
lista = []
for c in range (0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado com sucesso...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lsita...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em odem foram {lista}')