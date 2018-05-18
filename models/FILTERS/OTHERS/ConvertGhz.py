import numpy as np


array = np.loadtxt('laboca_passband_normalized.txt')

for i in range(len(array)):
    array[i][0] *= 1e9
    array[i][0] = 2.998e18/array[i][0] # Unit Angstrom



np.savetxt('laboca_new.dat', array)
