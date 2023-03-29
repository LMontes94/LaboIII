
def main():
  pass
  sexo = input("Ingresar sexo: (M o H): ")
  edad = int(input("Ingresar edad: "))
  aniosTrabajados = int(input("Ingresar la cantidad de años trabajados: "))
  
  if sexo == 'M' and edad >= 60 and aniosTrabajados >= 30:
     print("Usted se puede jubilar.")
  elif sexo == 'H' and edad >= 65 and aniosTrabajados >= 30:
    print("Usted se puede jubilar.")
  else:
     print("Usted no se puede jubilar.")

  
if __name__ == '__main__':
    main()

