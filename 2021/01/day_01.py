import numpy as np
data = np.loadtxt('input_1.txt')

# part 1
print(np.sum(data[1:] > data[:-1]))

# part 2
windows = np.array([np.sum(data[i-2:i+1]) for i in range(2, len(data))])
print(np.sum(windows[1:] > windows[:-1]))
