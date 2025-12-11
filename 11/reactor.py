START = "you"
END = "out"

with open("input.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]


devices = {}
for line in lines:
    device = line.pop(0)[:-1]
    outputs = line
    devices[device] = outputs

count = 0


def get_outputs(start):
    global count
    outputs = devices[start]
    for out in outputs:
        print(f"From {start} to {out}")
        if out != END:
            outputs = get_outputs(out)
        else:
            print()
            count += 1
    return outputs


# outputs = devices[START]

get_outputs(START)

print(count)
