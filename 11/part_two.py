START = "svr"
END = "out"
REQUIRED_DEVICES = ("dac", "fft")

with open("input.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]


devices = {}
for line in lines:
    device = line.pop(0)[:-1]
    outputs = line
    devices[device] = outputs

count = 0


def get_outputs(start, dac=False, fft=False):
    global count
    outputs = devices[start]
    for out in outputs:
        if start == START:
            dac, fft = False, False
        # print(f"From {start} to {out}")

        if out == END:
            if dac and fft:
                count += 1
                print(count)
            # print()
            return outputs, dac, fft

        elif out == "dac":
            # print("dac")
            dac = True
        elif out == "fft":
            # print("fft")
            fft = True

        outputs, dac, fft = get_outputs(out, dac, fft)

    return outputs, dac, fft


# outputs = devices[START]

get_outputs(START)

print(count)
