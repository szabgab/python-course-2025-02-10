import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename) as fh:
    for row in fh:
        row = row.rstrip()
        if ";" not in row:
            continue
        row = row.rstrip(";")
        row = row.replace(" ","")
        #print(row)
        ix, values = row.split(";", maxsplit=1)
        values = values.split(";")
        #values.pop()
        print(values)
