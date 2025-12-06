with open("input.txt") as f:
    lines = [line.strip("\n") for line in f.readlines()]

last_line = lines.pop(-1)
line_length = len(last_line)
operators = last_line.split()

columns = [""] * line_length

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        columns[j] += c

columns = [column.strip() for column in columns]

totals = 0
operands = []
i = 0
for j, val in enumerate(columns):
    if val == "":
        if operators[i] == "*":
            total = 1
            for x in operands:
                total *= x
        else:
            total = sum(operands)
        operands = []
        totals += total
        i += 1
    else:
        operands.append(int(val))
    if j == line_length - 1:
        if operators[i] == "*":
            total = 1
            for x in operands:
                total *= x
        else:
            total = sum(operands)
        operands = []
        totals += total
        i += 1

print(totals)
