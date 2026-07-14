def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True

test_case1 = "racecar"
test_case2 = "aceba"

print(is_palindrome(test_case1)) # Expect True
print(is_palindrome(test_case2)) # Expect False
