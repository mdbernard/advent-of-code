print("Part 1:", max(map(lambda elf: sum(map(int, elf.split("\n"))), open("input.txt").read().strip().split("\n\n"))))
print("Part 2:", sum(sorted(map(lambda elf: sum(map(int, elf.split("\n"))), open("input.txt").read().strip().split("\n\n")), reverse=True)[:3]))
