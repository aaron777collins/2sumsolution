def twoSumSorted(nums: list[int], target: int) -> tuple[int, int]:
    # returning the 2 indexes for summing to the target

    l = 0
    r = len(nums) -1

    while l < r:
        curSum = nums[l] + nums[r]

        if curSum == target:
            return (l, r)
        elif curSum < target:
            # move left pointer to the right aka choosing a bigger number
            l += 1
        else:
            # curSum > target
            # moving the right pointer to the left to choose a smaller number
            r -= 1

    return (-1, -1)

if __name__ == "__main__":
    nums = [1, 2, 3, 5, 6]
    target = 9
    l, r = twoSumSorted(nums, target)
    print(nums[l], '+', nums[r], '=', target)

    nums = [1, 1, 1]
    target = 3
    l, r = twoSumSorted(nums, target)
    assert(l == -1)
    assert(r == -1)
    print("Couldn't find it!")
