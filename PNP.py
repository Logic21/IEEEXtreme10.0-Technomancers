import sys

input_data = sys.stdin.readlines()

static = input_data.pop(0).rstrip().split()
teams = int(static[0])
pizza = int(static[1])
nopizza= int(static[2])

input_data.pop(0)

pizza_scores = input_data[0:pizza]
input_data = input_data[pizza:]
pizza_scores = [-1 if x.rstrip() == '?' else int(x.rstrip()) for x in pizza_scores]

input_data.pop(0)

nopizza_scores = input_data[0:nopizza]
input_data = input_data[nopizza:]
nopizza_scores = [-1 if x.rstrip() == '?' else int(x.rstrip()) for x in nopizza_scores]

print pizza_scores
print nopizza_scores
