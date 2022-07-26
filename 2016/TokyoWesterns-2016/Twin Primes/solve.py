#!/usr/bin/python
from Crypto.Util.number import *
import Crypto.PublicKey.RSA as RSA
import gmpy2

with open('key1', 'r') as f:
    n1 = long(f.read().splitlines()[0])
with open('key2', 'r') as f:
    n2 = long(f.read().splitlines()[0])
with open('encrypted', 'r') as f:
    m = long(f.read().splitlines()[0])

s = (n2 - n1 - 4L) / 2L

# p^2 - sp + n1 = 0
# Apply quadratic formula:
a = 1
b = -s
c = n1

p = long((-b + gmpy2.isqrt(b*b-4*a*c))/2L)
q = n1/p

assert p*q == n1
assert (p+2)*(q+2) == n2

e = long(65537)
d1 = inverse(e, (p-1)*(q-1))
d2 = inverse(e, (p+1)*(q+1))
key1 = RSA.construct((n1, e, d1))
key2 = RSA.construct((n2, e, d2))
m = key2.decrypt(m)
m = key1.decrypt(m)
m = long_to_bytes(m)

end = m.index('}')
print m[:end+1]
