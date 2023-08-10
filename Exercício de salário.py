'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento. '''

salario = int(input('Qual seu salário? '))
if salario <= 280 and salario > 0:
  aumento = salario + (salario * 0.2)
  diferenca = aumento - salario
  print(f"Seu salário era de R${salario}. Com o aumento, passará a receber R${aumento}, tendo a diferença de R${diferenca}(20%).")
elif salario > 280 and salario <= 700:
  aumento = salario + (salario * 0.15)
  diferenca = aumento - salario
  print(f"Seu salário era de R${salario}. Com o aumento, passará a receber R${aumento}, tendo a diferença de R${diferenca}(15%).")
elif salario > 700 and salario <= 1500:
  aumento = salario + (salario * 0.10)
  diferenca = aumento - salario
  print(f"Seu salário era de R${salario}. Com o aumento, passará a receber R${aumento}, tendo a diferença de R${diferenca}(10%).")
elif salario > 1500:
  aumento = salario + (salario * 0.05)
  diferenca = aumento - salario
  print(f"Seu salário era de R${salario}. Com o aumento, passará a receber R${aumento}, tendo a diferença de R${diferenca}(5%).")
else:
  print('Seu salário não pode ser 0')


