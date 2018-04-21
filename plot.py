import matplotlib.pyplot as plt
import numpy as np
import os

'''
energy = np.loadtxt("energy.csv")
moment = np.loadtxt("moment.csv")

plt.plot(energy)
plt.savefig("plots/energy.pdf")
plt.show()

plt.plot(moment)
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
	plt.savefig("plots/spins2/"+filename+".pdf")
	i += 1
