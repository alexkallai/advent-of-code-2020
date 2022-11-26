from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

# INPUT FILE ALREADY READ IN

list_of_executed_lines = []
accumulator = 0
index = 0
    
while not index in list_of_executed_lines:
    list_of_executed_lines.append(index)
    command = file_lines_list[index].split(" ")[0].strip()
    argument = int(file_lines_list[index].split(" ")[1])

    print(f"The accumulator is {accumulator}, the row number is: {index}")
    print(f"Current command is: {command}, argument is {argument}")

    if command == "nop":
        index += 1
        continue
    if command == "acc":
        accumulator += (argument)
        index += 1
        continue
    if command == "jmp":
        index += (argument)
        continue

print(f"The final value of the accumulator is: {accumulator}")