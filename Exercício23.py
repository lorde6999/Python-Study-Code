aluno = input("Digite o nome do aluno: ")
opcao = 1

while opcao == 1:

    nota1 = float(input("Digite a primeira nota de 0 a 10 do aluno: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Você errou. Digite novamente a primeira nota: "))

    nota2 = float(input("Digite a segunda nota de 0 a 10 do aluno: "))

    while nota2 < 0 or nota2 > 10:
        nota2 = float(input(f"Você errou. Digite novamente a segunda nota: "))

    resul = (nota1 + nota2)/2
    print(f"A média do aluno foi: {resul}")
    opcao = int(input("Se deseja continuar digite 1, caso contrário 2: "))