import sys

#All Stdin at once!
input_data = sys.stdin.readlines()

base_set = input_data.pop(0).rstrip().split()

base = int(base_set[0])
base_char_set = base_set[1]

operand_a = input_data.pop(0).rstrip()
operand_b = input_data.pop(0).rstrip()

line = input_data.pop(0).rstrip()

print str(base) + " " + base_char_set
print operand_a
print operand_b
print line

op_a = operand_a[::-1].rstrip()
op_b = operand_b[:0:-1].rstrip()

total = ""
carry = 0

num_digits = max(len(op_a),len(op_b))
for index in range(num_digits):
    place = carry
    if index <= len(op_a)-1:
        place = place+base_char_set.index(op_a[index])
    if index <= len(op_b)-1:
        place = place+base_char_set.index(op_b[index])

    if place >= base:
        carry = (place - (place % base))/base
    else:
        carry = 0
    place = place % (base)
    total = total + base_char_set[place]
if carry > 0:
    total = total + base_char_set[carry]

total = total[::-1]
print " "*(len(line)-len(total)) + total
