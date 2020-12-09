def wrapper(input_file, preamble_length):
    with open(input_file, "r") as f:
        data = f.read().split("\n")
        data = [int(num) for num in data if num]

        outlier = find_outlier(data, preamble_length)
        weakness = crack_the_code(data, outlier)

        return outlier, weakness

def find_outlier(data, preamble_length):
    for index, num in enumerate(data[preamble_length:]):
        preamble = data[index:index + preamble_length]
        combinations = [x + y for x in preamble for y in preamble]
        if not num in combinations:
            return num

def crack_the_code(data, outlier):
    for start_num in range(len(data)):
        sumz = 0
        sum_list = []

        slice = data[start_num:]
        for num in slice:
            sumz += num
            sum_list.append(num)
            if sumz == outlier:
                return (min(sum_list) + max(sum_list))




if __name__ == "__main__":
    outlier, weakness = wrapper("08.txt", 25)
    print(f"This is the nasty little outlier, just lying out: {outlier}")
    print(f"This is the weakness that we should exploit: {weakness}")
