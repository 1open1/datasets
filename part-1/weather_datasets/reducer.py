import sys

dmax = {}
dmin = {}
for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t")
    if len(parts) == 2:
        year = int(parts[0])
        temp = int(parts[1])
        if year not in dmax:
            dmax[year] = temp
            dmin[year] = temp
        else:
            dmax[year] = max(dmax[year], temp)
            dmin[year] = min(dmin[year], temp)
print("Year,MaxTemp,MinTemp")
for year in sorted(dmax.keys()):
    print(f"{year},{dmax[year]},{dmin[year]}")
