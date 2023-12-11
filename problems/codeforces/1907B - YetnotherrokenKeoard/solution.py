from collections import deque
from string import ascii_lowercase

for t in range(int(input())):
    lower_letters = set(ascii_lowercase)
    lower = deque()
    upper = deque()
    s = input()
    for i, l in enumerate(s):
        if l == "b":
            if lower:
                lower.pop()
            continue
        elif l == "B":
            if upper:
                upper.pop()
            continue
        elif l in lower_letters:
            lower.append((l, i))
        else:
            upper.append((l, i))
    result = [""] * (len(s))
    for l, i in lower:
        result[i] = l
    for l, i in upper:
        result[i] = l
    print("".join(result))
