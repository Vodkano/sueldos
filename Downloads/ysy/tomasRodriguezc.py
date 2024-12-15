


import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]

def clasificar_sueldos():
    menores = [t for t, s in zip(trabajadores, sueldos) if s < 800000]
    intermedios = [t for t, s in zip(trabajadores, sueldos) if 800000 <= s <= 2000000]
    mayores = [t for t, s in zip(trabajadores, sueldos) if s > 2000000]
    print(f"Sueldos menores a $800.000 TOTAL: {len(menores)}")
    for t, s in zip(menores, sueldos):
        if s < 800000:
            print(f"{t} ${s}")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(intermedios)}")
    for t, s in zip(intermedios, sueldos):
        if 800000 <= s <= 2000000:
            print(f"{t} ${s}")
    print(f"Sueldos superiores a $2.000.000 TOTAL: {len(mayores)}")
    for t, s in zip(mayores, sueldos):
        if s > 2000000:
            print(f"{t} ${s}")
    print(f"TOTAL SUELDOS: ${sum(sueldos)}")

def ver_estadisticas():
    print(f"Sueldo más alto: ${max(sueldos)}")
    print(f"Sueldo más bajo: ${min(sueldos)}")
    print(f"Promedio de sueldos: ${sum(sueldos) / len(sueldos)}")
    print(f"Media geométrica de sueldos: {math.exp(sum(math.log(s) for s in sueldos) / len(sueldos))}")

def reporte_sueldos():
    with open('sueldos.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for t, s in zip(trabajadores, sueldos):
            salud = s * 0.07
            afp = s * 0.12
            liquido = s - salud - afp
            writer.writerow([t, f"${s}", f"${int(salud)}", f"${int(afp)}", f"${int(liquido)}"])
            print(f"{t} ${s} ${int(salud)} ${int(afp)} ${int(liquido)}")

def main():
    while True:
        print("\n1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            adios =  """Finalizando programa
              Desarrollado por Tomás Rodriguez
              Rut (21.375.***-*) """
            print (adios)
            
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
