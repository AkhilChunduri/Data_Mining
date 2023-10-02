fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

NUMBERS = ["1","2","3","4","5"]
for num in NUMBERS:
    print(num)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

#Use enumerate to get the index value of the element 
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index + 1}: {color}")

#Looping over a range
for i in range(1, 6):
    print(i)


# Define the number of rows for the reversed triangle
num_rows = 5

# Outer loop for rows
for i in range(1, num_rows+1):
    # Inner loop for printing asterisks
    for j in range(num_rows-i):
        print(" ", end=" ")   
    for k in range(i):
        print("*",end=" ")
    # Move to the next line after each row
    print()

# Outer loop for rows
for i in range(num_rows):
    # Inner loop for printing asterisks
    for j in range(0,num_rows-2):
        print(" ", end=" ")   
    for k in range(i,i+2):
        print("*",end=" ")
    # Move to the next line after each row
    print()

  