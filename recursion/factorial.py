# Recursion Implementation:
# Make sure to have the below cases when you think of implementing Recursion:
# 1. Base case (stop)
# 2. recursive case (keep calling)
# 3. Get closer and closer and return when needed. 2 -> 1. Usually 2 returns. 

def findFactorialRecursive(num):
    if num == 1:
        return num
    else:
        return num * findFactorialRecursive(num-1)

def findFactorialIterative(num):
    #factorial = 1
    #for i in range(1,num+1):
    #    factorial = factorial * i
    #return factorial
    fact = num
    while num > 1 :
        fact = fact * (num-1)
        num -= 1
    return fact


if __name__ == "__main__":
    n = 5
    print(findFactorialRecursive(5))
    print(findFactorialIterative(5))