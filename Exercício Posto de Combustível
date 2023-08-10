"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        até 20 litros, desconto de 3% por litro
        acima de 20 litros, desconto de 5% por litro
    Gasolina:
        até 20 litros, desconto de 4% por litro
        acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros = int(input('Quantos litros você deseja colocar? '))
comb = input('"a" para Álcool e "g" para gasolina. ')
preco = 0
if comb == 'a':
    preco = 1.9 * litros
    if litros <= 20:
        preco -= (1.9 * litros) * 0.03
    elif litros > 20:
        preco -= (1.9 * litros) * 0.05
if comb == 'g':
    preco = 2.5 * litros
    if litros <= 20:
        preco -= (2.5 * litros) * 0.04
    elif litros > 20:
        preco -= (2.5 * litros) * 0.06
print(f"O preço com o desconto aplicado será de {preco:.2f}")



