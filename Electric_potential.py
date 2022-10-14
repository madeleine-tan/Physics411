#--------------------------------------------------------------------
#Exercise 5.21 in Computational Physics by Mark Newman
#Part 1: Plots the electric potential in the xy plane two charges
#Part 2: Makes quiver plot of the electric field in the xy plane
#--------------------------------------------------------------------

#Part 1 -------------------------------------------------------------
def electric_potential(q, x1, y1, x2, y2):
  return q/(4*np.pi*(8.854e-12)*(np.sqrt((x1-x2)**2 + (y1-y2)**2)))

xs = np.linspace(-0.5, 0.5, 100)
ys = np.linspace(-0.5, 0.5, 100)
vals = np.zeros((100, 100))
p1_x = -0.05 #Charge 1 x-loc
p2_x = 0.05 #Charge 2 x-loc
p1_y = 0 #Charge 1 y-loc
p2_y = 0 #Charge 2 y-loc

for i, x in enumerate(xs):
  for j, y in enumerate(ys):
    vals[j,i] = electric_potential(1, x, y, p1_x, p1_y) + electric_potential(-1, x, y, p2_x, p2_y)

z_min, z_max = -np.abs(vals).max(), np.abs(vals).max()
plt.pcolormesh(vals, cmap="flag")
plt.show()

#Part 2 -------------------------------------------------------------
y, x = np.mgrid[0.5:-0.5:100j, 0.5:-0.5:100j]
dy, dx = np.gradient(electric_potential(1, x, y, p1_x, p1_y)
                    + electric_potential(-1, x, y, p2_x, p2_y)) #gradient using axis as partials

fig, ax = plt.subplots()
ax.quiver(x, y, dx, dy, electric_potential(1, x, y, p1_x, p1_y)
                        + electric_potential(-1, x, y, p2_x, p2_y))
plt.title("Quiver Plot")
plt.show()
