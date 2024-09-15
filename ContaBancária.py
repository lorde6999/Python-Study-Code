tent = 0

nome = input("Cadastre seu nome e sobrenome: ")
cpf1 = int(input("Cadastre seu CPF: "))
senhac = int(input("Cadastre sua senha: "))
while tent <3:
    cpf2 = int(input("Digite seu CPF para entrar: "))
    senhae = int(input("Digite sua senha para entrar: "))
    if cpf1 == cpf2 and senhae == senhac:
        tent += 3
        print(f"Bem vindo ao ZamorBank Senhor(a), {nome}. Seu saldo é de R$42.154,00: ")
    else:
        tent += 1
        print(f"Senha errada, digite novamente!")
if senhae != senhac and cpf1 != cpf2:
    tent +=1
    print("Por motivos de segurança sua senha foi bloqueada!")