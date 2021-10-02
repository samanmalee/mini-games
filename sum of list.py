# Code a function to receive a list of integers seperated by commas and to
# return the sum of the numbers

def f1(lst):
    L1 = lst.split(",") # ["1","2","3","4","5"]
    c = [int(i) for i in L1] # [1,2,3,4,5]
    return sum(c)

sum1 = f1("1,2,3,4,5")
print(sum1)
sum2 = f1("40,20,30")
print(sum2)