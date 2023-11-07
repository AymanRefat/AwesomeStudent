def solution(self, nums1: list[int], nums2: list[int]) -> float:
    nums1 += nums2
    print(nums1)
    nums1.sort()
    length = len(nums1)
    # even
    if length % 2 == 0:
        return (nums1[int(length / 2 - 1)] + nums1[int(length / 2)]) / 2
    else:
        print(length - 1)
        return nums1[int((length - 1) / 2)]
