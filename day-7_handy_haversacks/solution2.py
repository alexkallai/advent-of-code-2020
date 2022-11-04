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

def walk_graph_until_end(color):
    global number_of_bags_shiny_gold_contains
    for content_color in dict_of_bag_color_dicts[color]:
        for key in dict_of_bag_color_dicts[content_color].keys():
            print(key)
            print(dict_of_bag_color_dicts[content_color][key])
            print(dict_of_bag_color_dicts[content_color])
            number_of_bags_shiny_gold_contains += int(dict_of_bag_color_dicts[content_color][key])
            walk_graph_until_end(key)
        

number_of_bags_shiny_gold_contains = 0

walk_graph_until_end("shiny gold")
print("788964 too high 200 too low")
print(number_of_bags_shiny_gold_contains)