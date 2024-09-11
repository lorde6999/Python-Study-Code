G = 5.80
E = 4.90
comb = input("Escolha o combustível desejado. G para Gasolina e E para Etanol: ")
if comb == "G" or comb == "g":
    litros = float(input("Insira a quantidade de litros desejado: "))
    resultado = litros * G
    print(f"Você colocou: {litros:.2f} litros, o combustível escolhido foi: {comb} e o valor a ser pago será: {resultado:.2f}")
    print("Legenda: G ou g = Gasolina, E ou e = Etanol")
elif comb == "E" or comb == "e":
    litros = float(input("Insira a quantidade de litros desejado: "))
    resultado = litros * E
    print(f"Você colocou: {litros:.2f} litros, o combustível escolhido foi: {comb} e o valor a ser pago será: {resultado:.2f}")
    print("Legenda: G ou g = Gasolina, E ou e = Etanol")
else:
    print(f"Digito errado! Escolha novamente. Lembrando: G para Gasolina ou E para Etanol.")