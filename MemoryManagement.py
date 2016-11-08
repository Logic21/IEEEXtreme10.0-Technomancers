import sys
import math

def fifo(num_pages,accesses):
    stack = []
    num_unload = 0
    for page in accesses:
        if page not in stack:
            stack.insert(0, page)
            if len(stack) > num_pages:
                stack.pop()
                num_unload = num_unload+1
    return num_unload

def lru(num_pages,accesses):
    stack = []
    num_unload = 0
    for page in accesses:
        if page not in stack:
            stack.insert(0,page)
            if len(stack) > num_pages:
                stack.pop()
                num_unload = num_unload+1
        else:
            stack.remove(page)
            stack.insert(0,page)
    return num_unload

#All Stdin at once!
input_data = sys.stdin.readlines()

num_tests = int(input_data.pop(0))

for test in range(num_tests):
    static = input_data.pop(0).split()

    #Static
    os_pages = int(static[0])
    page_size = int(static[1])
    mem_accesses = int(static[2])

    addresses = input_data[0:mem_accesses]
    input_data = input_data[mem_accesses:]
    page_accesses = [int(math.floor(int(address)/page_size)) for address in addresses]

    fifo_res = fifo(os_pages, page_accesses)
    lru_res = lru(os_pages, page_accesses)

    print ("yes" if lru_res < fifo_res else "no") + " " + str(fifo_res) + " " + str(lru_res)
