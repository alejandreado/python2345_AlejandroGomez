def esBinario(strbinario):
    # Verificar que la cadena no esté vacía
    if len(strbinario) == 0:
        return False
    
    # Recorrer cada carácter de la cadena
    for caracter in strbinario:
        # Comprobar si el carácter es distinto de 0 y distinto de 1
        if caracter != '0' and caracter != '1':
            return False
    
    return True

def estaEnRango(valor, minimo, maximo):
    # Parámetrosss:
    #   valor: el número introducido por el usuario
    #   minimo: valor mínimo del rango inclusive
    #   maximo: valor máximo del rango inclusive
    
    if valor >= minimo and valor <= maximo:
        return True
    else:
        return False

def estaEnLista(valor, lista):
    # Parámetros:
    #   valor: el número introducido por el usuario
    #   lista: la lista que contiene los números
    
    for elemento in lista:
        if elemento == valor:
            return True
    
    return False