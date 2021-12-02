with open('input_1.txt', 'r') as infile:
    lines = [line.strip().split(' ') for line in infile]
lines = [(line[0], int(line[1])) for line in lines]

# part 1
x = sum([(line[0] == 'forward')*line[1] for line in lines])
y = sum([(line[0] == 'down')*line[1] - (line[0] == 'up')*line[1] for line in lines])
print(x*y)

# part 2
x = d = aim = 0
for line in lines:
    aim += (line[0] == 'down')*line[1] - (line[0] == 'up')*line[1]
    x += (line[0] == 'forward')*line[1]
    d += aim*(line[0] == 'forward')*line[1]
print(x*d)
