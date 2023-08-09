def twoSum(nums: list[int], target: int):
    # Not sorted this time, find 2 nums to create sum

    numLookup = {}

    for i, num in enumerate(nums):
        oppositeNum = target-num
        if oppositeNum in numLookup:
            # we found a match
            return (numLookup[oppositeNum], i)

        # otherwise we didn't find a match
        numLookup[num] = i # store in num lookup

    # no result
    return (-1, -1)


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 6]
    target = 9
    l, r = twoSum(nums, target)
    print(nums[l], '+', nums[r], '=', target)

    nums = [1, 1, 1]
    target = 3
    l, r = twoSum(nums, target)
    assert(l == -1)
    assert(r == -1)
    print("Couldn't find it!")

