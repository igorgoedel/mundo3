#Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre
#A) Os 5 primeiros colocados
#B) Os ultimos 4 colocados
#C) Times em ordem afabetica
#D) Em que posição está o time chapecoense.
Times =  ('Botafogo', 'Palmeiras','Atlético Mineiro','Grêmio','Flamengo','Fluminense','Atlético Paranaense','São paulo','Fortaleza','Cruzeiro','Red Bull Bragantino','Santos','Internacional','Cuiabá','Bahia','Corinthians','Goias','America','Vasco','Coritiba')
print('=-'* 30)
print('Cinco Primeiros colocados.')
print(Times[0:5])
print('=-'* 30)
print('Ultimos quatro colocados.')
print(Times[16:])
print('=-'* 30)
print('Times em ordem alfabética.')
print(f'{sorted(Times)}')
print('=-'* 30)
print(Times[2])