import sys
current_city=None
current_cnt=0
for line in sys.stdin:
    line=line.strip()
    parts=line.split('\t')
    if len(parts)!=2:
        continue
    city=parts[0]
    cnt=parts[1]
    try:
        cnt=int(parts[1])
    except ValueError:
        continue
    if city==current_city:
        current_cnt+=cnt
    else:
        if current_city:
            print(f"{current_city}\t{current_cnt}")
        current_cnt=cnt
        current_city=city
    
if current_city==city:
    print(f"{current_city}\t{current_cnt}")

