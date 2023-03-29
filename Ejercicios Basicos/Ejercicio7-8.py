
def main():
 pass

 fecha = int(input("Ingresar fecha de nacimiento: formato AAAAMMDD "))

 anio = fecha // 10000
 dia = (fecha % 100) 
 mes = (fecha % 10000) // 100
 anioActual = 2023
 if anioActual - anio > 18:
  print("Es mayor de edad!!")
 else:
   print("No es mayor de edad")
if __name__ == '__main__':
    main()
