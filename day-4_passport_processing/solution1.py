# empty: . tree: 
# NEEDS 1 EXTRA LINE AT END OF
from cProfile import run
from sys import getsizeof
from pathlib import Path
import os

file_path = Path(__file__).parent
file_arg = os.path.join(file_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

# INPUT FILE ALREADY READ IN

"""

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

"""

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


def analyze_slice(slice: list):
    print(slice)
    global number_of_correct_passports
    list_of_passport_dict_elements = []
    for line in slice:
        list_to_add = line.strip().split(" ", -1)
        list_of_passport_dict_elements.extend(list_to_add)
    
    for index, element in enumerate(list_of_passport_dict_elements):
        list_of_passport_dict_elements[index] = {element.split(":")[0]: element.split(":")[-1]}
    for a in list_of_passport_dict_elements:
        print(a)

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
    print("CORRECT")
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