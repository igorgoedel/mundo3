#Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanha adaptável.
def escreva(msg):
    tam = len(msg) + 4
    print('*' * tam)
    print(f' {msg}')
    print('*' * tam)


#Programa principal
escreva('Igor Goedel')
escreva('Curso de python')
