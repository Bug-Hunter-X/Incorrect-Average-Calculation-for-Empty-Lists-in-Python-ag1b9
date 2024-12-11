def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#The bug is that when the list is empty the return value is 0, which is not a good solution in many cases.
#A better solution would be to return an appropriate error message or raise an exception in cases where the list is empty.

