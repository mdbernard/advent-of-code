print("Part 1:", sum(map(lambda line: ord(list(set(line.strip()[:len(line)//2]) & set(line.strip()[len(line)//2:]))[0]) % 97 + 1 if ord(list(set(line.strip()[:len(line)//2]) & set(line.strip()[len(line)//2:]))[0]) >= 97 else ord(list(set(line.strip()[:len(line)//2]) & set(line.strip()[len(line)//2:]))[0]) % 65 + 27, open("input.txt").read().strip().split())))
print("Part 2:", sum(map(lambda elves: ord(list(set(elves[0]) & set(elves[1]) & set(elves[2]))[0]) % 97 + 1 if ord(list(set(elves[0]) & set(elves[1]) & set(elves[2]))[0]) >= 97 else ord(list(set(elves[0]) & set(elves[1]) & set(elves[2]))[0]) % 65 + 27, [open("input.txt").read().strip().split()[i:i+3] for i in range(0, len(open("input.txt").read().strip().split()), 3)])))
