
def main():
 pass
 dia = input("Ingrese el dia: ")
 hora = int(input("Ingrese la hora: AAMM "))

 if (dia == 'Domingo' or dia == 'Sabado'):
    print("El banco esta cerrado!!")
 elif (hora > 999 and hora < 1500):
    print("Puedo ir al banco!!")
 else:
    print("El banco esta cerrado!!")
 
if __name__ == '__main__':
    main()
