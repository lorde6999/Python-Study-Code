numero = int(input("Digite um número: "))
resultado = numero % 2 == 0
if resultado:
    print(f"{numero} é par")
else:
    print(f"{numero} é impar")
