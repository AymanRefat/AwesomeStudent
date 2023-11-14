def solution(s: str) -> str:
    vowels = {
        "A": 65,
        "a": 97,
        "E": 69,
        "e": 101,
        "I": 73,
        "i": 105,
        "O": 79,
        "o": 111,
        "U": 85,
        "u": 117,
    }

    found = []
    new = s
    v = vowels.keys()
    for l in s:
        if l in v:
            found.append(l)
            new = new.replace(l, "@")

    found.sort(key=lambda x: vowels[x])

    for i in found:
        new = new.replace("@", i, 1)

    return new


if __name__ == "__main__":
    print(solution("lEetcOde"))
