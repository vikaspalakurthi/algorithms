# Some Notes on Recursion: 
# Instead of trying to code right away, practice asking:
# What’s the smallest input I can solve directly? (Base case)
# If I assume the smaller version is solved, how do I use it?
# How does the input shrink toward the base case?



def reverseStringIterative(s):
    r = []
    for i in range(len(s)):
        r.append(s[len(s)-i-1])
    return ''.join(r)
    # r = s[::-1]

def reverseStringRecursive(s):
    if len(s) <= 1:
        return s
    else:
        return reverseStringRecursive(s[1:]) + s[0]

if __name__ == "__main__":
    s = "vikas palakurthi"
    print(reverseStringIterative(s))
    print(reverseStringRecursive(s))