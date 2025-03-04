numero = 100000

while True:
    bandera = False
    for x in range(2, int(numero/2)):
            if(numero % x == 0):
                        bandera = True
                        break #romper el primer ciclo

    if(bandera == False):
                print(f" {numero}")
                numero + 1 