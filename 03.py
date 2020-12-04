import re


def passport_validator(input_file):
    with open(input_file, "r") as f:
        data = f.read()
        data = data.split("\n\n")  # Eind paspoort = een empty line
        data = [line.replace("\n", " ").rstrip(" ") for line in data]
        data = [line.replace(" ", ",").split(",") for line in data]
        data = [[category.split(":") for category in passport] for passport in data]

        data_dict = {}

        for index, passport in enumerate(data):
            data_dict[index] = {info[0]: info[1] for info in passport}

        # Dictionary containing regexes with keys matching the keys of the passport dictionary.
        requirements = {
            "byr": r"^19[2-9][0-9]|200[0-2]$",
            "iyr": r"^201[0-9]|2020$",
            "eyr": r"^202[0-9]|2030$",
            "hgt": r"^59in|6[0-9]in|7[0-6]in|1[5-8][0-9]cm|19[0-3]cm$",
            "hcl": r"^#[a-f0-9]{6}$",
            "ecl": r"^amb|blu|brn|gry|grn|hzl|oth$",
            "pid": r"^[0-9]{9}$"
        }

        valid_count_ex1 = 0
        valid_count_ex2 = 0

        for index, passport in data_dict.items():
            # All keys except "cid" should be present in the passport.
            if all(item in passport.keys() for item in requirements.keys()):
                valid_count_ex1 += 1 # Valid passports in exercise 1
                # All values of the keys mentioned earlier should match with the regexes provided
                if all(re.match(requirements[key], passport[key]) for key in requirements.keys()):
                    valid_count_ex2 += 1 # Valid passports in exercise 2

    return valid_count_ex1, valid_count_ex2


if __name__ == "__main__":
    passports_ex1, passports_ex2 = passport_validator("03.txt")
    print(f"""Valid Passports exercise 1: {passports_ex1} 
Valid Passports exercise 2: {passports_ex2}""")


