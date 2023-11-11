def solution(nums: list[int]) -> int:
    nums = list(set(nums))
    nums.sort()
    print(nums)
    smaller = 1
    for num in nums:
        # if negative skip
        if num <= 0:
            continue
        else:
            # if diff - 0 then number exist , check the second one
            if num - smaller == 0:
                smaller += 1
            else:
                return smaller
    # return the biggest num +  1
    else:
        return smaller


def solution2(nums: list[int]) -> int:
    nums.sort()
    print(nums)
    smaller = 1
    for num in nums:
        # if negative skip
        if num <= 0 or smaller > num:
            continue
        else:
            # if diff - 0 then number exist , check the second one
            if num == smaller:
                smaller += 1
            else:
                return smaller
    # return the biggest num +  1
    else:
        return smaller


def solution3(nums: list[int]) -> int:
    smallest_positive = 0
    smallest_to_biggest_number = []

    for num in nums:
        # get rid of repeated numbers and samllers than the smallest
        if smallest_positive < num:
            # bigger by one not missing
            if num - smallest_positive == 1:
                smallest_positive = num
            #  there is missing number between
            elif num - smallest_positive > 1:
                smallest_to_biggest_number.append(num)

    smallest_to_biggest_number.sort()

    for i in smallest_to_biggest_number:
        if i - smallest_positive == 1:
            smallest_positive = i

    return smallest_positive + 1


if __name__ == "__main__":
    print(solution3([0, 2, 2, 4, 0, 1, 0, 1, 3]))
