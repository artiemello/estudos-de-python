num = int(input("Digite o número que gostaria de converter para binário: "))

binario = ''

while num > 0:
    resto = num % 2
    binario = str(resto) + binario
    num //= 2

print(f"Esse número em binário é: {binario}")
