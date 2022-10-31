from pathlib import Path
import os

file_folder_path = Path(__file__).parent
file_arg = os.path.join(file_folder_path, "input.txt")

with open(file_arg, "r", encoding = "utf-8") as f:
    file_lines_list = f.readlines()

# INPUT FILE ALREADY READ IN
max_seat_id = 0
list_of_seat_locator_dicts = []

for line in file_lines_list:
    seat_row_locator = line.strip()[0:7]
    seat_no_locator = line.strip()[7:10]
    print(seat_row_locator)
    print(seat_no_locator)
    # L: 0 R: 1
    # F: 0 B: 1
    seat_row_binary_no = seat_row_locator.replace("F", "0").replace("B", "1")
    seat_no_binary_no = seat_no_locator.replace("L", "0").replace("R", "1")

    seat_row_dec = int(seat_row_binary_no, 2)
    print(seat_row_binary_no, " - ", seat_row_dec)
    seat_no_dec = int(seat_no_binary_no, 2)
    print(seat_no_binary_no, " - ", seat_no_dec)

    list_of_seat_locator_dicts.append(
        {
            "seat_row": seat_row_dec,
            "seat_number": seat_no_dec
        }
        )
    if (seat_row_dec*8 + seat_no_dec) > max_seat_id:  
        max_seat_id = seat_row_dec*8 + seat_no_dec

print(max_seat_id)