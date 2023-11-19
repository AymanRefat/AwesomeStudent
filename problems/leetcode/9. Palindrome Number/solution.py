def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    counter = -1
    for i in str(x):
        if i == str(x)[counter]:
            counter -= 1
        else:
            return False
    return True
