# Parcial_2_pensamineto

# ANALISIS

# punto 1
El algoritmo encuentra el Máximo Común Divisor basándose en el principio de que el MCD de dos números también divide exactamente a su residuo en cada una de las itirenaciones calcula el residuo de la división y luego actualiza los valores despues el divisor pasa a ser el dividendo y el residuo se convierte en el nuevo divisor y el proceso termina invariablemente porque en cada paso el divisor se hace más pequeño hasta que el residuo es exactamente cero comparado con un método ingenuo que probaría todos los divisores posibles uno por uno Euclides es muchísimo más rápido y eficiente al saltarse todas esas comprobaciones innecesarias.

# punto 2
cada término matemático se construye dividiendo un numerador x elevado a la potencia actual entre un denominador osea el factorial de esa misma posición. La variable n influye directamente en la precisión entre mayor sea su valor más fracciones se sumarán y el resultado final se acercará mucho más al valor real exacto pero el costo computacional de esta implementación es ineficiente, ya que recalcula el factorial desde cero en cada iteración en lugar de aprovechar el cálculo del paso anterior, generando multiplicaciones redundantes y pesadas.

# punto 3
Este método organiza una lista recorriéndola repetidamente y comparando pares de números adyacentes si el de la izquierda es mayor los intercambia, haciendo que los números más grandes burbujeen rápidamente hacia el finalel problema es q su complejidad temporal es cuadrática debido a que utiliza un ciclo anidado dentro de otro ciclo lo que multiplica drásticamente las operaciones según la cantidad de elementospor eso es que su eficiencia para listas grandes es muy deficiente ya que el tiempo de procesamiento se dispara a tal punto que resulta inútil en la vida real si se compara con algoritmos más avanzados.
