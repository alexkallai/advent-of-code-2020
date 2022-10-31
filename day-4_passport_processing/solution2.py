# empty: . tree: 
# NEEDS 1 EXTRA LINE AT END OF
from cProfile import run
from sys import getsizeof
from pathlib import Path
import os
import string

file_path = Path(__file__).parent
file_arg = os.path.join(file_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

# INPUT FILE ALREADY READ IN

number_of_correct_passports = 0

list_of_mandatory_fields = [
                            "byr",
                            "iyr",
                            "eyr",
                            "hgt",
                            "hcl",
                            "ecl",
                            "pid"
                            #"cid"
                            ]

def verify_passport_dict_element(dict_element: dict):
    try:
        key = list(dict_element.keys())[0]
        if key == "byr":
            if len(dict_element[key]) == 4:
                birth_year = int(dict_element[key])
                return 1920 <= birth_year <=2002
        if key == "iyr":
            if len(dict_element[key]) == 4:
                issue_year = int(dict_element[key])
                return 2010 <= issue_year <= 2020
        if key == "eyr":
            if len(dict_element[key]) == 4:
                expiration_year = int(dict_element[key])
                return 2020 <= expiration_year <= 2030
        if key == "hgt":
            if "in" in dict_element[key]:
                height_in_inches = int(dict_element[key].strip().removesuffix("in"))
                return 59 <= height_in_inches <= 76
            if "cm" in dict_element[key]:
                height_in_cm = int(dict_element[key].strip().removesuffix("cm"))
                return 150 <= height_in_cm <= 193
        if key == "hcl":
            hair_color_value = dict_element[key]
            allowed_chars = set(string.digits + "a" + "b" + "c" + "d" + "e" + "f" + "#")
            return (hair_color_value[0] == "#" and 
                    set(hair_color_value).issubset(allowed_chars))
        if key == "ecl":
            eye_color_value = dict_element[key]
            return eye_color_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if key == "pid":
            passport_id = dict_element[key]
            return len(passport_id) == 9 and set(passport_id).issubset(string.digits)
        if key == "cid":
            return True
    except:
        print("EXCPTION")
        return False
    return False


def analyze_slice(slice: list):
    print(slice)
    global number_of_correct_passports
    list_of_passport_dict_elements = []
    for line in slice:
        list_to_add = line.strip().split(" ", -1)
        list_of_passport_dict_elements.extend(list_to_add)
    
    for index, element in enumerate(list_of_passport_dict_elements):
        list_of_passport_dict_elements[index] = {element.split(":")[0]: element.split(":")[-1]}

    #for entry in list_of_passport_dict_elements:
    #list_of_keys = (list(entry.keys())[0] in list_of_mandatory_fields for entry in list_of_passport_dict_elements)
    #if all( list(entry.keys())[0] in list_of_mandatory_fields for entry 
            #in list_of_passport_dict_elements 
                #if list(entry.keys())[0] != "cid"):
        #number_of_correct_passports += 1
    temp_list = []
    for entry in list_of_passport_dict_elements:       
        temp_list.append(list(entry.keys())[0])
    temp_list.sort()
    print(temp_list)
    for element in list_of_mandatory_fields:
        if element not in temp_list:
            print(f"INCORRECT {element}  missing")
            return
    for a in list_of_passport_dict_elements:
        print(a)
        is_a_correct = verify_passport_dict_element(a)
        if not is_a_correct:
            print("PASSPORT INCORRECT")
            return
        if is_a_correct:
            print("PASSPORT FIELD CORRECT")

    print("FULL PASSPORT CORRECT")
    number_of_correct_passports += 1

list_of_passport_dicts = []

from_idx = 0
to_idx = 0

runner_index = 0
while runner_index < len(file_lines_list):
    #print(f"Actual line: {file_lines_list[runner_index]}")
    #print(f"Actual line type: {type(file_lines_list[runner_index])}")
    passport_dict = {}
    to_idx = runner_index

    if file_lines_list[runner_index] == "\n":
        print("\n\n")
        analyze_slice(file_lines_list[from_idx:to_idx])
        from_idx = runner_index +1

    runner_index += 1

print("281 too high, 225 too low")
print(number_of_correct_passports)