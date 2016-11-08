import sys
import math

#All Stdin at once!
input_data = sys.stdin.readlines()

num_tests = int(input_data.pop(0))

for test in range(num_tests):
    num_petals = int(input_data.pop(0))
    a = 2
    while a <= num_petals:
        a=a**2
    diff=a-num_petals
    if diff == 0:
        print 1
    else:
        print (a-2*diff+1)
