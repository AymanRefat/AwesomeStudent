def findMin(nums: list[int]) -> int:
    end = len(nums)
    mid = round((end) / 2)
    # if start of nums smallers than the end of them
    #  this means that no rotation has been
    if end == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]
    else:
        g1 = nums[:mid]
        g2 = nums[mid:]
        if len(g1) == 1 and len(g2) == 1:
            return g1[0] if g1[0] < g2[0] else g2[0]
        #  if the start of range is smaller than the end
        # this means it's sorted right we can exclude it
        if g1[0] < g1[-1]:
            return findMin(g2)
        else:
            return findMin(g1)


if __name__ == "__main__":
    print(findMin([3, 4, 5, 1, 2]))
