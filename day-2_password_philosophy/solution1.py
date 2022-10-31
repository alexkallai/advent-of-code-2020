from pathlib import Path
import os

file_path = Path(__file__).parent
file_arg = os.path.join(file_path, "input.txt")

TREE = "#"

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

no_of_correct_passwords = 0


for index, line in enumerate(file_lines_list):
    print(line)
    password = line.split(":")[-1].strip()
    print(password)
    character = line.split(":")[0][-1]
    print(character)
    first_number = int(line.split(":")[0].split(" ")[0].split("-")[0])
    second_number = int(line.split(":")[0].split(" ")[0].split("-")[1])
    print(first_number)
    print(second_number)

    if first_number <= password.count(character) and password.count(character) <= second_number:
        no_of_correct_passwords += 1



print(no_of_correct_passwords)


