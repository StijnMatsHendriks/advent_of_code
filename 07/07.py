from copy import deepcopy

def executor(input_file):
    with open(input_file, "r") as f:
        data = [line.split() for line in f.read().split("\n") if line]
        data = [[line[0], int(line[1])] for line in data]

        changed_indexes = []

        for i, changed_instruction in enumerate(data):
            orig_data = deepcopy(data)
            current_index = 0
            repeat_loop = True
            used_indexes = []
            accumulator = 0

            if i not in changed_indexes and (orig_data[i][0] == "nop" or orig_data[i][0] == "jmp"):
                if orig_data[i][0] == "jmp":
                    orig_data[i][0] = "nop"
                elif orig_data[i][0] == "nop":
                    orig_data[i][0] == "jmp"

            changed_indexes.append(i)
            accumulator, current_index = run_loop(accumulator, current_index, orig_data, repeat_loop, used_indexes)
            if current_index == len(data):
                return accumulator


def run_loop(accumulator, current_index, data, repeat_loop, used_indexes):
    while repeat_loop:
        slize = data[current_index]


        if current_index in used_indexes:
            return accumulator, current_index

        used_indexes.append(current_index)

        action = slize[0]
        increment = slize[1]

        if action == "jmp":
            current_index += increment
        elif action == "acc":
            accumulator += increment
            current_index += 1
        elif action == "nop":
            current_index += 1

        if current_index == len(data):
            return accumulator, current_index


if __name__ == "__main__":
    data = executor("07.txt")
    print(data)