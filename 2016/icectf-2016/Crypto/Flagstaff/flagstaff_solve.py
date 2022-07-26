#!/usr/bin/python

from pwn import *
import base64
import binascii

def connect():
    #return remote('localhost', 6003)
    return remote('flagstaff.vuln.icec.tf', 6003)

def decrypt(s):
    r = connect()
    r.recvuntil('command: ')
    r.sendline('decrypt')
    r.recvuntil('decrypt:')
    r.sendline(base64.b64encode(s))
    ret = r.recvline().strip()
    r.close()
    return base64.b64decode(ret)

def getflag():
    s = '\x00' * 32
    base = decrypt(s)
    desired = b'flag' + '\x00' * 12
    assert(len(desired) == 16)
    s2 = strxor(base, desired) + s[16:]

    print decrypt(s2)

    r = connect()
    r.recvuntil('command: ')
    r.sendline('secret')
    r.recvuntil('command: ')
    r.sendline(base64.b64encode(s2))
    ret = r.recvline().strip()
    r.close()

    return decrypt(base64.b64decode(ret))


def strxor(a, b):
    return ''.join(chr(ord(ac) ^ ord(bc)) for ac, bc in zip(a, b))

print getflag()
