def calcularSueldo(sueldoNeto, categoria, cantH, antiguedad):
    return (sueldoNeto + calcularBonoCategoria(categoria) + calcularSalarioFamiliar(cantH)) * calcularAntiguedad(antiguedad)

def calcularBonoCategoria(categoria):
    if categoria == "Administrativo":
        return 3000
    if categoria == "Supervisor":
        return 6000
    if categoria == "Gerente":
        return 1000

    return 0

def calcularSalarioFamiliar(cantH):
    return 350 * cantH    

def calcularAntiguedad(antiguedad):
  if antiguedad < 6 and antiguedad > 2:
    return 1 + 0.25
  if antiguedad > 5 and antiguedad < 10:
    return 1 + 0.6
  if antiguedad > 9:
    return 1 + 1
  
  return 1     
  
def main():
 pass
 sueldoNeto = float(input("Ingrese su sueldo neto: "))
 categoria = input("Ingrese su categoria: ")
 tieneH = input("Tiene hijos? S/N ")
 
 cantH = 0 
 if tieneH == 'S':
   cantH = int(input("Ingrese cuantos hijos tiene: "))

 antiguedad = int(input("Cuantos años de antiguedad tiene: "))
 
 sueldoTotal = calcularSueldo(sueldoNeto,categoria,cantH,antiguedad)
 print(f"El sueldo bruto es de {sueldoTotal}")

if __name__ == '__main__':
    main()







