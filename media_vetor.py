if __name__ == '__main__':

    notas = []


    contador = 0
    while (contador < 4):
        notas.append (int(input(f"DIGITE AS NOTAS DO ALUNO:")))
        contador = contador + 1

    print (f"Essas são as notas{notas}")

    soma = (notas[0] + notas[1] + notas[2] + notas[3])

    media = soma / 4

    print (f"A MEDIA DO ALUNO É:{media}")


