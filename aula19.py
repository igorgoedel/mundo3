pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(pessoas)

print(pessoas['nome'])#Na hora de enunciar os elemntos usa-se colchetes e na hora de declarar os elementos usa-se chaves.

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')#Dentro de aspas simples, usase aspas duplas.

print(pessoas.keys())

print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'Leandro'#Também posso modificar um dicionário.

pessoas['peso'] = 98.5#Posso adicionar mais itens ao dicionário.