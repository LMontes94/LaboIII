
def main():
 pass
 n1 = input("Ingresar nombre: ")
 e1 = int(input("Ingresar edad: "))

 n2 = input("Ingresar nombre: ")
 e2 = int(input("Ingresar edad: "))

 n3 = input("Ingresar nombre: ")
 e3 = int(input("Ingresar edad: "))
 
 if e1 >= e2 and e1 >= e3:
    print(f"Nombre del mayor: {n1} y su edad {e1}")
 if e2 >= e1 and e2 >= e3:
    print(f"Nombre del mayor: {n2} y su edad {e2}")
 if e3 >= e1 and e3 >= e2:
    print(f"Nombre del mayor: {n3} y su edad {e3}")
 if e1 == e2 and e1 == e3:
    print("Todos tienen la misma edad")
   
if __name__ == '__main__':
    main()


