import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('mremh_presupuestoejecutadomisionesecuadorexterior_2024marzo.csv')

# Crear la imagen
plt.figure(figsize=(10, 6))
plt.plot(df['Mes'], df['Presupuesto Ejecutado'], label='Presupuesto Ejecutado')
plt.xlabel('Mes')
plt.ylabel('Presupuesto Ejecutado')
plt.title('Presupuesto Ejecutado por Mes')
plt.legend()
plt.show()
