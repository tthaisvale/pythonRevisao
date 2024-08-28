#Faça um programa que calcule a média de três números inseridos pelo usuário.

print('Vamos calcular a média dos três números que serão digitados. Vamos lá! ')
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o último número: '))
soma = n1 + n2 + n3
media = soma / 3
print('A média dos números digitados é {:.2f}'.format(media))
