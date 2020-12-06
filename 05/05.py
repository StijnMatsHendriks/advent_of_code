def who_answered_yes(input_file):
    with open(input_file, "r") as f:
        data = f.read()
        data = data.split("\n\n")
        data = [person.split("\n") for person in data]

        # How many questions were answered yes by any of the members of a group?
        unique_group_sets = [set().union(*group_chars) for group_chars in data]

        num_any_answers = 0
        for group in unique_group_sets:
            num_any_answers += len(group)

        # How many questions were answered yes by all of the members of a group?
        same_answers = []
        for group_index, group_chars in enumerate(unique_group_sets):
            group_list = []
            for char in group_chars:
                group_data = data[group_index]
                people_said_yes = 0
                for group_member in group_data:
                    people_said_yes += char in group_member

                if people_said_yes == len(group_data):
                    group_list.append(char)
            same_answers.append(group_list)

        num_all_answers = 0
        for group in same_answers:
            num_all_answers += len(group)

        return num_any_answers, num_all_answers

if __name__ == "__main__":
    num_any_answers, num_all_answers = who_answered_yes("05.txt")
    print(f"These questions were answered with yes by any of the group members: {num_any_answers}")
    print(f"These questions were answered with yes by all of the group members: {num_all_answers}")
