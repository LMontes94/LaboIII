def comparar_digitos(num):
      primerDigit = num // 10000
      lastDigit = num % 10
      num //= 10
      num %= 1000
      secondDigit = num // 100
      anteDigit = num % 10
      if primerDigit != lastDigit or secondDigit != anteDigit:
         return False        
      return True

def main():
  pass

  num = int(input("Ingresar numero entero de 5 digitos: "))
  
  if comparar_digitos(num):
    print(f"{num} es numero capicua.")      
  else:
     print(f"{num} no es numero capicua.")

if __name__ == '__main__':
    main()
