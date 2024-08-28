#Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

maximo = int(input("Digite o valor máximo para a sequência de Fibonacci: "))

a, b = 0, 1

print("Sequência de Fibonacci:")
while a <= maximo:
    print(a, end=' ')
    a, b = b, a + b
