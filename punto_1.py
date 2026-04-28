# El MCD es el número más grande que divide exactamente a dos números sin dejar residuo
#empezamos efiniendo mcd para que reciba dos números enteros a y b, y devuelva su máximo común divisor usando el algoritmo de Euclides que se va a implementar
def mcd(a, b):
    # el ciclo while se repite mientras la condición sea verdadera
    # while b != 0" significa: hace que mientras b sea diferente de 0 ejecuta lo siguiente
    # En cada iteración del ciclo, b disminuye hasta llegar a 0
    # Cuando b llega a 0, la variable a contiene el MCD de los números originales
    while b != 0:
        # para hacer el calculo del resudio se usa el operador %
        # a % b calcula el residuo de la división a ÷ b
        # como por ejemplo seria 12 % 8 = 4 porque 12 ÷ 8 = 1 con residuo 4
        # Guardamos este residuo en la variable residuo
        residuo = a % b
        
        # para hacer la asignacion hora actualizamos los valores de a y b
        # a = b significa copia el valor de b en a
        # esto lo usamos para poder dividir números más pequeños en la siguiente iteración
        a = b
        
        # con la asignacion Ahora b recibe el valor del residuo que calculamos
        # b = residuo significa copia el valor de residuo en b
        # En la siguiente iteración se divide a que es el b anterior entre b que es el residuo
        b = residuo
    
    # con el return evolvemos el valor final de a
    # Cuando el ciclo termina ose cuando b = 0, a contiene el MCD de los dos números originales
    # Esta es la respuesta que devolveremos a quien llamó esta función
    return a

# Esta función valida que el usuario ingrese un número entero positivo
# Si el usuario ingresa algo inválido, le pedimos que lo intente de nuevo

def entero_positivo(mensaje):
    # el while True crea un ciclo que se repite indefinidamente
    # Solo termina cuando usamos return para salir de la función
    # Esto es útil para validar entrada si el usuario ingresa algo inválido se pide de nuevo
    while True:
        # con el input al usuario que escriba algo
        # input(mensaje) muestra el mensaje y espera que el usuario escriba una línea de texto
        # Lo que escribe el usuario se almacena en la variable texto como una cadena de caracteres
        # como por ejemplo si el usuario escribe 12, texto = "12" como texto, no como número
        texto = input(mensaje)
        
        # para verificarlo se verifica si el texto contiene solo dígitos
        # texto.isdigit() devuelve True si el texto son solo números (0-9)
        # Devuelve False si contiene letras, símbolos o espacios
        if texto.isdigit():
            # se convierte el texto a un número entero
            # int(texto) toma la cadena de texto y la convierte a un número entero
            # 12 (texto) se convierte en 12 (número)
            # Este número se almacena en la variable valor
            valor = int(texto)
            
            # se verifica que el número sea positivo que sea mayor a 0
            # "valor > 0" es True si valor es mayor que 0, False si es 0 o negativo
            # Solo aceptamos números positivos para nuestro algoritmo MCD
            if valor > 0:
                # con return si todo es válido, devolvemos el número
                # Salimos de la función y entregamos el valor al programa principal
                return valor
        
        # si el usurio lo hace mal dira simplemente error y el ciclo se repetira pidiendo la entrada de nuevo
        print("error")


#Esta función controla todo el flujo del programa: pide entrada y muestra resultados

def main():
    # pedimos el primer número al usuario
    # entero_positivo(...) llama a la función que definimos arriba esta función pide un número hasta que el usuario ingrese uno válido 
    # El número validado se almacena en la variable x
    # Ejemplo: si el usuario escribe 12, x = 12
    x = entero_positivo("1 numero: ")
    
    # despues pedimos el segundo número al usuario
    # De la misma manera se pide y validamos el segundo número
    # El número se almacena en la variable y como por ejemplo si el usuario escribe 8, y= 8
    y = entero_positivo("2 numero: ")
    
    # llamamos a la función mcd() con nuestros dos números
    # mcd(x, y) calcula el máximo común divisor de x y y usando el algoritmo de Euclides
    # El resultado se almacena en la variable resultado
    # como por ejemplo si mcd(12, 8) = 4, entonces resultado = 4
    resultado = mcd(x, y)
    
    # Mostramos el resultado al usuario
    # print() muestra en pantalla todos los valores separados por comas
    # Esto imprimiria el mcd  12 y 8 es: 4
    # Los valores x, y, resultado se reemplazan por sus números reales
    print("el mcd ", x, "y", y, "es:", resultado)


#if __name__ == "__main__": es una condición especial en Python que se cumple solo cuando ejecutamos el archivo directamente q si otro programa importa este archivo esta condición no se cumplesto esto hace que el archivo sea usado como biblioteca sin ejecutar main() automáticamente.

if __name__ == "__main__":
    # para que pueda empezar a ejecutar el programa, llamamos a la función main()
    # el main() hace que el programa pida entrada al usuario y muestre el resultado
    # main() lo uqe hace es que pide números al usuario y muestra el resultado del MCD
    main()
