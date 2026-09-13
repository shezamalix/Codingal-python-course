numbers = [6, 4, 6, 8, 9, 1, 78, 10]

#find the sum and average

sum = 0

for i in numbers :
    sum += i
print("sum =", sum)

average = sum / len(numbers)
print("The average is", average)

numbers.sort() #sorts in ascending order
print(numbers)

print("minimum :", numbers[0])
print("Maximum :", numbers[-1])

a = [[1, 2, 3, 100, 200],
    [4, 5, 6],
    [7, 8, 9]]

print(len(a[0]))