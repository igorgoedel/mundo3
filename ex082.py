#Crie um programa aonde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão
#passada está com os parênteses abertos e fechados na ordem correta.
expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')#Então cada parenteses aberto eu vou ir jogando em uma pilha.
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')