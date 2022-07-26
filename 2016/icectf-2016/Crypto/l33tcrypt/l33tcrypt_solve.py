#!/usr/bin/python

from pwn import *
import base64
import binascii
import time
import string
import subprocess
import sys

context.log_level = 'ERROR'

MAGIC_WORD = "l33tserver please"

def crypt(s):
    """Contact the l33tserver to encrypt the string.

    Base64-encodes the input string and sends it to the server to be encrypted.
    Base64-decodes the response. If the response is empty or not base64
    encoded, just try again forever.
    """
    msg = base64.b64encode(s)+'\n'
    while True:
        r = remote('l33tcrypt.vuln.icec.tf', 6001, timeout=30)
        r.send(msg)
        response = r.recvall()
        try:
            data = base64.b64decode(response.splitlines()[3])
            return data
        except (TypeError, IndexError):
            pass
        finally:
            r.close()

def nccrypt(s):
    """Encrypt the string using netcat instead of libpwn.

    For some reason this was working better for me at one point, so leaving it
    in just in case.
    """
    msg = base64.b64encode(s)+'\n'
    while True:
        popen = subprocess.Popen(['nc', 'l33tcrypt.vuln.icec.tf', '6001'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, _ = popen.communicate(msg)
        try:
            data = base64.b64decode(out.splitlines()[3])
            return data
        except (TypeError, IndexError) as e:
            pass

def pad(text, bs):
    pad_num = (bs - len(text) % bs)
    return text + 'a' * pad_num

base = pad(MAGIC_WORD, 16)


def findbyte(known):
    """Given the known bytes of the flag, find the next byte."""
    known = ''.join(known)

    # Compute a base string of the correct length to test the next byte
    idx = len(known)
    offset = (16 - (len(MAGIC_WORD) + idx + 1) % 16) % 16
    chridx = len(MAGIC_WORD) + offset + idx
    s = MAGIC_WORD + 'a'*offset
    start = chridx - chridx % 16

    # Encrypt a block with a single unknown flag byte, to match the test blocks
    # against
    actual = crypt(s)
    expected = actual[start:start+16]

    # Try all printable characters as the missing byte. Try _ first as it turns
    # out to be common
    for bc in '_' + string.printable:
        s = MAGIC_WORD + 'a'*offset + known + bc
        res = crypt(s)
        if res[start:start+16] == expected:
            return bc

known = list('IceCTF{')
sys.stdout.write(known)
new = ''
while new != '}':
    new = findbyte(known)
    sys.stdout.write(new)
    known.append(new)
print
