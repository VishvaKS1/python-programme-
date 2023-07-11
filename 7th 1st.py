def get_element_at_index(numbers):
    try:
        index = int(input("Enter an index: "))
        element = numbers[index]
        print("Element at index", index, "is", element)
    except IndexError:
        print("Error: Index is out of range.")
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
get_element_at_index(numbers)
