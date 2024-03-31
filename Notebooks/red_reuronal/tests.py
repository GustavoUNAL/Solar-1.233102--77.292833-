import numpy as np

# Crear un tensor (array NumPy)
tensor = np.array([[0.70689474], [0.08783057], [0.41928377], [0.1457094], [0.17855711], [0.51348876], [0.99052128], [0.75325388], [0.5444733]])

# Almacenar el tensor en un archivo
# np.save('mi_tensor.npy', tensor)

# Cargar el tensor desde el archivo
tensor_cargado = np.load('tensor_SFV.npy')
print(tensor_cargado)
