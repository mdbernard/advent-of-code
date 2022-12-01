print("Part 1:", max(weights := list(map(lambda elf: sum(map(int, elf.split("\n"))), open("input.txt").read().strip().split("\n\n")))), "\nPart 2:", sum(sorted(weights, reverse=True)[:3]))
