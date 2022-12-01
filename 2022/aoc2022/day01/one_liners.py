print("Part 1:", max([sum([int(weight) for weight in elf.split("\n")]) for elf in open("input.txt").read().strip().split("\n\n")]))
print("Part 2:", sum(list(sorted([sum([int(weight) for weight in elf.split("\n")]) for elf in open('input.txt').read().strip().split("\n\n")], reverse=True))[:3]))
