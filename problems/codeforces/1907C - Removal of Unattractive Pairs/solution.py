from collections import Counter

for t in range(int(input())):
    n = int(input())
    counter = Counter(input())
    max_char = counter.most_common(1)[0][1]
    others = sum(x for x in counter.values()) - max_char
    if (max_char - others) >= 0:
        print(max_char - others)
    else:
        print(n % 2)
