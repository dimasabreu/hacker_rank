
check = []
qnt = int((input()))
UID = []
repetidos = 0


while qnt != 0:
    UID.append(input())
    qnt -= 1


for elemento in UID:
    var = len(elemento)
    if var == 10:
        timer = 10
        for letra in elemento:
            if timer != 1:
                if letra not in check:
                    check.append(letra)
                    timer -= 1
                else:
                    repetidos += 1
                    timer -= 1
            else:
                if repetidos != 0:
                    print("Invalid")
                    repetidos = 0
                    check.clear()
                else:
                    print("Valid")
                    repetidos = 0
                    check.clear()
    else:
        print("Invalid")
