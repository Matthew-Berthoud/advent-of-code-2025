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

    if direction == "L":
        count *= -1

    dial = (dial + count) % 100
    print(f"    - The dial is rotated {line} to point at {dial}")

    if dial == 0:
        total += 1

print(f"The password is {total}")
