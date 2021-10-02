# Algorithm
# 1) Get the numbers as a string by ,
x = input('Enter the string of numbers ->')
print(x)
# 2) Convert the list to a list of sub strings
y = x.split(",")
#  3) Convert the strings in the list to numbers
y = [int(i) for i in y]
print(y)
# 4) Sum the numbers in the list of numbers
z = sum(y)
# 5) Print the answer
print(z)