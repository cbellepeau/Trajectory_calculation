import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Charger les données depuis le fichier Excel
# excel_file_path = r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11414.xlsx'
excel_file_path = r'C:\Users\Camélia\Documents\TFE\Livrables\TRAJ\Trajectory_11416.xlsx'

sheet_name = 'Distance_finale_2'
label = 'Performance trajectory'
data = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Create a figure for the 3D scatter plot
fig = go.Figure()

x, y, z = data['Q'], data['D'], data['S']
date = pd.to_datetime(data['date'])

scatter = go.Scatter3d(
    x=x, y=y, z=z,
    mode='lines+markers',
    marker=dict(size=5),
    line=dict(width=3),
    name=label
)

fig.add_trace(scatter)

# Define animation frames
frames = []

for i in range(1, len(data)):
    x_data = x[:i+1]
    y_data = y[:i+1]
    z_data = z[:i+1]
    
    line = go.Scatter3d(
        x=x_data, y=y_data, z=z_data,
        mode='lines',
        line=dict(width=3),
        name=label
    )
    
    timer_annotation = [
        dict(text=f'Trajectory for {date.iloc[i].strftime("%Y-%m-%d")}', showarrow=False,
             xref="paper", yref="paper", x=0.5, y=1.05),
        dict(text=f'Time: {date.iloc[i].strftime("%Y-%m-%d")}', showarrow=False,
             xref="paper", yref="paper", x=0.5, y=0.95)
    ]
    
    frames.append(go.Frame(data=[line], name=f'Trajectory for {date.iloc[i].strftime("%Y-%m-%d")}', layout=dict(annotations=timer_annotation)))

# Add frames to the figure
fig.frames = frames

# Define animation settings
animation_settings = dict(frame=dict(duration=200, redraw=True), fromcurrent=True)

# Update layout for animation
fig.update_layout(
    scene=dict(
        xaxis_title="on quality",
        yaxis_title="on delay",
        zaxis_title="on stress"
    ),
    updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, animation_settings])])]
)

# Show the animation
pio.show(fig)
