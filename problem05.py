from functools import reduce
from math import lcm

print(reduce(lcm, range(1, 21)))
