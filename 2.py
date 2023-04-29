x = int(input("num1"))
y = int(input("num2"))
z = int(input("num3"))
n = int(input("num4"))

# Create a list comprehension with all possible combinations of i, j and k
# where 0 <= i <= x, 0 <= j <= y and 0 <= k <= z
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

# Filter the coordinates to exclude the ones where i+j+k equals n
filtered_coordinates = [c for c in coordinates if sum(c) != n]

# Print the filtered coordinates
print(filtered_coordinates)