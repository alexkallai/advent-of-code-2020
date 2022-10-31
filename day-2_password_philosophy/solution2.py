
with open("input.txt", "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()


no_of_correct_passwords = 0


for index, line in enumerate(file_lines_list):
    print("\n\n\n\n\n\n\n\n")
    print(line)
    password = line.split(":")[-1].strip()
    print(password)
    character = line.split(":")[0][-1]
    print(character)
    first_number = int(line.split(":")[0].split(" ")[0].split("-")[0])
    second_number = int(line.split(":")[0].split(" ")[0].split("-")[1])
    print(first_number)
    print(second_number)
    
    if second_number  <= len(password):
        if (password[first_number-1] == character) ^ (password[second_number-1] == character):
            no_of_correct_passwords += 1


print("\n")
print(no_of_correct_passwords)
