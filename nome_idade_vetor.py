if __name__ == '__main__':

    nomes = []

    i = 0
    while (i < 5):
        nomes.append(input("DIGITE SEU NOME:"))
        i = i+1
    print ("NOMES REGISTRADOS!!!")
    print (f"ESSES SÃO OS NOMES OBTIDOS:{nomes}")

    idades = []

    contador = 0
    while (contador < 5):
        idades.append(int(input("DIGITE AS IDADES:")))
        contador = contador + 1
    print ("IDADES REGISTRADAS!!!")
    print (f"ESSAS SÃO OS NOMES E IDADES OBTIDOS:{nomes}")
    print (idades)


