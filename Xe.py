from matplotlib.ticker import MultipleLocator
import numpy as np; import matplotlib.pyplot as plt

Xe = [ (419.35,  80), (450.10, 150), (462.43, 500), (467.12, 600),
	   (469.19, 200), (473.42, 350), (480.70, 250), (482.97, 180), 
	   (491.65, 120), (492.32, 150), (529.22,  80), (541.90,  60), 
	   (582.49,  70), (618.24,  90), (631.81, 110), (688.22, 400)]

Λ = np.linspace(400, 800, 2000)
plt.xlim((400, 800)); plt.ylim((0,max([t[1] for t in Xe])+10))

for λ,I in Xe:
	if   λ < 440: c = '#8A2BE2'
	elif λ < 490: c = '#0000FF'
	elif λ < 500: c = '#00FFFF'
	elif λ < 570: c = '#00FF00'
	elif λ < 590: c = '#FFFF00'
	elif λ < 620: c = '#FF8C00'
	else:         c = '#FF0000'
	plt.vlines(x=λ, ymin=0, ymax=I, colors=c, lw=2)

plt.title("Spectre d'émission visible du Xénon", weight='bold')

plt.xlabel("Longueur d'onde (nm)")
plt.ylabel("Intensité Relative (NIST)")

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_minor_locator(MultipleLocator(50))
ax.tick_params(axis='x', which='major', length=6, width=1)
ax.tick_params(axis='x', which='minor', length=4, width=0.8)
ax.tick_params(axis='y', left=False, labelleft=False)

plt.show()
