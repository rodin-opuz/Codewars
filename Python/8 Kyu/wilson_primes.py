import math
def am_i_wilson(n):
    if n < 2: return False
    return (math.factorial(n - 1) + 1) % (n * n) == 0
