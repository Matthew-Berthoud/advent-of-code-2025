def check_overlap(bounds1, bounds2):
    l1, h1 = bounds1
    l2, h2 = bounds2
    if l1 <= h2 and l2 <= h1:
        return True, (min(l1, l2), max(h1, h2))
    return False, ()


with open("input.txt", "r") as f:
    bounds = []
    while True:
        line = f.readline().strip()
        if line == "":
            break
        bounds.append(tuple([int(bound) for bound in line.split("-")]))

    # print(bounds)

    overlap = True
    new_bounds = ()
    while overlap:
        overlap = False
        for i, bound1 in enumerate(bounds):
            for j, bound2 in enumerate(bounds[i + 1 :]):
                overlap, new_bounds = check_overlap(bound1, bound2)
                if overlap:
                    bounds.remove(bound1)
                    bounds.remove(bound2)
                    break
            if overlap:
                break
        if overlap:
            bounds.append(new_bounds)

    # print(bounds)

    ingredients_to_test = [int(line.strip()) for line in f.readlines()]

    # print(ingredients_to_test)

total = 0
for low, high in bounds:
    for ingredient in ingredients_to_test:
        if low <= ingredient and ingredient <= high:
            total += 1

print(total)
