modulo = 1000000007
def gcd(a, b):
    if a == 0:
        return b
    elif a % 2 == 0 and b % 2 == 0:
        return 2 * gcd(a / 2, b / 2)
    elif a % 2 == 0 and b % 2 != 0:
        return gcd(a / 2, b)
    elif a % 2 != 0 and b % 2 == 0:
        return gcd(a, b / 2)
    else:
        if a < b:
            a, b = b, a
        return gcd((a - b) / 2, b)
n = int(input())
for i in range(n):
    q, a, b = list(map(int, input().strip().split()))
    s = 0
    for j in range(a, b + 1):
        if int(gcd(q, j)) == 1:
            s += j
    print(s % modulo)
