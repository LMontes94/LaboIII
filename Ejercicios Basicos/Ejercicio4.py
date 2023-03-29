def main():
  pass

  c1 = int(input("Ingrese el valor del primer cateto: "))
  c2 = int(input("Ingrese el valor del segundo cateto: "))
  h = int(input("Ingrese el valor de la hipotenusa: "))

  if (h**2) == (c1**2) + (c2**2):
     print("Es un triangulo rectangulo!!")
  else:
     print("Noo es un triangulo rectangulo!!")  
     
if __name__ == '__main__':
    main()