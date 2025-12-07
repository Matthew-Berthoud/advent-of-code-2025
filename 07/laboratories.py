SPLITTER = "^"

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

start_line = lines.pop(0)
beams = set([start_line.find("S")])

total = 0
for line in lines:
    to_split = set()
    for i in beams:
        if line[i] == SPLITTER:
            to_split.add(i)
            total += 1
    for i in to_split:
        beams.remove(i)
        beams.add(i - 1)
        beams.add(i + 1)

print(total)
