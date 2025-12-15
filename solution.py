def day1(input_file, start=50):
    """
    Description of the problem to solve : https://adventofcode.com/2025/day/1
    This function is a solution of the day 1 of advent of code (2025)
    """
    dictionnary = []
    with open(input_file, "r") as puzzle_input:
        for line in puzzle_input:
            dictionnary.append([line[0], int(line[1:].strip())])

    for line in dictionnary:
        if line[0] == 'L':
            line[1] = -line[1]

    counter = start
    zero_counter = 0

    for line in dictionnary:
        counter = (counter + line[1]) % 100
        if counter == 0:
            zero_counter += 1

    return zero_counter
