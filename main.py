import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement des données à partir d'un fichier CSV
data = pd.read_csv('sales_data.csv')

# Affichage des premières lignes du DataFrame
print(data.head())

# Statistiques descriptives
print(data.describe())

# Visualisation des ventes totales par mois
monthly_sales = data.groupby('Month')['Sales'].sum()
months = monthly_sales.index
sales = monthly_sales.values

plt.bar(months, sales)
plt.xlabel('Mois')
plt.ylabel('Ventes totales')
plt.title('Ventes mensuelles')
plt.show()
