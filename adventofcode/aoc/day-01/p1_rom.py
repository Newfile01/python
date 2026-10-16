def loop_over_input(tuple_list: list[tuple]) -> int:
    count = 0
    position = 50
    for tup in tuple_list:
        position = move_dial(position, tup)
        if position == 0:
            count += 1
    return count


def move_dial(start_position: int, move_tuple: tuple) -> int:
    if move_tuple[0] == 'L':
        return (start_position - move_tuple[1]) % 100
    elif move_tuple[0] == 'R':
        return (start_position + move_tuple[1]) % 100
    else:
        return -1


def get_input_list(path: str) -> list[tuple]:
    with open(path, 'r') as file:
        lines = file.readlines()
    tuple_list: list[tuple] = []
    for line in lines:
       tuple_list.append((line[0], int(line[1:])))
    return tuple_list


def main():
    print(loop_over_input(get_input_list('input_p1.txt')))


if __name__ == "__main__":
    main()