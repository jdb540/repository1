import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
animales = pd.read_csv("animales.csv")

plot(animales, "edad", "peso", "color", "edad", "Peso de los animales por edad", "Edad (años)", "Peso (kg)")
