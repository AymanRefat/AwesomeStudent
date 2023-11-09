def solution(strs: list[str]) -> str:
    counter = 1
    prefix = ""
    if len(strs) == 1:
        return strs[0]
    while True:
        test_prefix = strs[0][:counter]
        if prefix == test_prefix:
            return prefix
        for s in strs:
            if s == "":
                return ""
            if test_prefix == s[:counter]:
                continue
            else:
                return prefix

        else:
            prefix = test_prefix
            counter += 1


if __name__ == "__main__":
    print(solution([""]))
