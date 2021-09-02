#Carlos Peña Gutiérrez 
#A01661455
import math 

 #escribe tu código abajo de esta línea

def bisiesto(year):
    if (year%4==0):
      tipo=True
    else:
      tipo=False
    return tipo

def main():
    year=int(input())

    tipoa=bisiesto(year)
    print(tipoa)
  
if __name__=='__main__':
    main()
