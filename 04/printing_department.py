with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

ROLL = "@"

Y_MAX = len(lines) - 1
X_MAX = len(lines[0]) - 1

total = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ROLL:
            print(".", end="")
            continue

        rolls = 0

        # Corners
        if x > 0 and y > 0 and lines[y - 1][x - 1] == ROLL:
            rolls += 1
        if x > 0 and y < Y_MAX and lines[y + 1][x - 1] == ROLL:
            rolls += 1
        if x < X_MAX and y < Y_MAX and lines[y + 1][x + 1] == ROLL:
            rolls += 1
        if x < X_MAX and y > 0 and lines[y - 1][x + 1] == ROLL:
            rolls += 1

        # North, South, West, East
        if y > 0 and lines[y - 1][x] == ROLL:
            rolls += 1
        if y < Y_MAX and lines[y + 1][x] == ROLL:
            rolls += 1
        if x > 0 and lines[y][x - 1] == ROLL:
            rolls += 1
        if x < X_MAX and lines[y][x + 1] == ROLL:
            rolls += 1

        if rolls < 4:
            print("x", end="")
            total += 1
        else:
            print("@", end="")
    print()

print(total)
