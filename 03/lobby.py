INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
    banks = [bank.strip() for bank in f.readlines()]

total = 0
for bank in banks:
    tens_digit = max([int(char) for char in bank[:-1]])
    tens_digit_idx = bank.find(str(tens_digit))
    ones_digit = max([int(char) for char in bank[tens_digit_idx + 1 :]])
    total += int(f"{tens_digit}{ones_digit}")

print(total)
