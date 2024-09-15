tent = 0
senhac = int(input("Cadastre sua senha: "))
while tent <3:
    senhae = int(input("Digite sua senha para entrar: "))
    if senhae == senhac:
        tent += 3
        print(f"Seu saldo é de: R$43.120,23")
    else:
        tent += 1
        print(f"Senha errada, digite novamente!")
if senhae != senhac:
    tent +=1
    print("Por motivos de segurança sua senha foi bloqueada!")