'''Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; '''
nome = input('Digite seu nome: ')
while True:
  if len(nome) <= 3:
    print('O nome não pode ter 3 caracteres. ')
    nome = input('Digite seu nome: ')
  else:
    break
idade = int(input('Digite sua idade: '))
while True:
  if idade <= 0 or idade > 150:
    print('A idade é inválida. ')
    idade = int(input('Digite sua idade: '))
  else:
    break
salario = int(input('Digite seu salário: '))
while True:
  if salario <= 0:
    print('O salário não pode ser 0. ')
    salario = int(input('Digite seu salário: '))
  else:
    break
sexo = input('Digite masculino ou feminino: (M/F)').lower()
while True:
  if sexo != 'm' and sexo != 'f':
    print('O sexo é inválido.')
    sexo = input('Digite masculino ou feminino: (M/F) ').lower()
  else:
    break
ec = input('Digite seu estado civil: (S,C,D,V) ').lower()
ecc = ['s','c','d','v']
while True:
  if ec not in ecc:
    print('O estado civil é inválido.')
    ec = input('Digite seu estado civil: (S,C,D,V) ').lower()
  else:
    break
print('Cadastro criado com sucesso! Segue as informações: ')
print(
            f"\n Nome: {nome.capitalize()}"
            f"\n Idade: {idade}"
            f"\n Salário: R${salario:.2f}"
            f"\n Sexo: {sexo.capitalize()}"
            f"\n Estado civil: {ec.capitalize()}")
        


  
    

            





