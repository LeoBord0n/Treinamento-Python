'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.'''

  

saque = int(input('Quanto você deseja sacar? '))
if saque > 10 and saque <= 600:
  cem = saque // 100
  saque = saque % 100
  cinquenta = saque // 50
  saque = saque % 50
  vinte = saque // 20
  saque = saque % 20
  dez = saque // 10
  saque = saque % 10
  cinco = saque // 5
  saque = saque % 5
  um = saque

  print(
  f"\n Notas de cem:        {cem}"
  f"\n Notas de cinquenta:  {cinquenta}"
  f"\n Notas de vinte:      {vinte}"
  f"\n Notas de dez:        {dez}"
  f"\n notas de cinco:      {cinco}"
  f"\n Notas de um:         {um}"
)
else:
  print('O valor é inválido para nosso caixa.')


