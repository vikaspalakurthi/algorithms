# Implementing fibonacci using recursion and Dynamic Programming. 

# Recursive fib: 

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(50))

# Using Dynamic Programming: 

def fibDP():
    cache = {}
    def fib(n):
        if n in cache:
            return cache[n]
        if n < 2: 
            return n
        else:
            cache[n] =  fib(n-1) + fib(n-2)
        return cache[n]

    return fib

#findFibonacciIndex = fibDP()
#print(findFibonacciIndex(100))