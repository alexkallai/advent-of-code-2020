from ast import walk
from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

# INPUT FILE ALREADY READ IN
# [{color: {color: amount,
#           color2: amount}},
#  {}
#   ...]
dict_of_bag_color_dicts = {}

for line in file_lines_list:
    color = line.strip().split("bags contain")[0].strip()
    contents = line.strip().split("bags contain")[1].strip()
    if "no other bags." not in contents:
        list_of_contents = contents.replace(".", "").split(", ")
    else:
        list_of_contents = []
    dict_of_content = {}
    for content_type in list_of_contents:
        content_color = content_type.split(" ", 1)[-1].replace(" bags", "").replace(" bag", "")
        content_amount = content_type.split(" ", 1)[0]
        dict_of_content.update({content_color: content_amount})
    dict_of_bag_color_dicts.update({color: dict_of_content})

# How many bag colors can eventually contain at least one shiny gold bag? 

def walk_graph_until_found(starting_color, color_to_find="shiny gold"):
    for content_color in dict_of_bag_color_dicts[starting_color]:
        if content_color == color_to_find:
            return True
        if walk_graph_until_found(content_color):
            return True
    return False
        

number_of_colors_able_to_contain_shiny_gold = 0
for index, line in enumerate(dict_of_bag_color_dicts):
    print(dict_of_bag_color_dicts[line])
    if walk_graph_until_found(line):
        number_of_colors_able_to_contain_shiny_gold += 1

print(number_of_colors_able_to_contain_shiny_gold)