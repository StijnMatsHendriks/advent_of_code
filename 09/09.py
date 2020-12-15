def test_adapters(input_file):
    with open(input_file, "r") as f:
        data = f.read().split("\n")
        data = sorted([int(joltage) for joltage in data if joltage])

        num_1 = 1 # (0-->1) not in the list
        num_2 = 0
        num_3 = 1 # data[index-1]+3 not in the list

        for index, num in enumerate(data[:-1]):
            diff = data[index+1]-num
            num_1 += diff == 1
            num_2 += diff == 2
            num_3 += diff == 3

        return data, num_1 * num_3, num_1, num_2, num_3

def calc_combinations(data):
    overall_index = 1

    for index, num in enumerate(data):

        prev_num = data[overall_index + index - 1]
        next_num = data[index+1]
        if not (num-prev_num == 3 or next_num-num == 3):
            if next_num-prev_num <= 3:
                kan_aangepast = True

                kan_aangepast = False

    return kan_aangepast



if __name__ == "__main__":

    data, answer, num_1, num_2, num_3  = test_adapters("09.txt")
    #kan_aangepast = calc_combinations(data)

    print(data)
    print(answer)
    print(num_1, num_2, num_3)