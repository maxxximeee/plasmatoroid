import numpy as np; import matplotlib.pyplot as plt

fig = plt.figure(); ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1]); ax.axis('off'); ax.view_init(elev=33, azim=91)
##### Tore
R = 3.0; r = 1.0

Θ, Φ = np.meshgrid(np.linspace(0, 2*np.pi, 100), np.linspace(0, 2*np.pi, 60))
X = (R + r*np.cos(Φ)) * np.cos(Θ)
Y = (R + r*np.cos(Φ)) * np.sin(Θ)
Z = r * np.sin(Φ)

tore = ax.plot_surface(X, Y, Z, color="#A143D4", alpha=0.2, rstride=4, cstride=4, 
					   edgecolors='w', linewidth=0.1, antialiased=True)

##### Champ électrique azimutal
θ = np.linspace(0, 2*np.pi, 200); r_E = 0.0

X_E = (R + r_E) * np.cos(θ)
Y_E = (R + r_E) * np.sin(θ)
Z_E = np.zeros_like(θ)

ax.plot(X_E, Y_E, Z_E, color="#220034", linewidth=2.5)
ax.quiver(X_E[50], Y_E[50], Z_E[50], -Y_E[50], X_E[50], 0, length=0.5, color="#220034", pivot='middle')

##### Champ magnétique poloïdal
N = 16; t = np.linspace(0, 2*np.pi, 1000)
X_B = (R + r * 1.02 * np.cos(N*t)) * np.cos(t)
Y_B = (R + r * 1.02 * np.cos(N*t)) * np.sin(t)
Z_B = r * 1.02 * np.sin(N*t)

ax.plot(X_B, Y_B, Z_B, color="#C390DE", linewidth=2)
ax.quiver(X_B[100], Y_B[100], Z_B[100], -Y_B[100], X_B[100], Z_B[101]-Z_B[100], 
		  length=0.4, color="#C390DE", pivot='middle')

M = R + r
ax.set_xlim(-M, M); ax.set_ylim(-M, M); ax.set_zlim(-M, M)

plt.show()
