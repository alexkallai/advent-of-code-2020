# empty: . tree: #
from sys import getsizeof
from pathlib import Path
import os

file_path = Path(__file__).parent
file_arg = os.path.join(file_path, "input.txt")

TREE = "#"

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()


NO_OF_REPEATED_PATTERNS = 2000
for index, line in enumerate(file_lines_list):
    file_lines_list[index] = line.strip() * NO_OF_REPEATED_PATTERNS

print(getsizeof(file_lines_list)/1024, " MB")

increment_list = [
                {"right": 1, "down": 1},
                {"right": 3, "down": 1},
                {"right": 5, "down": 1},
                {"right": 7, "down": 1},
                {"right": 1, "down": 2}
                ]


list_of_results = []

for dict in increment_list:
    horizontal_index = 0
    vertical_index = 0
    number_of_trees = 0
    while vertical_index < len(file_lines_list):
        if file_lines_list[vertical_index][horizontal_index] == TREE:
            number_of_trees += 1
        horizontal_index += dict["right"]
        vertical_index += dict["down"]
    list_of_results.append(number_of_trees)

print(list_of_results)
result = 1
for number in list_of_results:
    result *= number
print(result)