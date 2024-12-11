def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list.")
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

try:
    my_empty_list = []
    average_empty = calculate_average(my_empty_list)
    print(f"The average of an empty list is: {average_empty}")
except ValueError as e:
    print(f"Error: {e}")

#This solution handles the empty list case by raising a ValueError exception, which is a more appropriate way of signaling an error condition.