'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo), 10% para o INSS e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor de seu salário e retornar com o holerite.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. '''

salario_bruto = int(input('Qual seu salário? '))
if salario_bruto <= 900:
  impr = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
  impr = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
  impr = 10
elif salario_bruto > 2500:
  impr = 20

IR = salario_bruto * (impr / 100)
FGTS = salario_bruto * (11/100)
INSS = salario_bruto * (10/100)
TD = IR + INSS 
liquido = salario_bruto - TD
print(
  f"\nSalário Bruto:             : R$ {salario_bruto:.2f}"
  f"\n(-) IR ({impr}%)               : R$ {IR:.2f}"
  f"\n(-) INSS (10%)             : R$ {INSS:.2f}"
  f"\nFGTS (11%)                 : R$ {FGTS:.2f}"
  f"\nTotal de descontos         : R$ {TD:.2f}"
  f"\nSalário Liquido            : R$ {liquido:.2f}"
)

