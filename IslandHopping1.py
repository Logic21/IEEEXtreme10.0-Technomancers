import sys

#All Stdin at once!
input_data = sys.stdin.readlines()

num_tests = int(input_data.pop(0).rstrip())

for test in range(num_tests):
    num_islands = int(input_data.pop(0).rstrip())

    islands = input_data[0:num_islands]
    islands = [[island.rstrip().split()[0],int(island.rstrip().split()[1])] for island in islands]
    input_data = input_data[num_islands:]

    num_channels = int(input_data.pop(0).rstrip())

    channels = input_data[0:num_channels]
    channels = [[channel.rstrip().split()[0],channel.rstrip().split()[1],int(channel.rstrip().split()[2])] for channel in channels]
    input_data = input_data[num_channels:]

    fuel = 0
    fuel = fuel+
