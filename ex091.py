#CRie um programa que leia o nome, o ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
#Se por acaso a CPTS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
#Alem da idade, com quantos anos a pessoas vai se aposentear.
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados ['contraação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'   -{k} tem o valor de {v}')