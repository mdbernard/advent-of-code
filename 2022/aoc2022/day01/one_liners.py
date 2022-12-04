print("Part 1:", max(w := sorted(map(lambda e:sum(map(int,e.split())),open("i").read().split("\n\n")))[-3:]))
print("Part 2:", sum(w))
