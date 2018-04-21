from numba import jit
import numpy as np
import math
import random

height = 500
width = 500

modulus = int(math.floor(height*width/10.))
steps = 1000*modulus
print(modulus)

beta = 10
J = 1
mu = 1

@jit
def UpdateBoundaries(spins):
	for i in range(height):
		spins[i,-1] = spins[i,1]
		spins[i,0] = spins[i,-2]
	for j in range(width):
		spins[-1,j] = spins[1,j]
		spins[0,j] = spins[-2,j]

def Energy(spins):
	Energy = 0

	UpdateBoundaries(spins)

	for i in range(height):
		for j in range(width):
			Energy += spins[i,j]*spins[i+1,j]
			Energy += spins[i,j]*spins[i,j+1]

	return Energy

def Moment(spins):
	mag_mom = 0
	for i in range(height):
		for j in range(width):
			mag_mom += spins[i,j]
	return mag_mom

spins = np.ones((height+2, width+2),dtype='int')
for i in range(height):
	for j in range(width):
		spins[i,j] = random.choice([-1,1])


energy_file = open("data/energy.csv", "w")
moment_file = open("data/moment.csv", "w")

energy = Energy(spins)
moment = Moment(spins)

e4 = np.exp(-4*J*beta)
e8 = np.exp(-8*J*beta)

@jit
def Calc_dE(spins,i,j):
	return -2*spins[i,j]*(spins[i-1,j]+spins[i+1,j]+spins[i,j-1]+spins[i,j+1])

@jit
def Accept(dE):
	accept = False
	if dE >= 0:
		accept = True
	elif dE == -4:
		if random.uniform(0,1) <= e4:
			accept = True
	elif dE == -8:
		if random.uniform(0,1) <= e8:
			accept = True
	else:
		print("ya done goofed")
	return accept

for k in range(steps):
	i = random.randint(0,height-1)
	j = random.randint(0,width-1)

	UpdateBoundaries(spins)
	
	dE = Calc_dE(spins,i,j)

	if Accept(dE):
		spins[i,j] *= -1
		moment += spins[i,j]
		energy += dE

	print('k: ',k, "energy: ", energy)

	if not (k%modulus):
		energy_file.write(str(energy)+"\n")
		moment_file.write(str(moment)+"\n")
		np.savetxt("data/spins/spins"+str(k)+".csv",spins,delimiter=',')


energy_file.close()
moment_file.close()