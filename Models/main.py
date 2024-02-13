import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import save_model



# Cargar el DataFrame
# Supongamos que df es tu DataFrame
# Asegúrate de tener las columnas "TEMP" y "flagR" en tu DataFrame

# Leer el archivo csv 'solargis_01-01-2023.csv '
df = pd.read_csv('Data/Processed/solargis_15-03-2023.csv', sep=',')
# df = pd.read_csv('../../../Data/Processed/solargis_15-03-2023.csv', sep=',')
# print(df.head())


# Normalizar los datos
scaler = MinMaxScaler()
df[['TEMP', 'flagR']] = scaler.fit_transform(df[['TEMP', 'flagR']])

# Preparar los datos de entrada y salida
X = df[['TEMP', 'flagR']].values
y = df['GHI'].values  # Suponiendo que la columna de salida se llama "radiacion_solar"

# Dividir los datos en conjuntos de entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo
model = Sequential()

# Capa de SimpleRNN
model.add(SimpleRNN(units=64, input_shape=(X.shape[1], 1), return_sequences=True))
# Capa de dropout para regularización
model.add(Dropout(0.2))

# Otra capa de SimpleRNN
model.add(SimpleRNN(units=64, return_sequences=True))
# Capa de dropout para regularización
model.add(Dropout(0.2))

# Capa de salida
model.add(Dense(units=1))

# Compilación del modelo
model.compile(optimizer='adam', loss='mse')

# Resumen del modelo
model.summary()

# Entrenamiento del modelo
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_data=(X_val, y_val))


# Guardar el modelo en un archivo .h5
save_model(model, 'modelo_entrenado.h5')