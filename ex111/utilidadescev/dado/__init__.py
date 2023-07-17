#Dentro do pacote utilidadesCev que foi criado no desafio 110, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
#que seja capaz de funcionar como uma função input(), mas com uma validação de dados par aceitar apenas valores que sejam monetários.
def LeiaDinheiro(msg):
    valido=False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\ é um Preço inválido!\033[m')
        else:
            valiod=True
            return float(entrada)