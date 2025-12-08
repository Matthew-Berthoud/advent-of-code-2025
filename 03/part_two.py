INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    banks = [bank.strip() for bank in f.readlines()]

total = 0
for bank in banks:
    prev_idx = -1
    number = ""
    for remaining in range(12, 0, -1):
        search_space = bank[prev_idx + 1 : len(bank) - remaining + 1]

        digit = max([int(char) for char in search_space])
        prev_idx = bank.find(str(digit), prev_idx + 1)
        number += str(digit)

    total += int(number)

print(total)
