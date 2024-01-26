import pandas as pd
import json

# Abrir el archivo JSON y cargar los datos
with open('DataLake/NASA/POWER_Point_Daily_20230101_20240101_001d23N_077d29W_LST.json', 'r') as f:
    data = json.load(f)
    print(data["properties"])