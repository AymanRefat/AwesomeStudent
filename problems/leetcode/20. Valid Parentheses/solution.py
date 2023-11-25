def isValid(s: str) -> bool:
    valid = ["()", "[]", "{}"]

    if len(s) == 2:
        if s in valid:
            return True
        return False

    for i in range(2, len(s)):
        if s[i - 2 : i] in valid:
            return isValid("".join((s[0 : i - 2], s[i:])))
    else:
        return False


if __name__ == "__main__":
    print(isValid("(((())))"))
