def find_occurrence(numbers, target):
    p_indices = []
    n_indices = []
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == target:
            p_indices.append(i)
            n_indices.append(-len(numbers) + i)
            count += 1
    return count, p_indices, n_indices
numbers = list(map(int, input("Enter the list of numbers : ").split(',')))
target = int(input("Enter the element to be found: "))
occurrence, p_indices, n_indices = find_occurrence(numbers, target)
print("Element", target, "occurs", occurrence, "time(s) in the list.")
print("Positive Index:", ", ".join(map(str, p_indices)))
print("Negative Index:", ", ".join(map(str, n_indices))) 

