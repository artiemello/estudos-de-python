num = int(input("Digite o número que gostaria de converter para binário: "))

bin = ''

while num > 0:
    resto = num % 2
    bin = str(resto) + bin
    num //= 2

print(f"Esse número em binário é: {bin}")
