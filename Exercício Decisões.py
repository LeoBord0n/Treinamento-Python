'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. '''

nota1 = int(input('Qual foi a primeira nota? '))
nota2 = int(input('Qual foi a segunda nota? '))
media = (nota1 + nota2) / 2
if media >= 7 and media < 10:
  print(f"Sua média foi de {media:.0f}. Aprovado!")
elif media < 7:
  print(f"Sua média foi de {media:.0f}. Reprovado!")
elif media == 10:
  print(f"Sua média foi de {media:.0f}. Aprovado com distinção!")
