import matplotlib.pyplot as plt
import numpy as np
import os


energy = np.loadtxt("data/energy.csv")
moment = np.loadtxt("data/moment.csv")

plt.plot(np.arange(0,1000,1)*25000,energy)
plt.ylabel("Energy")
plt.xlabel("Metropolis Step")
plt.tight_layout()
plt.savefig("plots/energy.pdf")
plt.show()

plt.plot(np.arange(0,1000,1)*25000,moment)
plt.ylabel("Magnetic Dipole Moment")
plt.xlabel("Metropolis Step")
plt.tight_layout()
plt.savefig("plots/moment.pdf")
plt.show()

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
