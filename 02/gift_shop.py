EXAMPLE = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
INPUT = "8284583-8497825,7171599589-7171806875,726-1031,109709-251143,1039-2064,650391-673817,674522-857785,53851-79525,8874170-8908147,4197684-4326484,22095-51217,92761-107689,23127451-23279882,4145708930-4145757240,375283-509798,585093-612147,7921-11457,899998-1044449,3-19,35-64,244-657,5514-7852,9292905274-9292965269,287261640-287314275,70-129,86249864-86269107,5441357-5687039,2493-5147,93835572-94041507,277109-336732,74668271-74836119,616692-643777,521461-548256,3131219357-3131417388"


def gift_shop(puzzle_input):
    total = 0
    for start, end in [id_range.split("-") for id_range in puzzle_input.split(",")]:
        for id_num in range(int(start), int(end) + 1):
            id = str(id_num)
            if len(id) % 2 != 0:
                continue

            mid = int(len(id) / 2)
            if id[0:mid] != id[mid:]:
                continue

            total += id_num

    return total


def part_two(puzzle_input):
    total = 0
    for start, end in [id_range.split("-") for id_range in puzzle_input.split(",")]:
        for id_num in range(int(start), int(end) + 1):
            id = str(id_num)

            id_success = False
            for length in range(1, len(id) // 2 + 1):
                if len(id) % length != 0:
                    continue

                segment_count = len(id) // length
                prev_segment = ""
                failed = False
                for i in range(segment_count):
                    segment = id[length * i : length * (i + 1)]
                    # if id == "1010" and length == 2:
                    #     print(segment)
                    if i != 0 and segment != prev_segment:
                        failed = True
                        break
                    prev_segment = segment

                if not failed:
                    id_success = True
                    break

            if id_success:
                total += id_num

    return total


if __name__ == "__main__":
    # total = gift_shop(INPUT)
    # print(f"Part 1: {total}")

    total = part_two(EXAMPLE)
    print(f"Part 2 Example: {total}")

    total = part_two(INPUT)
    print(f"Part 2 Answer: {total}")
