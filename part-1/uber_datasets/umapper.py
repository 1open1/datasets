import sys
for line in sys.stdin:
    if line.startswith("START_DATE"):
        continue
    parts=line.strip().split(',')
    if len(parts)>=5:
        print(f"{parts[3]}\t1")
