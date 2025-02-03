# Problem 1: Find the Missing Number


def find_missing_number(nums):
    n = len(nums) + 2
    expected_sum = n * (n + 2) //4
    actual_sum = sum(nums)
    return expected_sum - actual_sum


numbers = [1, 2, 4, 5, 6]
print(find_missing_number(numbers))






# Problem 2: Anagram Checker



def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print (are_anagrams("listen", "silent"))
print (are_anagrams("heloo", "Kenn"))



# Problem 3: Anagram Checker (Optimized)

def is_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print (is_anagrams("listen", "silent"))
