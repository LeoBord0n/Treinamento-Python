'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''
print('Responda com "s" ou "n" ')
suspeito = 0
p1 = input('Telefonou para a vítima? ')
if p1 == 's':
  suspeito = suspeito + 1
p2 = input('Esteve no local do crime? ')
if p2 == 's':
  suspeito = suspeito + 1
p3 = input('Mora perto da vítima? ')
if p3 == 's':
  suspeito = suspeito + 1
p4 = input('Devia para a vítima? ')
if p4 == 's':
  suspeito = suspeito + 1
p5 = input('Já trabalhou com a vítima? ')
if p5 == 's':
  suspeito = suspeito + 1
if suspeito == 2:
  print('Suspeito')
elif suspeito == 3 or suspeito == 4:
  print('Cúmplice')
elif suspeito == 5:
  print('Assassino')
else:
  print('Inocente')

