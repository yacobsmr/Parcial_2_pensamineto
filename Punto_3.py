# El algoritmo de burbuja compara elementos adyacentes y los intercambia si están en orden incorrecto

def ordenar_burbuja(lista):
    # se calcula cuántos elementos tiene la lista
    # len(lista) devuelve el número de elementos
    # como por ejemplo si lista = [5, 2, 8, 1], entonces n = 4
    # Guardamos este valor en n para usarlo en los ciclos
    n = len(lista)
    
    # se repite n-1 veces
    # for i in range(0, n - 1) significa que  i toma valores 0, 1, 2, ... y asi consecutiamente hasta n-2
    # range(0, n-1) genera números desde 0 hasta n-2 que no incluye n-1
    # Hacemos n-1 pasadas porque después de cada pasada, el elemento más grande está en su posición correcta
    for i in range(0, n - 1):
        # se repite el proceso de comparación dentro de cada pasada
        # for j in range(0, n - i - 2) significa que j toma valores 0, 1, 2, ..., hasta n-i-2
        #n es la cantidad total de elementos, restamos i porque en cada pasada el último elemento ya está ordenado y restamos 2 adicionales porque comparamos j con j+1, entonces el último índice válido es n-i-2
        # Ejemplo: en la 1ª pasada (i=0), j va de 0 a n-2; en la 2ª pasada (i=1), j va de 0 a n-3
        for j in range(0, n - i - 2):
            # verificamos si el elemento actual es mayor que el siguiente
            # lista[j] es el elemento en la posición j
            # lista[j+1] es el elemento en la posición j+1 
            # "lista[j] > lista[j+1]" devuelve True si j es mayor, False si no
            # Si es True, significa que están en orden incorrecto y necesitan intercambiarse
            if lista[j] > lista[j + 1]:
                # se intercambian los dos elementos de posición
                # se unsa una asignación múltiple para intercambiar
                # lista[j], lista[j+1] = lista[j+1], lista[j] significa que el nuevo lista[j] será el valor anterior de lista[j+1] y el nuevo lista[j+1] será el valor anterior de lista[j]
                # Esto es la misma operación que usar una variable temporal:
                #   temp = lista[j]
                #   lista[j] = lista[j+1]
                #   lista[j+1] = temp
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    # con returnla lista ordenada
    # Después de todos los ciclos, la lista está completamente ordenada
    # Elas listas son mutables, así que la lista original ya fue modificada
    # Pero devolvemos la referencia para que se pueda usar el resultado
    return lista

# Esta función pide al usuario una lista de números separados por espacios

def obtener_lista():
    # con la entrada pedimos al usuario que ingrese números separados por espacios
    # input() muestra el mensaje y espera que el usuario escriba
    # La entrada se almacena como una cadena de texto en "entrada"
    # Ejemplo: si el usuario escribe "5 2 8 1", entrada = "5 2 8 1"
    entrada = input("Ingrese una lista: ")
    
    # Dividimos la cadena en números individuales
    # entrada.split() divide la cadena por espacios y crea una lista de textos
    # Ejemplo: "5 2 8 1".split() = ["5", "2", "8", "1"] como textos
    # Después usamos una "list comprehension" para convertir cada texto a número entero
    # [int(x) for x in entrada.split()] significa que
    #   para cada elemento x en entrada.split(), convierte x a entero con int(x)"
    # Resultado: ["5", "2", "8", "1"] se convierte en [5, 2, 8, 1] (como números)
    # Este valor se guarda en la variable lista
    lista = [int(x) for x in entrada.split()]
    
    #Devolvemos la lista de números convertidos
    return lista



def main():
    # en la entrada pedimos una lista de números al usuario
    # obtener_lista() llama a la función que definimos arriba
    # La función pedirá números y los convertirá a una lista
    # El resultado se guarda en numeros
    # como por ejemplo si el usuario escribe "5 2 8 1", numeros = [5, 2, 8, 1]
    numeros = obtener_lista()
    
    # llamamos al algoritmo de burbuja
    # ordenar_burbuja(numeros) ordena la lista en orden ascendente menor a mayor
    # El resultado (la lista ordenada) se guarda en "ordenada"
    # Ejemplo: [5, 2, 8, 1] se convierte en [1, 2, 5, 8]
    ordenada = ordenar_burbuja(numeros)
    
    # en la salida mostramos la lista ordenada
    # print("Lista ordenada:", ordenada) muestra el resultado en pantalla
    # Ejemplo: imprime "Lista ordenada: [1, 2, 5, 8]"
    print("Lista ordenada:", ordenada)



if __name__ == "__main__":

    main()
