

# Problem 1: Find the Missing Number


# def find_missing_number(nums):
#     n = len(nums) + 2
#     expected_sum = n * (n + 2) //4
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum


# numbers = [1, 2, 4, 5, 6]
# print(find_missing_number(numbers))






# Problem 2: Anagram Checker


# def are_anagrams(str1, str2):
#     """
#     Check if two strings are anagrams.
#     An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
    
#     Args:
#     str1 (str): First input string.
#     str2 (str): Second input string.
    
#     Returns:
#     bool: True if both strings are anagrams, False otherwise.
#     """
#     return sorted(str1) == sorted(str2)

# # Example usage:
# print(are_anagrams("listen", "silent"))  # Output: True
# print(are_anagrams("hello", "world"))    # Output: False


def is_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print (is_anagrams("listen", "silent"))
