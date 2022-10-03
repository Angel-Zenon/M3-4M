# M3-4M
Proyecto

Primero importe las librerías random (esta genera números aleatorios) y la librería matplotlib. pyplot (esta nos permite graficar datos)
Posteriormente definí las variables: canicas, niveles, y una lista de resultados para almacenar los resultados de cada canica
Luego creé una función que pide como parámetros canicas y niveles para calcular la casilla o la posición de cada canica, utilizando un ciclo for para cada elemento del rango de (canicas + 1), después definí una variable local para almacenar la posición de cada canica = 0. Después utilice otro for para el rango de los (niveles + 1) , como siguiente paso use la librería random con .randint(1, 100) para generar un numero aleatorio entre el 1 y el 100. Use los condicionales if para que cuando el numero random generado sea mayor a 50 le sume 1 a canica que es la variable local que antes definí y si no se cumple use la sentencia continue para continuar con el ciclo. Y el valor de cada canica lo amacena en la lista resultados
Después creé otra función para graficar que pide como parámetros los valoresAbsolutos o la lista de valores, lo que hace esta función es usar la librería matplotlib.pllt con la función .hits para hacer un histograma con los valores y agrege un color rosado
Y para finalizar llame a las dos funciones con sus respectivos valores


REFLEXIONES DEL BOOTCAMP 
Hasta ahora el bootcamp me ha gustado bastante ya que nos han enseñado cosas muy utilies en este modulo, entre ellas creear nuestras propias funciones las cuales nos pueden ahorra mucho tiempo , al igual como llevarlas a la practica en la vida real. Tambien me gusto que nos hayan enseñadoo a usar las librerias de numpy, random y mathplot que son de suma importancia en los analisis de datos.
