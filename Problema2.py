from pyfiglet import Figlet
import random

figlet = Figlet()

fuente_l = figlet.getFonts()
print("Fuentes para seleccionar:")
for font in fuente_l:
    print(font)

seleccion_de_fuente = input("Ingresa el nombre de la fuente que se di en la anterior lista (Deje el espacio en blanco para fuente aleatoria): ")
if not seleccion_de_fuente:
    seleccion_de_fuente = random.choice(fuente_l)

figlet.setFont(font=seleccion_de_fuente)

texto = input("Ingrese algun texto para colocar la fuente: ")
retexto = figlet.renderText(texto)

print(retexto)
