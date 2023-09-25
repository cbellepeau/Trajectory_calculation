import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Chemin vers le fichier xlsx
# excel_file_path = r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11414.xlsx'
excel_file_path = r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11416.xlsx'

# Noms des onglets contenant les données
sheet_names = [
    # 'Distance_finale', 
    'Distance_finale_2', 
#     'Distance_finale_3', 
    # 'Distance_finale_4', 
#     'Distance_finale_5'
]

figs = []
axes = []

# Labels personnalisés pour chaque subplot
subplot_labels = [
    # 'Performance trajectory',
    # 'Performance trajectory, positive=0',
    # 'Performance trajectory, 1/(v-c)²',
    'Performance trajectory 11416',
    # 'Performance trajectory, 1/(exp(v-c))²',
]

# Liste des dates importantes et leurs étiquettes
important_dates = [
    # ('06/01/2023', '06 jan'),
    # ('12/04/2023', '12 avr'),
    ('05/01/2023', '05 jan'),
    ('16/03/2023', '16 mars')
]

# Lire les données à partir des onglets spécifiques et créer les figures et axes correspondants
for idx, sheet_name in enumerate(sheet_names):
    data = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    x = data['Q']
    y = data['D']
    z = data['S']
    dates = pd.to_datetime(data['date'])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label=subplot_labels[idx])  # Utiliser le label personnalisé

    # Ajouter les dates importantes avec leurs étiquettes
    for date, label in important_dates:
        mask = (dates.dt.strftime('%d/%m/%Y') == date)
        ax.scatter(x[mask], y[mask], z[mask], s=50, label=label)

    # # Ajouter un point rouge "cible" en 0,0,0 
    # ax.scatter(0, 0, 0, c='red', s=50, label='cible') #je l'ai désactivé parce que ça nique l'échelle et on voit plus rien

    ax.set_xlabel('on quality')
    ax.set_ylabel('on delay')
    ax.set_zlabel('on stress')
    ax.legend() #loc='upper right', title='Legend'
    axes.append(ax)

plt.show()  # Afficher les graphiques