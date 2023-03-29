
def main():
  pass

  l1 = int(input("Ingrese el valor del primer lado: "))
  l2 = int(input("Ingrese el valor del segundo lado: "))
  l3 = int(input("Ingrese el valor del tercer lado: "))

  if (l1 + l2) < l3 or (l1 + l3) < l2 or (l2 + l3 < l1):
     print("No es Triangulo")
  else:
     print("Forman un triangulo")
     
if __name__ == '__main__':
    main()