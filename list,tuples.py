#tuples_example
coordinates = (10.0, 20.0)
print(coordinates[0])  # Output: 10.0

# coordinates[0] = 30.0  # ❌ This would cause an error (tuples are immutable)


#lists implementation
fruits = ["apple", "banana", "mango"]
fruits.append("orange")  # Add item
fruits[0] = "grape"       # Change item
print(fruits)             # ['grape', 'banana', 'mango', 'orange']


# range_implentation
for i in range(3):
    print(i)
# Output:
# 0
# 1
# 2