from threading import ExceptHookArgs


def main():
    data = read_input("day2_input")
    count, total = part_1(data)
    print(total)


def read_input(file_name):
    read_data = None
    with open(file_name, "r") as f:
        read_data = f.read()
    if read_data:
        read_data = read_data.removesuffix("\n")
        read_data = read_data.split(",")
    return read_data


def identify_invalid_id(id):
    # pass in string.
    # anything with an uneven length is valid
    if len(id) % 2 != 0:
        return False
    mid = int((len(id) // 2))
    # print(mid)
    left = id[:mid]
    right = id[mid:]
    if left == right:
        return True
    else:
        return False


def identify_range(range):
    # range is the string
    split_range = range.split("-")
    if len(split_range) == 2:
        first_id = int(split_range[0])
        last_id = int(split_range[1])
        return first_id, last_id
    else:
        raise Exception(f"Fuck this shit {split_range}, {range}")


def loop_over_range(id_range):
    count = 0
    id_sum = 0
    first_id, second_id = identify_range(id_range)
    for i in range(first_id, second_id + 1):
        outcome = identify_invalid_id(str(i))
        if outcome:
            count += 1
            id_sum += i
    return count, id_sum


def part_1(data):
    count = 0
    total = 0
    for id_range in data:
        print(f"id_range from data: {id_range}")
        c, sum = loop_over_range(id_range)
        count += c
        total += sum
    return count, total


if __name__ == "__main__":
    main()
