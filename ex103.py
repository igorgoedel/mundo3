#Crie um programa que tenha a função leiaint(), que vai funcionar de froma semelhante á função input() do python só que fazendo
#a validação para aceitar apenas um valor númerico.
#Ex: n = leiaint('Digite um n')
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok =True
        else:
            print('Erro!, Digíte um número inteiro válido.')
        if ok:
            break
    return valor



n = leiaint(('Digite um número: '))
print(f'Você acabou de digitar o número {n}.')