print(max(w:=sorted(map(lambda e:sum(map(int,e.split())),open("i").read().split("\n\n")))[-3:]),sum(w))
