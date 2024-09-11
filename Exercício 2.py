nome = input(" Digite seu Nome: ")
nota1 = float(input(" Digite a Primeira Nota: "))
nota2 = float(input(" Digite a Segunda Nota: "))
media = (nota1+nota2)/2
if media <7:
    print(f"{nome}, sua média é: , {media}, Você está reprovado!")
else:
    print(f"{nome}, sua média é: , {media}, Você está aprovado, parabéns!")