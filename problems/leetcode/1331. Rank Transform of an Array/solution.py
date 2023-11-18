def arrayRankTransform(arr: list[int]) -> list[int]:
    nums = list(set(arr))
    nums.sort()

    ranks = {}
    ranks_list = []
    for index, num in enumerate(nums, 1):
        ranks[num] = index
    for i in arr:
        ranks_list.append(ranks[i])
    return ranks_list
