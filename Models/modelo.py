# Cargar el modelo entrenado
from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
#scaler
from sklearn.preprocessing import MinMaxScaler


model = load_model('Data/Processed/modelo_entrenado.h5')  # Cambia 'modelo_rnn.h5' al nombre de tu archivo de modelo

# Suponiendo que tienes nuevos datos en un DataFrame llamado df_test
# Asegúrate de que tus datos estén preparados de la misma manera que los datos de entrenamiento
df_test = pd.read_csv('Data/Processed/solargis_13-02-2023.csv', sep=',')
# scaler = MinMaxScaler()

# scaler.fit(df_test[['TEMP', 'flagR', 'GHI']])
# # Normalizar los datos de prueba (si es necesario)
# # Suponiendo que tienes un MinMaxScaler guardado en la variable scaler
# df_test[['TEMP', 'flagR', 'GHI']] = scaler.transform(df_test[['TEMP', 'flagR', 'GHI']])

# # Preparar los datos de entrada para la predicción
# X_test = df_test[['TEMP', 'flagR']].values
# X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))  # Agregar una dimensión adicional para el modelo RNN

# # Hacer predicciones
# predicciones = model.predict(X_test)

# # Las predicciones estarán en la escala original si has invertido el escalado
# # Si utilizaste MinMaxScaler, puedes invertir el escalado de esta manera
# predicciones = scaler.inverse_transform(predicciones)

# # Ahora tienes las predicciones para tus nuevos datos


## probar el modelo con df_test 
# Normalizar los datos
scaler = MinMaxScaler()
df_test[['TEMP', 'flagR']] = scaler.fit_transform(df_test[['TEMP', 'flagR']])

# Preparar los datos de entrada y salida
X_test = df_test[['TEMP', 'flagR']].values
y_test = df_test['GHI'].values  # Suponiendo que la columna de salida se llama "radiacion_solar"

# Hacer predicciones
predicciones = model.predict(X_test)

# Las predicciones estarán en la escala original si has invertido el escalado
# Si utilizaste MinMaxScaler, puedes invertir el escalado de esta manera
predicciones = scaler.inverse_transform(predicciones)

# Ahora tienes las predicciones para tus nuevos datos
print(predicciones)
print(y_test)

# # Calcular el error cuadrático medio
# mse = np.mean((predicciones - y_test)**2)
# print('Error cuadrático medio:', mse)
# # print('Error cuadrático medio:', mse)


