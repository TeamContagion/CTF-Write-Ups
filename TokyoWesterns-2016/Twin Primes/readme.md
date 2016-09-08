# Twin Primes - Crypto, 50 Points

## Problem

The [encrypt.py](encrypt.py) program generates four primes in two twin prime
pairs (`p` and `p+2`, `q` and `q+2`). It then constructs two RSA keys from
them, key1 with modulus `p*q`, key2 with modulus `(p+2)*(q+2)`. The files in
the directory contain the public parts of key1 and key2, and the encryption of
the flag first with key1, then with key2.

## Solution

While it is normally difficult to factor large numbers, by giving us these two
related moduli the problem creators have made it easy, we only have to do some
algebra:

```
n1 = pq
n2 = (p+2)(q+2) = pq + 2p + 2q + 4
n2 - n1 = 2p + 2q + 4
let s = (n2 - n1 - 4)/2 = p + q
```

So, we can substitute into the original equations:
```
q = (s - p)
n1 = p(s-p) = ps - p^2
p^2 - sp + n1 = 0
```

Now we have a quadratic equation that we can solve, giving us `p` and `q`. From
these we can use the same code as encrypt.py to construct RSA decryption keys
and decrypt the message.

[solve.py](solve.py) implements this solution.

```
# ./solve.py
TWCTF{3102628d7059fa267365f8c37a0e56cf7e0797ef}
```
