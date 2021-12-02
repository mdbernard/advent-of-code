# part 1
data = {'forward': 0, 'up': 0, 'down': 0}
with open('input_1.txt', 'r') as infile:
    for line in infile:
        line = line.strip().split(' ')
        data[line[0]] += int(line[1])

x = data['forward']
y = data['down'] - data['up']
print(x*y)

# part 2
x = d = aim = 0
with open('input_1.txt', 'r') as infile:
    for line in infile:
        line = line.strip().split(' ')
        line[1] = int(line[1])
        aim += (line[0] == 'down')*line[1] - (line[0] == 'up')*line[1]
        x += (line[0] == 'forward')*line[1]
        d += aim*(line[0] == 'forward')*line[1]
print(x*d)
