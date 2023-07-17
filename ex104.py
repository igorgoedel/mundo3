#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes informações.
# - Quantidade de notas.
# - A maior nota.
# - A menor nota.
# - A média da turma.
# - A situação (opcional).
#Adicione também as docstrings.
def notas(*n, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos aceitas(aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informaçõessobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

    return r

#Programa principal
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)