def guardar_tabla(numero):
    if 1 <= numero <= 10:
        with open(f"tabla-{numero}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{numero} x {i} = {numero * i}\n")
        print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
    else:
        print("El número debe estar entre 1 y 10")

def mostrar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe")


while True:
        print("\nMenu:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla(numero)
        elif choice == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_archivo(f"tabla-{numero}.txt")
        elif choice == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input(f"Ingrese el número de línea (1-10) de la tabla del {numero}: "))
            mostrar_archivo(f"tabla-{numero}.txt")
        elif choice == "4":
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
