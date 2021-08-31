def main():
  #escribe tu código abajo de esta línea
  #Carlos Peña Gutiérrez 
  #A01661455

 def ba(base,altura):
    area=base*altura
    return area

 def volum(prof,area):
    v= area * prof
    return v


base=float(input("Dame la base: "))
altura=float(input("Dame la altura: "))
prof=float(input("Dame la profundidad: "))

volum= (base*altura*prof)
salida= (volum)
print("El volúmen del prisma es: ",salida)

if __name__ == '__main__':
    main()

