#---------------------------------------------------------------
#Exercise 10.2 in Computational Physics by Mark Newman
#http://www-personal.umich.edu/~mejn/cp/chapters/int.pdf
#Plot particle decay chain over time
#---------------------------------------------------------------

nBi213 = 10000 #work up the decay chain
nDecayPb = 0
nDecayTl = 0
nDecayBi = 0

h = 1.0
p_Bi = 1 - 2**(-h/(46*60))
p_Pb = 1 - 2**(-h/(3.3*60))
p_Tl = 1 - 2**(-h/(2.2*60))
tmax = 20000

tpoints = np.arange(0, tmax, h)
Bi_points = []
Bi209_points = []
Decay_points_Tl = []
Decay_points_Pb = []
Decay_points_Bi = []

for t in tpoints:
  Bi_points.append(nBi213)
  Bi209_points.append(nDecayBi)
  Decay_points_Tl.append(nDecayTl)
  Decay_points_Pb.append(nDecayPb)
  Decay_points_Bi.append(nDecayBi)

  decay_to_Pb1 = 0
  decay_to_Tl1 = 0
  decay_to_Bi = 0
  decay_to_Pb2 = 0

  for j in range(nDecayPb):
    r = random()
    if r<p_Pb:
      decay_to_Bi += 1
  nDecayBi += decay_to_Bi
  nDecayPb -= decay_to_Bi

  for k in range(nDecayTl):
    r = random()
    if r<p_Tl:
      decay_to_Pb2 += 1
  nDecayPb += decay_to_Pb2
  nDecayTl -= decay_to_Pb2

  for i in range(nBi213):
    r = random()
    if r<p_Bi:
      if r <= 0.9791:
        decay_to_Pb1 += 1
      else:
        decay_to_Tl1 += 1

        
  nBi213 -= decay_to_Pb1 + decay_to_Tl1
  nDecayTl += decay_to_Tl1
  nDecayPb += decay_to_Pb1


plt.plot(tpoints, Bi_points, label="Bi-213")
plt.plot(tpoints, Bi209_points, label="Bi-209")
plt.plot(tpoints, Decay_points_Tl, label="Tl")
plt.plot(tpoints, Decay_points_Pb, label="Pb")
plt.legend()
plt.show()
