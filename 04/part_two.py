with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

ROLL = "@"
EMPTY = "."
REMOVED_ROLL = "x"

Y_MAX = len(lines) - 1
X_MAX = len(lines[0]) - 1


def iterate():
    total = 0
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            print(c, end="")

            if c != ROLL:
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
                lines[y][x] = REMOVED_ROLL
                total += 1

        print()
    return total


print("Initial state:")
grand_total = 0
total = 1
while total > 0:
    total = iterate()
    if total > 0:
        print(f"\nRemove {total} rolls of paper:")
    grand_total += total

print(grand_total)
