import os
import numpy as np


infile_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'input_1.txt')
with open(infile_path, 'r') as infile:
    data = np.array([int(line) for line in infile])

# part 1
diffs = data[1:] - data[:-1]
signs = np.sign(diffs)
print(np.sum(signs > 0))

# part 2
windows = np.array([np.sum(data[i-2:i+1]) for i in range(2, len(data))])
diffs2 = windows[1:] - windows[:-1]
signs2 = np.sign(diffs2)
print(np.sum(signs2 > 0))
