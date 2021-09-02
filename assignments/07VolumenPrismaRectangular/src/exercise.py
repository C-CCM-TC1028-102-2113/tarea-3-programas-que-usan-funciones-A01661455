#A01661455 Carlos Peña Gutiérrez
#escribe tu código abajo de esta línea

def ba(base,altura):
    area=base*altura
    return area

def volum(prof,area):
    v= area * prof
    return v

def main():

   base=float(input("Dame la base: "))
   altura=float(input("Dame la altura: "))
   prof=float(input("Dame la profundidad: "))

   area= ba(base,altura)

   vol= volum(prof,area)

   print("El volúmen del prisma es: ",vol)

if __name__ == '__main__':
    main()

