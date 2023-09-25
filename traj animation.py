import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Charger les données depuis le fichier Excel, penser à décommenter le chemin du fichier qui m'intéresse
# excel_file_path = r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11414.xlsx'
excel_file_path = r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11416.xlsx'

sheet_names = [
    # 'Distance_finale', 
    # 'Distance_finale_2', 
#     'Distance_finale_3', 
    'Distance_finale_4'
]
labels = [
    'Performance trajectory', 
    # 'Performance trajectory, positive=0', 
    # 'Performance trajectory, 1/(v-c)²', 
    # 'Performance trajectory, calcul d1, d2, d3'
]
datasets = [pd.read_excel(excel_file_path, sheet_name=sheet) for sheet in sheet_names]

# Définir les noms de colonnes pour chaque KPI
columns = ['Q', 'D', 'S']

# Définir les figures et axes pour chaque plot
figs = [plt.figure() for _ in range(len(sheet_names))]
axes = [fig.add_subplot(111, projection='3d') for fig in figs]

# Fonction pour l'animation
def animate(i):
    if i == 0:
        return
    for j, ax in enumerate(axes):
        data = datasets[j]
        x, y, z = data[columns[0]], data[columns[1]], data[columns[2]]
        date = pd.to_datetime(data['date'])
        
        ax.clear()
        # # Fixer les limites minimales des axes à 0
        # ax.set_xlim(left=0)
        # ax.set_ylim(bottom=0)
        # ax.set_zlim(bottom=0)
        # Fixer les limites maximales en fonction des données
        # ax.set_xlim(0, x.max())  # Remplacez x.max() par la valeur maximale appropriée
        # ax.set_ylim(0, y.max())  # Remplacez y.max() par la valeur maximale appropriée
        # ax.set_zlim(0, z.max())  # Remplacez z.max() par la valeur maximale appropriée
        ax.plot(x[:i], y[:i], z[:i], label=labels[j])
        ax.scatter(x[i-1:i], y[i-1:i], z[i-1:i], c='red', s=50)
        ax.set_xlabel('on quality')
        ax.set_ylabel('on delay')
        ax.set_zlabel('on stress')
        ax.set_title(f'Trajectory for {date[i-1]:%Y-%m-%d}')
        ax.legend()


# Lancer les animations
animations = [animation.FuncAnimation(fig, animate, frames=len(data), interval=200, blit=False) for fig, data in zip(figs, datasets)]

plt.show()
