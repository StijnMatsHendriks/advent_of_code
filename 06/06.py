import re

def bagz_of_bagz(input_file):
    with open(input_file, "r") as f:
        data = f.read().split("\n")

        bag_dict = {}
        pattern = r"[0-9]{1,}\s[a-z]{1,}\s[a-z]{1,}"

        for line in data:
            splitted_line = line.split("contain")
            contains = splitted_line[0][:-6]
            contained = splitted_line[1]

            contained_bags = re.findall(pattern, contained)
            contained_bags = {contained_bag[2:]: int(contained_bag[0]) for contained_bag in contained_bags}
            bag_dict[contains] = contained_bags

        total_bags, unique_bags = portable_black_hole(bag_dict, mode="contained")

        return total_bags, unique_bags


def portable_black_hole(bag_dict, mode):
    current_bags = ["shiny gold"]
    total_bags = []
    still_searching = True
    while still_searching:
        bags_this_iteration = []

        for bag in current_bags:
            for k, v in bag_dict.items():
                if mode == "contain":
                    if bag in v:
                        bags_this_iteration.append(k)
                elif mode == "contained":
                    if bag in k:
                        # print(k)
                        keyz = list(bag_dict[bag].keys())
                        valuez = list(bag_dict[bag].values())
                        for key, value in zip(keyz, valuez):
                            for i in range(value):
                                bags_this_iteration.append(key)

        total_bags.append(current_bags)
        unique_bags = len([set().union(*total_bags)][0])

        if not bags_this_iteration:
            still_searching = False

        current_bags = bags_this_iteration
    return total_bags, unique_bags


if __name__ == "__main__":
    total_bags, unique_bags = bagz_of_bagz("06.txt")
    total_bags = sum([len(bag_list) for bag_list in total_bags]) - 1 # minus 1 because shiny gold itself is in the list
    unique_bags = unique_bags - 1 # minus 1 because shiny gold itself is in the list

    print(f"The total number of bags is: {total_bags}")
    print(f"The total number of unique bags is: {unique_bags}")
