import sqlite3
from datetime import datetime

def crear_tabla():
    conn = sqlite3.connect("cryptos.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS bitcoin (moneda TEXT, precio REAL, fecha TEXT)""")
    conn.commit()
    conn.close()

def guardar_dato(moneda, precio):
    conn = sqlite3.connect("cryptos.db")
    cursor = conn.cursor()

    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO bitcoin (moneda, precio, fecha) VALUES (?, ?, ?)", (moneda, precio, fecha_actual))

    conn.commit()
    conn.close()

def mostrar_datos():
    conn = sqlite3.connect("cryptos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bitcoin")
    datos = cursor.fetchall()

    for fila in datos:
        print(f"Moneda: {fila[0]}, Precio: {fila[1]}, Fecha: {fila[2]}")

    conn.close()


crear_tabla()

while True:
        print("\nMenu:")
        print("1. Ingresar precio del bitcoin")
        print("2. Mostrar datos")
        print("3. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            moneda = input("Ingrese la moneda (USD, GBP, EUR): ")
            precio = float(input("Ingrese el precio del bitcoin: "))
            guardar_dato(moneda, precio)
            print("Datos ingresados correctamente.")
        elif choice == "2":
            mostrar_datos()
        elif choice == "3":
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida.")
