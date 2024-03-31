import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()