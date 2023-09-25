import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Charger les données pour 11414 et 11416

data_11414 = pd.read_excel(r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11414.xlsx', sheet_name="Distance_finale_4")
data_11416 = pd.read_excel(r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11416.xlsx', sheet_name="Distance_finale_4")

x_11414 = data_11414['Q']
y_11414 = data_11414['D']
z_11414 = data_11414['S']
dates_11414 = pd.to_datetime(data_11414['date'])

x_11416 = data_11416['Q']
y_11416 = data_11416['D']
z_11416 = data_11416['S']
dates_11416 = pd.to_datetime(data_11416['date'])

#  Définir les dates importantes et leurs légendes avec le format 'DD/MM/YYYY'
important_dates_11414 = [
    (pd.to_datetime('06/01/2023', format='%d/%m/%Y'), '06 jan 11414'),
    (pd.to_datetime('12/04/2023', format='%d/%m/%Y'), '12 avr 11414')
]

important_dates_11416 = [
    (pd.to_datetime('05/01/2023', format='%d/%m/%Y'), '05 jan 11416'),
    (pd.to_datetime('16/03/2023', format='%d/%m/%Y'), '16 mar 11416')
]

# Créer le graphique pour 11414 et y ajouter la courbe de 11416
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer la courbe pour 11414
ax.plot(x_11414, y_11414, z_11414, label='Trajectory 11414')

# Ajouter des points importants avec des légendes pour 11414
for date, label in important_dates_11414:
    mask = (dates_11414 == date)
    ax.scatter(x_11414[mask], y_11414[mask], z_11414[mask], s=50, label=label)

# Tracer la courbe pour 11416
ax.plot(x_11416, y_11416, z_11416, label='Trajectory 11416')

# Ajouter des points importants avec des légendes pour 11416
for date, label in important_dates_11416:
    mask = (dates_11416 == date)
    ax.scatter(x_11416[mask], y_11416[mask], z_11416[mask], s=50, label=label)

ax.set_xlabel('on quality')
ax.set_ylabel('on delay')
ax.set_zlabel('on stress')

# Définir les échelles des axes x, y et z entre 0 et 10
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

# Ajouter un point rouge "cible" en 0,0,0 
ax.scatter(0, 0, 0, c='red', s=50, label='cible')

ax.legend()

plt.show()
