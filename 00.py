from itertools import combinations

def not_so_smart_calculator(input_file, amount_of_entries):
    with open(input_file, "r") as f:
        data = [line for line in f for number in line.split()]
        data = [int(number.strip("\n")) for number in data]

        for comb in combinations(data,amount_of_entries):
            sum = 0
            mult = comb[0]
            for index in range(amount_of_entries):
                sum += comb[index]
                if index != 0:
                    mult *= comb[index]

                if sum == 2020:
                    return sum, mult


if __name__ == "__main__":
    answer = not_so_smart_calculator("00.txt", 3)
    print(answer)