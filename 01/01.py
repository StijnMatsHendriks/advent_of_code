def old_policy_check(data):
    data = [line for line in data if line[1].strip(":") in line[2]]

    valid_count = 0
    for line in data:
        count = line[2].count(line[1].strip(":"))
        min, max = int(line[0].split("-")[0]), int(line[0].split("-")[1])
        if count >= min and count <= max:
            valid_count += 1

    return valid_count

def new_policy_check(data):

    valid_count = 0
    for line in data:
        index_1, index_2 = int(line[0].split("-")[0])-1, int(line[0].split("-")[1])-1
        char = line[1].strip(":")
        pw = line[2]

        if len(pw) < index_1:
            continue
        else:
            if pw[index_1] == char and (len(pw) < index_2 or pw[index_2] != char):
                valid_count += 1
            if pw[index_2] == char and pw[index_1] != char:
                valid_count += 1

    return valid_count

def pw_checker(input_file):
    with open(input_file, "r") as f:
        data = [line.split() for line in f]

        return old_policy_check(data), new_policy_check(data)



if __name__ == "__main__":
    old, new = pw_checker("01.txt")
    print(old, new)

