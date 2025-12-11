from itertools import chain, combinations


def configure(target, buttons):
    bit = target[0]

    chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    return 0


def process(line):
    line.pop()  # don't need this for now
    target = [(bit == "#") for bit in list(line.pop(0)[1:-1])]
    values = [
        [(i in [int(n) for n in group[1:-1].split(",")]) for i in range(len(target))]
        for group in line
    ]
    print(
        f"target: {''.join(['1' if bit else '0' for bit in target])}, values: {[''.join(['1' if bit else '0' for bit in v]) for v in values]}"
    )

    return target, values


with open("example.txt") as f:
    total = 0
    for line in [line.strip().split() for line in f.readlines()]:
        target, values = process(line)
        total += configure(target, values)

print(total)
