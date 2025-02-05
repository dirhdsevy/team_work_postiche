def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def nsd_finder(a, b):
    while b:
        a, b = b, a % b
    return a