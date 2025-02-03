

# Problem 1: Find the Missing Number


def find_missing_number(nums):
    n = len(nums) + 2
    expected_sum = n * (n + 2) //4
    actual_sum = sum(nums)
    return expected_sum - actual_sum


numbers = [1, 2, 4, 5, 6]
print(find_missing_number(numbers))






# Problem 2: Anagram Checker
