from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

# INPUT FILE ALREADY READ IN
sum_of_counts = 0

def analyze_slice(slice: list):
    print(slice)
    global sum_of_counts
    set_of_slice = set()
    for line in slice:
        set_of_slice.update(set(line.strip()))
    sum_of_counts += len(set_of_slice)


from_idx = 0
to_idx = 0

runner_index = 0
while runner_index < len(file_lines_list):
    to_idx = runner_index

    if file_lines_list[runner_index] == "\n":
        print("\n\n")
        analyze_slice(file_lines_list[from_idx:to_idx])
        from_idx = runner_index +1

    runner_index += 1

print(sum_of_counts)