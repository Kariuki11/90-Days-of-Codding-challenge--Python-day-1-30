def second_largest(numbers):
    # Remove duplicates by converting the list to a set
    unique_numbers = set(numbers)
    
    # If there are fewer than 2 unique numbers, return None
    if len(unique_numbers) < 2:
        return None
    
    # Convert the set back to a list and sort it in ascending order
    sorted_numbers = sorted(unique_numbers)
    
    # Return the second last element (second largest)
    return sorted_numbers[-2]

# Example usage:
print(second_largest([10, 5, 20, 20, 15]))  # Output: 15
print(second_largest([1, 1, 1]))            # Output: None
print(second_largest([5, 7, 3, 9, 4]))      # Output: 7