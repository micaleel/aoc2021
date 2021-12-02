from collections import defaultdict

with open("input.txt") as fp:
    instructions = fp.readlines()

counter = defaultdict(int)

for instruction in instructions:
    direction, value = instruction.split()

    key = "horizontal" if direction in ("down", "up") else "depth"

    if direction in ("forward", "down"):
        counter[key] += int(value)
    elif direction in ("up",):
        counter[key] -= int(value)
    else:
        raise ValueError("Unrecognized direction: %s" % direction)

print(counter["horizontal"] * counter["depth"])
