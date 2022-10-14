#---------------------------------------------------------------
#Exercise 5.22 in Computational Physics by Mark Newman
#http://www-personal.umich.edu/~mejn/cp/chapters/int.pdf
#Calculate the first 20 derivatives of function f(zk)
#Compare to the factorial
#---------------------------------------------------------------

def f(z):
  return np.exp(2*z)

N = 10000
ms = np.linspace(1, 20, 20)

for m in ms:
  val = 0
  coeff = np.math.factorial(m)/N
  for k in range(0, N):
      sum = f(cmath.exp((1j*2*np.pi*k)/10000))*cmath.exp((-1j*2*np.pi*k*m)/10000) #function f(zk)
      val += sum
  print(val*coeff)
  print(2**m)
  print('\n')
