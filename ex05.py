#Faça um programa que leia uma lista de números e retorne a média dos números pares.


entrada = input("Digite uma lista de números separados por espaço: ")

lista = list(map(int, entrada.split()))

pares = [num for num in lista if num % 2 == 0]

if pares:
    media = sum(pares) / len(pares)
    print(f"A média dos números pares é: {media:.2f}")
else:
    print("Não há números pares na lista.")
