from decimal import *
from matrix import *

getcontext().prec = 500

f = open("encrypted")
curr = eval(f.read())
f.close()

n = len(curr)
r = Decimal(0.5)

matrix = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    if i == 0:
        matrix[i] = [2 + 2 * r, -r] + [Decimal(0)] * (n - 2)
    elif i == n - 1:
        matrix[i] = [Decimal(0)] * (n - 2) + [-r, 2 + 2 * r]
    else:
        matrix[i] = [Decimal(0)] * (i - 1) + [-r, 2 + 2 * r, -r] + [Decimal(0)] * (n - i - 2)

matrix2 = [[Decimal(0) for x in range(n)] for y in range(n)]
matrix2[0][0] = Decimal(1)
matrix2[n-1][n-1] = Decimal(1)
for i in range(1,n-1):
    matrix2[i][i-1] = r
    matrix2[i][i+1] = r
    matrix2[i][i] = Decimal(1)

inv2 = invert(matrix2)

# a[0] = o[0]
# a[1] = .5o[0] + o[1] + .5o[2]
# a[2] = .5o[1] + o[2] + .5o[3]
# a[3] = .5o[2] + o[3] + .5o[4]
# a[4] = .5o[3] + o[4] + .5o[5]
# a[5] = o[5]

for step in range(100):
    temp = mult(matrix, curr)
    curr = mult(inv2, temp)

ans = [chr(int(round(elem))) for elem in curr]
print ''.join(ans)
