with open("input.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]

operators = lines.pop(-1)
totals = [int(value) for value in lines.pop(0)]

for line in lines:
    for i, operand in enumerate(line):
        if operators[i] == "+":
            totals[i] += int(operand)
        else:
            totals[i] *= int(operand)

print(sum(totals))
