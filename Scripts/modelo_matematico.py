# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Cargar los datos del archivo CSV Data/Cleaned/SFV_2023.csv
df_SFV = pd.read_csv('./Data/Cleaned/SFV_2023.csv', sep=',')
# Cargar los datos del archivo CSV
df_solcast = pd.read_csv('./Data/Cleaned/solcast_2023.csv', sep=',')
# filtrar un dia de datos 
Fecha = '2023-01-07'
row_day_solcast = df_solcast.loc[df_solcast['Date'] == Fecha]
row_day_fronius = df_SFV.loc[df_SFV['Date'] == Fecha]

# reiniciar el index
row_day_solcast = row_day_solcast.reset_index(drop=True)
row_day_fronius = row_day_fronius.reset_index(drop=True)
# Odenernar row_day_solcast de menor a mayor hora
row_day_solcast = row_day_solcast.sort_values(by='Time')
row_day_solcast = row_day_solcast.reset_index(drop=True)
# Crear un nuevo dataframe con los datos de solcast y fronius a partir del indice 
df = pd.DataFrame()
df['Time'] = row_day_solcast['Time']
df['GHI'] = row_day_solcast['GHI']
df['air_temp'] = row_day_solcast['air_temp']
df['cloud_opacity'] = row_day_solcast['cloud_opacity']
df['Producción_fotovoltaica_SFV'] = row_day_fronius['Producción_fotovoltaica_SFV']


## Modelo matemático
# alpha y beta 
alpha = 0.1
beta = 0.5


#Parametros SFV
efficiency = 0.2094  # Eficiencia del panel solar
catidad_pv= 30
area =2.274*1.134

# normalizar 'cloud_opacity' de 0 a 1  en donde 1 es el valor más alto
df['cloud_opacity'] = df['cloud_opacity'] / df['cloud_opacity'].max()
# normalizar 'air_temp' de 0 a 1  en donde 1 es el valor más alto
df['air_temp'] = df['air_temp'] / df['air_temp'].max()

# Energía calculada a partir de Solcast 
df['P_cloud_opacity_temp'] = df['GHI'] * efficiency *  area * catidad_pv * (1 - beta*df['cloud_opacity']) * (1 - alpha*df['air_temp'])
# suma de la potencia generada solcast
energia = df['P_cloud_opacity_temp']*(5/60)
print("Energía calculada solacast [kWh] =",energia.sum()/1000)

# Energía calculada a partir de Fronius
df['Potencia'] = df['Producción_fotovoltaica_SFV'] / (5/60)
energia_fronius = df['Producción_fotovoltaica_SFV'].sum()
print("Producción fotovoltaica SVF [kWh/día] =",energia_fronius/1000)

# error porcentual
error = abs(  energia.sum() - energia_fronius.sum()) / energia_fronius.sum() * 100
print('Error porcentual:', error, '%')

# Horas de brillo solar
hbs = energia_fronius / (30*0.54)
print("Horas de brillo solar =", hbs/1000)