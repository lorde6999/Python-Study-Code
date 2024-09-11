nome = input(" Digite seu Nome: ")
nota1 = int(input(" Digite a Primeira Nota: "))
nota2 = int(input(" Digite a Segunda Nota: "))
nota3 = int(input(" Digite a Terceira Nota: "))
media = (nota1+nota2+nota3)/3
if media >= 7:
    print(f"{nome}, sua média é: , {media}, E você está aprovado!")
elif media >= 4:
    print(f"{media}Você está em recuperação!")
else:
    print(f"{nome}, sua média é: , {media}, E você infelizmente está reprovado!")