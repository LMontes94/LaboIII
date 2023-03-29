

def main():
    nota1 = int(input('Ingresa tu primer nota: '))
    nota2 = int(input('Ingresa tu segunda nota: '))
    nota3 = int(input('Ingresa tu tercer nota: '))

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio < 4:
      print('Insuficiente')

    if promedio <= 4 and promedio < 7:
       print('Regular')
    
    if promedio >= 6 and promedio < 9:
       print('Bien')

    if promedio >= 8 and promedio < 10:
       print('Muy Bien')

    if promedio >= 9 and promedio < 11:
       print('Sobresaliente')    

if __name__ == '__main__':
    main()
