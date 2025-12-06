with open("./input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# lines = [
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82",
# ]
# print(lines)

total = 0
dial = 50

for line in lines:
    assert line[0] in "RL"
    assert line[1:].isnumeric()

    direction = line[0]
    count = int(line[1:])

    while count > 0:
        if direction == "L":
            dial -= 1
        else:
            dial += 1

        if dial == 0 or dial == 100:
            dial = 0
            total += 1
        elif dial == -1:
            dial = 99

        count -= 1
    print(f"    - The dial is rotated {line} to point at {dial}")
print(f"The password is {total}")
