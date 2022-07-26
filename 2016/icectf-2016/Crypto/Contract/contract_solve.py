#!/usr/bin/python

import binascii
import hashlib
import sys
from ecdsa import numbertheory, util
from ecdsa import VerifyingKey, SigningKey

PUBLIC_KEY = """
-----BEGIN PUBLIC KEY-----
MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEgTxPtDMGS8oOT3h6fLvYyUGq/BWeKiCB
sQPyD0+2vybIT/Xdl6hOqQd74zr4U2dkj+2q6+vwQ4DCB1X7HsFZ5JczfkO7HCdY
I7sGDvd9eUias/xPdSIL3gMbs26b0Ww0
-----END PUBLIC KEY-----
"""
vk = VerifyingKey.from_pem(PUBLIC_KEY.strip())

msg1 = 'help'
sig1 = binascii.unhexlify('c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156cfd7287caf75247c9a32e52ab8260e7ff1e46e55594aea88731bee163035f9ee31f2c2965ac7b2cdfca6100d10ba23826')
msg2 = 'time'
sig2 = binascii.unhexlify('c0e1fc4e3858ac6334cc8798fdec40790d7ad361ffc691c26f2902c41f2b7c2fd1ca916de687858953a6405423fe156c0cbebcec222f83dc9dd5b0d4d8e698a08ddecb79e6c3b35fc2caaa4543d58a45603639647364983301565728b504015d')

r = util.string_to_number(sig1[:48])
s1 = util.string_to_number(sig1[48:])
z1 = util.string_to_number(hashlib.sha256(msg1).digest())
s2 = util.string_to_number(sig2[48:])
z2 = util.string_to_number(hashlib.sha256(msg2).digest())

k = (z1 - z2) * numbertheory.inverse_mod(s1 - s2, vk.pubkey.order) % vk.pubkey.order
d = (s1 * k - z1) * numbertheory.inverse_mod(r, vk.pubkey.order) % vk.pubkey.order

sk = SigningKey.from_secret_exponent(d, curve=vk.curve, hashfunc=hashlib.sha256)

msg3 = 'read %s' % sys.argv[1]
print '%s:%s' % (msg3, binascii.hexlify(sk.sign(msg3, k=k)))
