def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)


# Programa principal
título(' CURSO EM VÍDEO ')
título(' PYTHON É MUITO BOM ')

def soma(a, b):
    s = a + b
    print(s)

# Programa principal
soma(4, 5)
soma(b=8, a=9)
soma(2, 1)

def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)