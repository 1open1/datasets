import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(",")
    if len(parts) == 2:
        year, temp = parts
        print(f"{year}\t{temp}")
