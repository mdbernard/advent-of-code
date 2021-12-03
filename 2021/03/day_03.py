import numpy as np
from scipy.stats import mode


with open('input_1.txt', 'r') as infile:
    data = np.array([[int(char) for char in line.strip()] for line in infile])

# part 1
gamma_bits = np.array([mode(data[:,i])[0][0] for i in range(data.shape[1])])
eps_bits = -1*(gamma_bits - 1)
gamma = sum([2**i*b for (i, b) in enumerate(gamma_bits[::-1])])
epsilon = sum([2**i*b for (i, b) in enumerate(eps_bits[::-1])])
print(gamma*epsilon)

# part 2
