import numpy as np
data = np.loadtxt('input_1.txt')

# part 1
print(np.sum(data[1:] > data[:-1]))

# part 2
print(np.sum(data[3:] > data[:-3]))
