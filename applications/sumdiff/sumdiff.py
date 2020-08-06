"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
from itertools import product

#q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)
test = (1,1,3)

def f(x):
    return x * 4 + 6

# Your code here
# Make caches for the plus/left and minus/right sides of the equation
## Key = tuple(val1, val2), Value = f(val1) + f(val2) or f(val1) - f(val2)
plus_cache = {}
minus_cache = {}
# Use Cartesian product to get the 
perm = product(q,repeat=2)
for pair in list(perm):
    f1 = f(pair[0])
    f2 = f(pair[1])
    plus_cache[pair] = f1 + f2
    if f1 > f2:
        minus_cache[pair] = f1 - f2

for plus_item in list(plus_cache.items()):
    for minus_item in list(minus_cache.items()):
        if plus_item[1] == minus_item[1]:
            p1 = plus_item[0][0]
            p2 = plus_item[0][1]
            m1 = minus_item[0][0]
            m2 = minus_item[0][1]
            o1 = f(p1)
            o2 = f(p2)
            o3 = f(m1)
            o4 = f(m2)
            print(f"f({p1}) + f({p2}) = f({m1}) - f({m2})    {o1} + {o2} = {o3} - {o4}")
