import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar la tabla de Excel
df = pd.read_excel(r'C:\Datos_Python\Institucion.xlsx')
# Preprocesar los datos
df = df.dropna()  # Eliminar filas con datos faltantes
df['Género'] = df['Género'].map({'M': 0, 'F': 1})  # Conversión de género

# Dividir los datos en conjuntos de entrenamiento y prueba
X = df.drop('Nota', axis=1)  # Características
y = df['Nota']  # Variable objetivo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#converir los datod a float32
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
y_train = y_train.astype('float32')
y_test = y_test.astype('float32')

# Crear el modelo de red neuronal
modelo = Sequential()
modelo.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
modelo.add(Dense(32, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
modelo.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X_train, y_train, epochs=10, batch_size=128)

# Evaluar el modelo
loss, accuracy = modelo.evaluate(X_test, y_test)
print(f'Precisión: {accuracy:.2f}')