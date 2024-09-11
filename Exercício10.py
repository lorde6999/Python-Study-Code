e1 = int(input("Digite apenas a HORA de entrada: "))
e2 = int(input("Digite apenas os MINUTOS de entrada: "))
e3 = int(input("Digite apenas a HORA de entrada: "))
e4 = int(input("Digite apenas os MINUTOS de entrada: "))

resul1 = e1 + e3
resul2 = e2 + e4

if resul2 >= 60:
    resul1 += 1
    resul2 -= 60
else:
    pass

if resul1 <= 12:
    print(f"O horário de saída foi: {resul1}:{resul2}")

elif resul1 > 12 and resul1 < 24:
    resul1 -= 12
    print(f"O horário de saída foi: {resul1}:{resul2}")

elif resul1 >= 24 and resul1 < 36:
    resul1 -= 24
    print(f"O horário de saída foi: {resul1}:{resul2}")

elif resul1 >= 36 and resul1 <= 48:
    resul1 -= 36
    print(f"O horário de saída foi: {resul1}:{resul2}")

elif resul1 <= 48:
    resul1 -= 48
    print(f"O horário de saída foi: {resul1:02d}:{resul2}")

else:
    print("Horário indisponível.")