#---------------------------------------------------------------
#Exercise 8.6 in Computational Physics by Mark Newman
#http://www-personal.umich.edu/~mejn/cp/chapters/int.pdf
#Use fourth-order Runge Kutta method to solve van der Pol
#oscillator
#---------------------------------------------------------------

omega = 1
xs = []
gammas = []
t0, tMax = 0., 20.
h = 0.005
x, gamma = 1, 0.

# define the two differential equations
def f(r, t, mu):
    xs = r[0]
    gammas = r[1]
    return np.array([gammas, ((-omega**2)*xs + (mu*(1 - xs**2)*gammas))], float)

# RK4 method
def Pendulum_RK4(mu):
    r = np.array([x, gamma], float)
    tpoints = np.arange(t0, tMax, h)
    xs = []
    gammas = []

    for t in tpoints:
      xs.append(r[0])
      gammas.append(r[1])
      
      k1 = h*f(r, t, mu)
      k2 = h*f(r+0.5*k1, t+0.5*h, mu)
      k3 = h*f(r+0.5*k2, t+0.5*h, mu)
      k4 = h*f(r+h, t+h, mu)
      r += (k1+2*k2+2*k3+k4)/6

    return tpoints, xs, gammas

t_RK4_1, xs_RK4_1, gammas_RK4_1 = Pendulum_RK4(1)
t_RK4_2, xs_RK4_2, gammas_RK4_2 = Pendulum_RK4(2)
t_RK4_4, xs_RK4_4, gammas_RK4_4 = Pendulum_RK4(4)

plt.xlabel('dx/dt')
plt.ylabel('position')
plt.title("van der Pol oscillator with RK4")
plt.plot(gammas_RK4_1, xs_RK4_1, label='\u03BC = 1')
plt.plot(gammas_RK4_2, xs_RK4_2, label='\u03BC = 2')
plt.plot(gammas_RK4_4, xs_RK4_4, label='\u03BC = 4')
plt.legend(loc='best')
plt.grid()
