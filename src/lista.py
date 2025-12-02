from funcion.funciones import estaEnRango, estaEnLista

# Definir la lista a verificar
lista_especial = [6, 14, 11, 3, 2, 1, 15, 19]

print("EL VERIFICADOR")
print()
print("Introduce un numero entre 0 y 20")
print()

# Solicitar el número al usuario
numero_texto = input("Introduce un numero: ")

try:
    numero = int(numero_texto)
    
    # Verificar que el número está en el rango 0-20 (min y max de la lista)
    if estaEnRango(numero, 1, 19):
        print("El número " + str(numero) + " está en el rango valido (0-20)")
        
        # Verificar si el número está en la lista
        if estaEnLista(numero, lista_especial):
            print("¡Correcto! El número " + str(numero) + " sí está en la lista especial")
        else:
            print("El número " + str(numero) + " NO esta en la lista especial")
    else:
        print("Error: El numero " + str(numero) + " NO esta en el rango valido (0-20)")
        print("Por favor, introduce un numero entre 0 y 20")

except ValueError:
    print("Error: Debes introducir un numero valido")
