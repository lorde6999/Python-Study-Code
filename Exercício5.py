usuario = "Mateus"
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1<numero2:
    print(usuario, "Recebeu: ", numero1, numero2)
elif numero1==numero2:
    print("Essa porra é igual, escolhe outra: ")
else:
    print(usuario, "Recebeu: ", numero2, numero1)

#os números são iguais