with open("input.txt") as fp:
    s = [int(n) for n in fp.readlines()]

window = 3
n_larger = 0
previous = None

for i in range(window, len(s) + 1):
    current = sum(s[i - window : i])
    if previous and previous < current:
        n_larger += 1
    previous = current

print(n_larger)
