def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


n1 = LeiaInt('Digite um valor: ')
n2 = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1}, e o valor real foi {n2}.')