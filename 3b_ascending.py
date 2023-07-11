def is_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

# Read the list of numbers from the user
numbers = list(map(int, input("Enter the list of numbers (comma-separated): ").split(',')))

# Check if the list is in ascending order
if is_ascending(numbers):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")

