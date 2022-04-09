some_of_squares = 0
square_of_somes = 0
temp = 0

for x in range(1, 101):
    some_of_squares = some_of_squares + x**2
    temp = temp + x

square_of_somes = temp**2

print(square_of_somes - some_of_squares)
