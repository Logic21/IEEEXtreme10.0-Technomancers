import sys
import math

#All Stdin at once!
input_data = sys.stdin.readlines()

while len(input_data) and len(input_data[0].split()) == 2:
    header = input_data.pop(0).rstrip().split()
    header = [int(head) for head in header]

    posts = input_data[0:header[1]]
    input_data = input_data[header[1]:]
    posts = [int(post.rstrip()) for post in posts]

    threads = []
    threads_error = []
    thread_errors = []
    for idx,post in enumerate(posts):
        if post == 0:
            pointer = idx
            thread_size = 1
            #while pointer+1 in posts:
            pointers = (x for x in posts if x == pointer+1)
            for x in pointers:
                thread_size = thread_size+1
                pointer = posts.index(pointer+1)
            threads.append(thread_size)
            threads_error.append(abs(threads[-1]-header[0]))
            if len(threads) > 1:
                thread_errors.append(abs(thread_size+threads[-2]-header[0]))
    if len(threads) == 1:
        thread_errors.append(threads_error[0])
    page_errors = []
    for idx in range(len(threads_error)):
        thread_errors[int(math.ceil(idx/2))]
        if thread_errors[int(math.ceil(idx/2))] < threads_error[idx]:
            page_errors.append(thread_errors[int(math.ceil(idx/2))])
            idx = idx+1
        else:
            page_errors.append(threads_error[idx])

    page_errors.sort()
    print page_errors[-1]
