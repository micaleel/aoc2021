from collections import defaultdict

with open("input.txt") as fp:
    instructions = fp.readlines()

counter = defaultdict(int)
aim = 0

for instruction in instructions:
    direction, value = instruction.split()
    value = int(value)

    if direction == "down":
        aim += value
    elif direction == "up":
        aim -= value
    elif direction == "forward":
        counter["horizontal"] += value
        counter["depth"] += aim * value
    else:
        raise ValueError("Unrecognized direction: %s" % direction)

print(counter["horizontal"] * counter["depth"])
