import sys

def calc_ranges(items):
    diffs = []
    for idx, val in enumerate(items):
        if len(items) > idx+1:
            diffs.append(items[idx+1]-items[idx])
    return diffs

#All Stdin at once!
data = sys.stdin.readlines()

#First Line is Number of Tests
num_tests = int(data.pop(0))

for test in range(num_tests):

    tmp = data[0].split(' ')
    data = data[1:]

    # Number of Dogs, Walkers, and how many need to be combined into groups
    num_dogs = int(tmp[0])
    num_walkers = int(tmp[1])
    #num_reduce = num_dogs-num_walkers

    dogs = data[0:num_dogs]
    #dogs = [int(x) for x in dogs]
    dogs = list(map(int, dogs))
    data = data[num_dogs:]
    dogs.sort()# = sorted(set(dogs))

    ranges = calc_ranges(dogs)
    ranges.sort()

    num_reduce = (len(dogs)-num_walkers)
    #if num_reduce > len(ranges):
        #num_reduce = len(ranges)

    print(sum(ranges[0:num_reduce]))
