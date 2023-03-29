def categoria_socio(socio):
  if socio < 12:
    print("Categoria del socio: Menor")

  if socio > 12 and socio < 19:
    print("Categoria del socio: Cadete")

  if socio > 17 and socio < 27:
    print("Categoria del socio: Juvenil")

  if socio > 26:
    print("Categoria del socio: Mayor")

def main():
 pass
 socio = int(input("Ingresar edad: "))

 categoria_socio(socio)
 
if __name__ == '__main__':
    main()