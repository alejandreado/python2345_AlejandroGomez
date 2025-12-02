from funcion.funciones import esBinario

print("=== Convertidor de Binario a Decimal ===")
print()

# Bucle para permitir múltiples conversiones
while True:
    numero_binario = input("Introduce un numero binario (o 'exit' para terminar): ")
    
    # Condición para salir del programa
    if numero_binario == "exit":
        print("Arrivederci!")
        break
    
    # Validar que sea binario
    if esBinario(numero_binario):
        # Convertir binario a decimal
        numero_decimal = int(numero_binario, 2)
        print("El numero binario " + numero_binario + " en decimal es: " + str(numero_decimal))
        print()
    else:
        print("Error: '" + numero_binario + "' no es un numero binario valido.")
        print("Por favor, introduce solo digitos 0 y 1.")
        print()