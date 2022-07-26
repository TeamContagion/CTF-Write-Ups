# Contract (Crypto - 130 pts)

> Our contractors stole the flag! They put it on their file server and
> challenged us to get it back. Can you do it for us? `nc contract.vuln.icec.tf
> 6002` [server.py](server.py). We did intercept someone connecting to the
> server though, maybe it will help. [contract.pcapng](contract.pcapng)

Solution
--------

This server accepts a command and a signature, separated by a `:`. If the signature is not valid, the command is rejected. Three commands are available: `help`, `time`, and `read`. We would like to use the `read` command to read the flag from a file on the server's disk, but we will need a valid signature.

The included PCAP shows two successful commands:
```
help:c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156cfd7287caf75247c9a32e52ab8260e7ff1e46e55594aea88731bee163035f9ee31f2c2965ac7b2cdfca6100d10ba23826
time:c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156c0cbebcec222f83dc9dd5b0d4d8e698a08ddecb79e6c3b35fc2caaa4543d58a45603639647364983301565728b504015d
```

We can confirm that these signatures are correct by submitting them to the server:
```
# echo help:c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156cfd7287caf75247c9a32e52ab8260e7ff1e46e55594aea88731bee163035f9ee31f2c2965ac7b2cdfca6100d10ba23826 | nc contract.vuln.icec.tf 6002

COMMANDS:
* read [file]
 - prints contents of file
* time
 - prints the current time
* help
 - prints this message

# echo time:c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156c0cbebcec222f83dc9dd5b0d4d8e698a08ddecb79e6c3b35fc2caaa4543d58a45603639647364983301565728b504015d | nc contract.vuln.icec.tf 6002
2016-08-29 19:25:31
```

ECDSA signatures actually consist of two components, `r` and `s`. Each time a
signature is generated, the signer is supposed to choose a random integer `k`,
compute the elliptic curve point `(x1, y1) = k * G`, then find `r = x1 mod n`.
Because the value of `k` is random, every signature should have a different `r`
value.  However, if we look at the two signatures we have, we see that the
first 48 bytes of the signature are the same!

This is a serious error in usage of ECDSA, because from two signatures computed
with the same value of `k`, it is possible to compute the value of `k` used,
and from that the private key, as follows:
```
z1 = sha256('help')
(r, s1) = signature for 'help'
z2 = sha256('time')
(r, s2) = signature for 'time'

k = (z1 - z2) * (s1 - s2)^-1
d = (s1 * k - z1) * r^-1
```
Wikipedia has a
[good writeup](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm#Signature_generation_algorithm)
on this weakness of improperly-used ECDSA.

The resulting `d` is the secret exponent of the private key, so now we have all
the components of the key and can use an ECDSA library to generate signatures
for any string we want, including 'read \<filename\>'.

[contract_solve.py](contract_solve.py) implements this technique. It takes an
argument of the filename to read, and requests that file from the server. We
only have to request flag.txt to get the flag:
```
# ./contract_solve.py flag.txt | nc contract.vuln.icec.tf 6002
IceCTF{a_f0rged_signatur3_is_as_g00d_as_a_real_1}
```
