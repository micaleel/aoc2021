with open("input.txt") as fp:
    s = [int(n) for n in fp.readlines()]

n_larger = 0
previous = None

for current in s:
    if previous and previous < current:
        n_larger += 1
    previous = current

print(n_larger)
