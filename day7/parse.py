import re

filename = "data.log"
with open(filename) as fh:
    for line in fh:
        #print(line)
        if "Fine Alignment Final theta position: T =" in line:
            #parts = line.split("= ")
            #parts[-1]
            #theta_position = float(line.split("= ")[-1].split()[0])
            theta_position = float(line.split("= ", 1)[-1].split()[0])
            print(f"split: {theta_position}")
        match = re.search(r"Fine Alignment Final theta position: T = (-?\d+\.\d+)", line)
        if match:
            theta_position = float(match.group(1))
            print(f"regex: {theta_position}")
            continue
        
        numbers = re.findall(r"\[(\d+\.\d+)\]", line)
        if numbers:
            numbers = [float(n) for n in numbers]
            print(numbers)

        # hex::0x000072C0  Dec::29376
        match = re.search(r"hex::0x([0-9A-F]+) +Dec::(\d+)", line)
        if match:
            hex_value = match.group(1)
            dec_value = int(match.group(2))
            print(f"hex: '{hex_value}', dec: {dec_value}")
            dec_from_hex = int(hex_value, 16)
            assert dec_value == dec_from_hex
            # hex_from_dec = f"0x{dec_value:X}"
            # print(f"hex from dec: '{hex_from_dec}'")
            # assert hex_value == hex_from_dec

        