# Program to perform Linear Search on a list of items
numbers = [12, 35, 78, 90, 45, 23, 67]
target = int(input("Enter the number you want to search for: "))

found = False
position = -1

# Traversal through the list
for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        position = i
        break  # Exit the loop as soon as the item is found

if found:
    print(f"Element found at index position: {position}")
else:
    print("Element not found in the list.")
