def boarding_pass_analyzer(input_file):
    with open(input_file, "r") as f:
        data = [line.split()[0] for line in f]

        data = [list(map(lambda char: 1 if (char == "F" or char == "L") else 0, list(boarding_pass))) for boarding_pass in data]

        new_data = []
        for barcode in data:
            row, col = barcode_to_data(barcode, mode="row"), barcode_to_data(barcode, mode="col")
            id = row[0] * 8 + col[0]
            new_data.append((row[0], col[0], id))

        new_data.sort(key=lambda x: x[2], reverse=True)

    return new_data

def barcode_to_data(barcode, mode):
    if mode == "row":
        barcode = barcode[:7]
        num = list(range(128))
    if mode == "col":
        barcode = barcode[7:]
        num = list(range(8))

    for char in barcode:
        grens = int(len(num) / 2)

        if not char:
            num = num[grens:]

        num = num[:grens]
    return(num)

def get_own_seat(new_data):
    data = sorted(list(set([id for (row, col, id) in new_data])))
    missing_ids = [data[index]+1 for index,id in enumerate(data[:-1]) if not data[index+1]-data[index] == 1]

    return missing_ids

if __name__ == "__main__":
    ids = boarding_pass_analyzer("04.txt")
    print("These are the plane seat IDs: ",ids,"\n")

    own_seat = get_own_seat(ids)
    print(f"Our own seat is {own_seat}")
