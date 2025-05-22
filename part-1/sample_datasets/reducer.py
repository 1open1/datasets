import sys

current_word = None
current_cnt = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word, cnt = line.split("\t", 1)
    try:
        cnt = int(cnt)
    except ValueError:
        continue

    if current_word == word:
        current_cnt += cnt
    else:
        if current_word:
            print(f"{current_word}\t{current_cnt}")
        current_word = word
        current_cnt = cnt

# Ensure the last word is printed
if current_word == word:
    print(f"{current_word}\t{current_cnt}")
