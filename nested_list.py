if __name__ == '__main__':
    """Given the names and grades for each student in a class of N students,
     store them in a nested list and print the name(s) of any student(s)
     having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line."""

    dicio = {}
    valores = []
    chaves = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dicio[name] = score
    for nota in dicio.values():
        valores.append(nota)
    menor = min(valores)
    valores.remove(menor)
    while menor in valores:
        valores.remove(menor)
    for nota2 in valores:
        if nota2 == min(valores):
            for chave, valor in dicio.items():
                if valor == nota2:
                    if chave not in chaves:
                        chaves.append(chave)
                    else:
                        break
    chaves.sort()
    for x in chaves:
        print(x)
