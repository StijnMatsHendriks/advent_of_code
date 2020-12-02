from itertools import combinations

def not_so_smart_calculator(input_file, amount_of_entries):
    with open(input_file, "r") as f:
        data = [line for line in f for number in line.split()]
        data = [int(number.strip("\n")) for number in data]

        for comb in combinations(data, amount_of_entries):
            sumz = 0
            multz = comb[0]
            for index in range(amount_of_entries):
                sumz += comb[index]
                if index != 0:
                    multz *= comb[index]

                if sumz == 2020:
                    return sumz, multz


if __name__ == "__main__":
    answer = not_so_smart_calculator("00.txt", 3)
    print(answer)