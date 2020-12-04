import numpy as np

def count_trees(input_file, x_incr, y_incr):
    with open(input_file, "r") as f:
        data = [line.split() for line in f]
        data = [list(line[0]) for line in data[:-1]]

        x, y = 0, 0
        x_incr, y_incr = x_incr, y_incr

        no_trees = 0

        while y < len(data):
            no_trees += data[y][x] == "#"

            y += y_incr
            x = (x + x_incr) % len(data[0])

        return no_trees

def count_trees_wrapper(input_file, increments):
    trees_per_route = []

    for increment in increments:
        trees = count_trees(input_file, increment[0], increment[1])
        trees_per_route.append(trees)

    return np.prod(trees_per_route)

if __name__ == "__main__":
    trees = count_trees_wrapper("02.txt", [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
    print(trees)