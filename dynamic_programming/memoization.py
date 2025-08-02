# Dynamic Programming is in simpler way just an optimization technique where if we can use Cache, we can use DP. 

def AddtoNumber80(n):
    # Assume this calculation takes long time. 
    print("long time")
    return n+80

#print(AddtoNumber80(5)) # Output: long time, 85
#print(AddtoNumber80(5)) # Output: long time, 85

# Basically, performing the same calculations over and over. 
# This is where we introudce caching. 

cache = {}

def AddtoNumber80Cache(n):
    if n in cache:
        return cache[n]
    else:
        print("long time") # assuming the calculation is long time. 
        cache[n] = n+80
        return cache[n]

#print(AddtoNumber80Cache(5)) # Output: long time, 85
#print(AddtoNumber80Cache(5)) # Output: 85

# Closure concept, where we dont want the cache to be global. with in the function, and also the main function to remember the state, in this case: cache. 

def AddtoNumber80Closure():
    cache = {}
    def function(n):
        if n in cache:
            return cache[n]
        else:
            print("long time")
            cache[n] = n + 80
            return cache[n]
    
    return function # We are passing the whole function itself, basically referencing it. 

add = AddtoNumber80Closure()
print(add(5))
print(add(6))
print(add(5))