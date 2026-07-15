def has_pair(nums: List[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1


    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return True
        if curr_sum > target:
            right -= 1
        else:
            left += 1


    return False

test_case1 = [1, 2, 4, 6, 8, 9, 14, 15]

print(has_pair(test_case1, 14)) # Expected output True
