

with open("input.txt", "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

for index, line in enumerate(file_lines_list):
    file_lines_list[index] = int(line) 

print(file_lines_list)



for index, line in enumerate(file_lines_list):
    for i, l in enumerate(file_lines_list):
        for idx, lin in enumerate(file_lines_list):
            if not i == index and not idx == i:
                if line + l + lin == 2020:
                    print(f"The solution is: {l*line*lin}")
                    break

    
