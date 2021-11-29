"""
programa para ver el funcionamiento de una red neuronal sencilla
para un modelo lineal
tiene la finalidad para entender que hacen las neuronas, su poder esta en la cantidad y el tipo de activacion
sientanse en confianza en agregar neuronas, cambiar el tipo de activacion, modificar las épocas
y el salto del optimizador para que vean que pasa
"""

# Librerias a ocupar, tensorflow; para redes neuronales, numpy; para arrays y matplotlib; para graficar.
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# Datos reales para entrenar la red neuronal
C=np.array  ([-40,  0, 15,   21,    38, 100, 45,     71,   119,  50],dtype=float)
F=np.array  ([-40, 32, 59, 69.8, 100.4, 212, 113, 159.8, 246.2, 122],dtype=float)

#crear la red neuronal, tiene una capa de entrada y una capa de salida (solo dos neuronas)
#un mayor numero de neuronas o capas oculta pueden mejorar el rendimiento
# tambien dentro del argumento de Sequential van  las funciones de activacion

capa=tf.keras.layers.Dense(units=1, input_shape=[1])
modelo=tf.keras.Sequential([capa])

#Modelo con dos capas ocultas una con 5 neuronas y la otra con 3
#la entrada es de un dato y la salida es igual 1 dato
#modelo de activacion es relu
"""
capOculta=tf.keras.layers.Dense(units=5, input_shape=[1])
capOculta1=tf.keras.layers.Dense(units=3,activation=tf.nn.relu)
capa=tf.keras.layers.Dense(units=1)
modelo=tf.keras.Sequential([capOculta, capOculta1,capa])
"""

#indica como va a ser el eprendizaje (descenso del gradiente) y la funcion de error
#un número muy grande puede hacer que nunca detecte el minimo local
#un número muy pequeño hace muy tardado encontrar el mínimo local
modelo.compile(
                optimizer=tf.keras.optimizers.Adam(0.1),
                loss="mean_squared_error"
              )


# empieza el entrenamiento e indica cuantas veces debe revisar los datos de entrada, en este caso los revisa 1000 vece
# aumentar el numero de epochs puede hacer que nuestra neurona aprenda mejor, pero será mas tardado
# pero solo se ba a ajustar a esos datos, si su funcion es dispersa, esto no les va a servir de mucho
#ya que se ajustará solo a los datos de entrada, es por eso la importancia de tener muchos, pero muchos datos
#un numero muy bajo no le dara tiempo de entrenar bien
entrenado=modelo.fit(C,F,epochs=1500)

#graficar el error

plt.xlabel("Épocas")
plt.ylabel("Perdida")
plt.plot(entrenado.history["loss"])
plt.show()

# prueba el modelo 
#ingrese un valor que se quiera predecir
resultado = modelo.predict([17])
print("El resultado es: ",resultado)

# muestra en pantalla los valores de peso y sesgo de la (o las) neurona(s)

print ("El sesgo y peso son: ",capa.get_weights())

# para este caso, la funcion para calcular grados Fahrenhei a partir de grados Celsius es F=(C*1.8)+32
#como se puede observar, el resiltado de la red neuronal fue muy cercano a los valores de la fórmula 

