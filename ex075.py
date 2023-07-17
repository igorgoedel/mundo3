#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequêcia. No final mostre uma listagem de preços, organizando em um aforma tabular.
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.33,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print('LISTAGEM DE PREÇO')
for pos in range (0, len(listagem)):
    if pos % 2 == 0:#Se a posiÇao do item na listagem for par. É o nome do produto.
        print(f'{listagem[pos]}:.<30', end='')#Se for par ele mostra o nome do produto
    else:#Aqui ele vai mostrar o preço.
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)