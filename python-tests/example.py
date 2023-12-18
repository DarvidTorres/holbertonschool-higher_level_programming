#!/usr/bin/python3
# for i in range(3):
# 	if i == 1:
# 		continue
# 	print(i)

# lambda x: x + 1

def high_ord_func(n):
    return lambda x: x + n

f = high_ord_func(3)
print(f(2))