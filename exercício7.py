time1 = input("Digite o nome do time 1: ")
time2 = input("Digite o nome do time 2: ")
gols1 = int(input(f"Digite o número de gols feito pelo {time1}: "))
gols2 = int(input(f"Digite o número de gols feito pelo {time2}: "))
if gols1>gols2:
    print(f"{time1}, vencedor com um total de: , {gols1}, gol(s)")
elif gols1==gols2:
    print("A partida empatou!")
else:
    print(f"{time2}, vencedor com um total de: , {gols2}, gol(s)")
