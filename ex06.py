#Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

import math

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    fatorial = math.factorial(numero)
    print(f"O fatorial de {numero} é {fatorial}.")
