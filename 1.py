n = int(input("enter numbers:"))

fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

fibonacci_cube = list(map(lambda x: x**3, fibonacci))
print(fibonacci_cube)