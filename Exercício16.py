soma = 0
for x in range(0,10,1):
    num = int(input("Digite 10 números aleatórios e o resultado final será a soma APENAS dos ímpares: "))
    if num % 2 != 0:
        soma = soma + num
print(f" A soma dos números ímpares foi de: {soma}")
