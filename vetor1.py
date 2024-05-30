if __name__ == '__main__':

    numeros = []

    contador = 0
    while (contador < 5):

        num = int(input(f"DIGITE UM NUMERO:"))
        numeros.append (num)
        contador = contador + 1

    print ("lEITURA INVERSA FINALIZADA:")

    i = 0
    while (i < 5):
        print (numeros[i])
        i = i + 1

    print ("Ordem inversa")

    i = 4
    while (i >= 0):
        i = i - 1
        print (numeros[i])

