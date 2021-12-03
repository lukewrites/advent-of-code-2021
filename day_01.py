from typing import List


def data_getter(file: str) -> List:
    data = []
    with open(file, 'r') as readings:
        for line in readings:
            data.append(int(line))
    return data


def data_analyzer(input: List, skip: int=0):
    # keep track of things
    previous = input[0]
    increases = 0

    if skip > 0:
        first, second, third = 0, 1, 2

    # analyze the input
    else:
        for item in input:
            if item > previous:
                increases += 1
            previous = item

    print('Skip', skip, ':', increases)


def main():
    data = data_getter('rsc/01.txt')
    return data_analyzer(data)
    data_analyzer(data, 3)


if __name__ == "__main__":
    main()
