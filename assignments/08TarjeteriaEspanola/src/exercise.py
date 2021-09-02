#A01661455 Carlos Peña Gutiérrez

def maxpapel(papel,plumones):
    max=papel*12
    maxplum=plumones*35

    if maxplum>max:
        total=max
    elif max>maxplum:
        total=maxplum

    return total

def main():
    #escribe tu código abajo de esta línea
    pass
    papel=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))

    total= maxpapel(papel,plumones)
    print("El número máximo de tarjetas que se pueden hacer es: ",total)
if __name__=='__main__':
    main()

