def informarDias(mes, anio):
   match mes:
      case 1,3,5,7,8,10,12:
         print(f"El mes {mes} tiene 31 dias")
      case 4,6,9,11:
         print(f"El mes {mes} tiene 30 dias")
      case 2:
         if anio % 4 == 0 and anio % 100 and anio % 400:
            print(f"El mes {mes} tiene 29 dias")
         else:
            print(f"El mes {mes} tiene 28 dias")
            
def main():
 pass
 mes = int(input("Ingrese mes: "))
 anio = int(input("Ingrese año: "))

 informarDias(mes,anio)

if __name__ == '__main__':
    main()

