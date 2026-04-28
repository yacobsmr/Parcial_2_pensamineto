# El factorial de un número n es el producto de todos los números enteros positivos desde 1 hasta n
# Usamos esta función para calcular los denominadores en la serie de Taylor

def facto(n):
    # Creamos una variable llamada resultado y le asignamos el valor inicial 1
    # Empezamos en 1 porque cuando multiplicamos, el numero neutro es 1
    resultado = 1
    
    # con el ciclo for repetimos un bloque de código varias veces
    # el range genera una secuencia de números desde 1 hasta n 
    # En cada iteración, la variable o toma un valor diferentecomo por ejemplo seria 1, 2, 3, ... y asi hasta llegar a n
    for o in range(1, n + 1):
        # Multiplicamos el resultado anterior por el número actual osea o
        # resultado = resultado * o significa que toma el valor anterior de resultado, multiplícalo por o, y guarda el nuevo valor
        # Iteración 1: resultado = 1 * 1 = 1
        # y asi hasta q se complete el ciclo
        resultado = resultado * o
    
    # el return no que hace es que al terminar el ciclo devolvemos el resultado final para que otras funcionen utilizen el factorial calculado
    return resultado


# FUNCIÓN PARA CALCULAR LA SERIE DE TAYLOR DE e^x
# Cuantos más términos sumemos, más precisa es la aproximación
# definimos ex_taylor que recibe dos parámetros: x que ews el número al que queremos calcular e^x y n que esla cantidad de términos de la serie que vamos a sumar
def ex_taylor(x, n):
    # Inicializamos una variable suma con valor 0
    # Esta variable acumulará todos los términos de la serie
    suma = 0
    
    # con el ciclo for epetimos el cálculo para cada término de la serie
    # range(0, n + 1) genera números desde 0 hasta n 
    # Cada valor de o representa el exponente y el índice del factorial
    for o in range(0, n + 1):
        # x ** o significa x elevado a la potencia o como por ejemplo 2**3 = 8
        # facto(o) calcula o factorial com oejemplo facto(3) = 6
        # Dividimos x^o entre o! para obtener el término
        termino = (x ** o) / facto(o)
        
        # sumamos el término calculado al valor anterior de suma
        # suma = suma + termino significa que toma la suma anterior sumarle el termino actual y x guarda el nuevo valor
        # Iteración 0: suma = 0 + (x^0/0!) = 0 + 1 = 1
        # Iteración 1: suma = 1 + (x^1/1!) = 1 + x
        # y asi sucesivamente hasta completar n términos de la serie
        suma = suma + termino
    
    # con el return devolvemos la suma total de todos los términos
    return suma

# Esta función controla el flujo principal del programa
# en este caso pedimos entrada al usuario y mostramos los resultados

def main():
    # con el input pedimos al usuario que ingrese un número el cual representara el valor x
    # input() muestra el mensaje entre paréntesis y espera que el usuario escriba algo
    # float() convierte el texto que escribe el usuario en un número decimal
    # La variable x almacena este número para usarlo después
    x = float(input("x: "))
    
    # esta vez con el input pedimos al usuario que ingrese otro número osea la cantidad de términos n
    # int() convierte el texto en un número entero sin decimales
    # La variable n almacena este número
    n = int(input("n: "))
    
    # llamamos a la funcion y jecutamos la función ex_taylor con nuestros valores x y n
    # ex_taylor calcula e^x usando n términos de la serie de Taylor
    # El resultado se guarda en la variable resultado
    resultado = ex_taylor(x, n)
    
    #  mostramos el resultado en la pantalla
    # print() como se sabe es la función que imprime valores y texto
    # Sin argumentos de formato, simplemente muestra el número
    print(resultado)


# if __name__ == "__main__ es una condición especial en Python
# Esto se cumple SOLO cuando ejecutamos el archivo directamente
# Si otra programa importa este archivo, esto NO se ejecuta
# Cuando se cumple, llamamos a main() para comenzar la ejecución del programa

if __name__ == "__main__":
    # Ejecutamos la funcion main() para iiniciar el programa
    # el main() hace que el programa pida entrada al usuario y muestre el resultado de ex 
    main()
