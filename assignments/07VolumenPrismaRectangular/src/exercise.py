#Volúmen de un prisma rectangular 
# A01661455 Carlos Peña Gutiérrez 

def main():
  #escribe tu código abajo de esta línea

 def ba(base,altura):
  area=base*altura
  return area

 def volumen(area,prof,vol):
  vol=area*prof
  return vol, area

base=float(input("Dame la base: "))
altura=float(input("Dame la altura: "))
prof=float(input("Dame la profundidad: "))

salida= (vol)
print(salida)

if __name__ == '__main__':
    main()
