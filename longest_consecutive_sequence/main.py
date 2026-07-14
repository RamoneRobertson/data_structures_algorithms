def find_longest_consecutive_sequence(nums: List[int]) -> int:
    longest_streak = 0

    for num in nums:
        current_num = num
        current_streak = 1

        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1

        longest_streak = max(current_streak, longest_streak)

    return longest_streak


test_case1 = [100,4,200,1,3,2]
test_case2 = [0,3,7,2,5,8,4,6,0,1]
test_case3 = [1,0,1,2]

print(
    f"Test Case 1 Output: {find_longest_consecutive_sequence(test_case1)}\n"
    f"Test Case 2 Output: {find_longest_consecutive_sequence(test_case2)}\n"
    f"Test Case 3 Output: {find_longest_consecutive_sequence(test_case3)}"
)
