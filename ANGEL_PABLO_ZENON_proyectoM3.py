import random  #Primero importamos las librerias que vamos a utilizar
import matplotlib.pyplot as plt 

canicas = 3000 #Definimos el numero de canicas
niveles = 12   #Definimos el numero de niveles
resultados = []#Definimos una lista para almacenar la casilla en la que quedo cada canica

def calcular(can, niv):  #creamos una funcion que recibe los valores de canicas y los niveles
    """FUNCION PARA CALCULAR LA POSICION DE CADA
    CANICA ....."""
    for i in range(can + 1) :  #Creamos un ciclo para el rango de canicas + 1 
        canica = 0  #definimos una variable local
        for x in range(niv + 1) : #Iniciamos otro ciclo para el rango de niveles 
            valor_aleatorio = random.randint(0, 100)  #usamos la librearia random para generar un numero random entre en 1 y el 100 y lo amacenamos en una variable
            if valor_aleatorio > 50 : # Si el valor obtenido es mayor a 50 se suma 1 a la canica
                canica += 1 
            else:  #Si no se cumple esta condicion 
                continue  #usamos la sentecnia continue
        resultados.append(canica)  #El resultado de la canica sera guradado en una lista ya antes definida

def graficar(valoresAbsolutos) :  #Creamos una funcion para graficar que pide un valor absoluto
    plt.hist(valoresAbsolutos, color = "pink") #Usamos la funcion hist de la libreria matloplip.pyplot para graficar el valor en forma de histograma
    plt.title("Simulación de la Máquina de Galton") #Le ponemos el titulo
    plt.ylabel("Numero de canicas")  #Al el eje Y le ponemos de titulo Numero de canicas
    plt.xlabel("Numero de casilla")  #Al eje X le ponemos de titulo Numero de casilla 1 - 12
    plt.show() #Y finalmente usamos la funcion .show de la libreria plt para ver el histograma 
calcular(canicas, niveles)  #Finalmanete llamamos a la funcion calcular con los valores indicados
graficar(resultados)     #Y al igual llamanos a la funcion graficas para que haga el histograma