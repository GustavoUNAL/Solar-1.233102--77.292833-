import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('DB/solargis.csv', sep=';')

# Crear un dataframe con los datos
df = pd.DataFrame(data)

date = df['Date']
ghi = df['GHI']

#graficar los datos de GHI en un diagrama de barras
# plt.bar(date, ghi)
# plt.xlabel('Date')
# plt.ylabel('GHI')
# plt.title('GHI vs Date')
# plt.show()

# Buscar en la columna "Date" las filas con el valor "01.01.2023"
selected_rows = data.loc[data['Date'] == '01.01.2023']

# Crear un dataframe con los datos
df2 = pd.DataFrame(selected_rows)
# print(df2)
print(df2['Time'])
print(df2['GHI'])

#graficar los datos de GHI en un diagrama de barras
# plt.bar(df2['Time'], df2['GHI'])
# plt.xlabel('Time')
# plt.ylabel('GHI')
# plt.title('GHI vs Time (01.01.2023)')
# plt.show()


# Grafico en una misma figura
# plt.figure(figsize=(10,5))

# # Gráfico de GHI vs Time
# plt.plot(df2['Time'], df2['GHI'], label='GHI')

# # Gráfico de DNI vs Time en el mismo plot
# plt.plot(df2['Time'], df2['DNI'], label='DNI')

# # Agregar una leyenda
# plt.legend()
# plt.xticks([20,40,80,120,140])
# plt.show()