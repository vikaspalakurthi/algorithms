# Given a number N return the index value of the Fibonacci sequence, where the sequence is: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ... (sum of its previous last 2 numbers)
# Ex: N=5, return 5
#     N=6, return 8.

def fibonacciRecursive(n):
    # base case
    # recursive case. 
    # n = 0 then return 0, n = 1, then return 1. 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def fibonacciIterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev1 = 0
        prev2 = 1
        counter = 2
        while counter != n:
            value = prev1 + prev2
            prev1 = prev2
            prev2 = value
            counter +=1
        return prev1 + prev2

if __name__ == "__main__":
    for N in range(15):
        print(fibonacciIterative(N))
        print(fibonacciRecursive(N))