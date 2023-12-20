def find_largest_smallest(a, b, c, d):
    largest = max(a, b, c, d)
    smallest = min(a, b, c, d)
    return largest, smallest

# Example usage:
num1, num2, num3, num4 = 10, 5, 20, 15
largest_num, smallest_num = find_largest_smallest(num1, num2, num3, num4)
print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
