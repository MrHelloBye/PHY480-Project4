import matplotlib.pyplot as plt
import numpy as np
import os
from math import sqrt
import ising
import glob

def avg(vector):
	avg = 0

	N = vector.size
	start = 300
	for i in range(start,N):
		avg += vector[i]
	avg /= (N-start)

	return avg

def std(vector):
	average = avg(vector)
	std = 0

	N = vector.size
	start = 300
	for i in range(start,N):
		std += vector[i]**2

	std /= (N-start)
	std -= average**2
	std = sqrt(std)

	return std

if False:
	for temperature in np.arange(1,4,0.01):
		ising.Ising(10,10,temperature)

temperatures = []
energy_avgs = []
energy_stds = []
for infile in sorted(glob.glob('data/energy/*.csv')):
    temperatures.append(float(infile[-8:-4]))
    energy = np.loadtxt(infile)
    energy_avgs.append(avg(energy))
    energy_stds.append(std(energy))

temperatures = []
moment_avgs = []
moment_stds = []
for infile in sorted(glob.glob('data/moment/*.csv')):
    temperatures.append(float(infile[-8:-4]))
    moment = np.loadtxt(infile)
    moment_avgs.append(abs(avg(moment)))
    moment_stds.append(std(moment))

plt.errorbar(temperatures,energy_avgs, energy_stds, elinewidth=0.1)
plt.ylabel("Energy")
plt.xlabel("Temperature")
plt.savefig("plots/Energy.pdf")
plt.clf()

plt.errorbar(temperatures,moment_avgs, moment_stds, elinewidth=0.1)
plt.ylabel("Moment")
plt.xlabel("Temperature")
plt.savefig("plots/Moment.pdf")

'''
plt.plot(energy)
plt.ylabel("Energy")
plt.xlabel("Metropolis Step")
plt.tight_layout()
plt.savefig("plots/energy.pdf")
plt.show()

plt.plot(moment)
plt.ylabel("Magnetic Dipole Moment")
plt.xlabel("Metropolis Step")
plt.tight_layout()
plt.savefig("plots/moment.pdf")
plt.show()
'''

'''
names = os.listdir("data/spins")
names.sort()
print(names)
i = 0
for filename in names:
	data = np.loadtxt("data/spins/"+filename,delimiter=',')
	plt.imshow(data)
	plt.savefig("plots/spins/"+filename+".pdf")
	i += 1
'''
