
def invertir_numero(num):
    numero = 0
    while num != 0:
     numero = (10*numero) + (num % 10)

     num //= 10
    return numero

def main():
  pass

  num = int(input("Ingresar numero entero de 5 digitos: "))
  
  if num != invertir_numero(num):
     print("No es un numero capicua")
  else:
    print("Es capicua")
 
if __name__ == '__main__':
    main()

