from numba import jit
import numpy as np
import math
import random
import os
import matplotlib.pyplot as plt

height = 2
width = 2

modulus = int(math.ceil(height*width/10.))
steps = 10*modulus
print(modulus)

beta = 1
J = 1
mu = 1
#E = 0
#M = 0
#meanE = 0
#meanM = 0
#spec_heat = 0
#suscept = 0

@jit
def UpdateBoundaries(spins):
	for i in range(height+2):
		spins[i,-1] = spins[i,1]
		spins[i,0] = spins[i,-2]
	for j in range(width+2):
		spins[-1,j] = spins[1,j]
		spins[0,j] = spins[-2,j]

def Energy(spins):
	Energy = 0

	UpdateBoundaries(spins)

	for i in range(1,height+1):
		for j in range(1,width+1):
			Energy += -J*spins[i,j]*spins[i+1,j]
			Energy += -J*spins[i,j]*spins[i,j+1]

	return Energy

def Moment(spins):
    mag_mom = 0
    for i in range(1, height+1):
        for j in range(1, width+1):
            mag_mom += spins[i,j]
            #print('i: ',i, 'j: ',j, 'spin: ',spins[i,j])
    return mag_mom

spins = np.ones((height+2, width+2),dtype='int')
for i in range(1, height+1):
	for j in range(1, width+1):
		spins[i,j] = random.choice([-1,1])



os.system("mkdir data")
os.system("mkdir data/spins")
energy_file = open("data/energy.csv", "w")
moment_file = open("data/moment.csv", "w")

energy = Energy(spins)
moment = Moment(spins)

energy_file.write(str(energy)+"\n")
moment_file.write(str(moment)+"\n")

e4 = np.exp(-4*J*beta)
e8 = np.exp(-8*J*beta)

@jit
def Calc_dE(spins,i,j):
	return -2*(-J*spins[i,j])*(spins[i-1,j]+spins[i+1,j]+spins[i,j-1]+spins[i,j+1])

@jit
def Accept(dE):
	accept = False
	if dE <= 0:
		accept = True
	elif dE == 4:
		if random.uniform(0,1) <= e4:
			accept = True
	elif dE == 8:
		if random.uniform(0,1) <= e8:
			accept = True
	else:
		print("ya done goofed")
	return accept

print('Moment: ',Moment(spins))

for k in range(steps):
    i = random.randint(1,height)
    j = random.randint(1,width)
    
    UpdateBoundaries(spins)
    
    dE = Calc_dE(spins,i,j)
    
    if Accept(dE):
        #print("spin1: ",spins[i,j],'i: ',i,'j: ',j)
        spins[i,j] *= -1
        #print("spin2: ",spins[i,j])
        moment += 2*spins[i,j]
        energy += dE

    print('k: ',k, "energy: ", energy)

    if not (k%modulus):
        energy_file.write(str(energy)+"\n")
        moment_file.write(str(moment)+"\n")
        np.savetxt("data/spins/spins"+str(k)+".csv",spins,delimiter=',')

print("Incremented Energy: ",energy,"Energy: ",Energy(spins))
print("Incremented Moment: ", moment, "Moment: ", Moment(spins))
UpdateBoundaries(spins)
plt.imshow(spins)
plt.show()

energy_file.close()
moment_file.close()
