def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    # populate hashmap
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]

    return []



test_case1 = [2,7,11,15]
test_case2 = [3,2,4]
test_case3 = [3,3]



print(f"Test Case 1:\n Expected output: [0, 1]\n Actual Output: {twoSum(test_case1, 9)} ")
print(f"Test Case 2:\n Expected output: [1, 2]\n Actual Output: {twoSum(test_case2, 6)}")
print(f"Test Case 3:\n Expected output: [0, 1]\n Actual Output: {twoSum(test_case3, 6)}")
