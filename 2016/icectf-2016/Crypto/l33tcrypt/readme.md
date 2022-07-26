# l33tcrypt (Crypto - 90 pts)

> l33tcrypt is a new and fresh encryption service. For added security it pads all information with the flag! Can you get it?

Solution
--------

Looking at `server.py`, we see that the server accepts a base64-encoded input:
```
data = recvline(req).strip()
try:
    data = base64.b64decode(data)
```

checks to make sure it begins with the "magic word":
```
if not data.startswith("l33tserver please"):
```

then pads it and encrypts it with AES and an unknown key:
```
c = AESCipher(KEY).encrypt(pad(data, 16))
```

The padding is the interesting part. The code first appends the flag:
```
def pad(text, bs):
    text = text + FLAG
```
then adds a number of padding bytes (1-16 bytes, never 0) to bring it to a multiple of 16:
```
    pad_num = (bs - len(text) % bs)
    return text + chr(pad_num) * pad_num
```

Next we [note](https://github.com/dlitz/pycrypto/blob/9e2b6af8c34efba80d141490b48b82a3c2185ae5/lib/Crypto/Cipher/blockalgo.py#L356)
that pycrypto's block ciphers are used in ECB mode by default.  That is, each
16-byte block of the input is encrypted individually with the key, with no
interaction between blocks. We can use this fact to reveal the flag, one byte
at a time.

The input must begin with 'l33tserver please'. Suppose we ask l33tserver to
encrypt the 31 bytes of data: 'l33tserver pleaseaaaaaaaaaaaaaa'. The server
will add the flag and pad it out to a multiple of 16 bytes. We will use F's to
represent the unknown bytes of the flag, and X's to represent the extra
padding:
```
l33tserver pleas|eaaaaaaaaaaaaaaF|FFFXXXXXXXXXXXXX
```
Now we know that the second block of the output is the encryption of
'eaaaaaaaaaaaaaa' plus the first byte of the flag.

Now we can brute-force the first byte of the flag. Say we want to try the byte 'q'. Then we ask the server to encrypt 'l33tserver pleaseaaaaaaaaaaaaaaq':
```
l33tserver pleas|eaaaaaaaaaaaaaaq|FFFFXXXXXXXXXXXX
```
If the second block of the output equals the second block computed earlier, then the guess was correct and 'q' is the first byte of the flag. Once we have one byte correct, we can work on the second byte. We get the expected block by encrypting 
```
l33tserver pleas|eaaaaaaaaaaaaaFF|FFXXXXXXXXXXXXXX
```
Then, we can see if the second byte is 'z' by encrypting
```
l33tserver pleas|eaaaaaaaaaaaaaqz|FFFFXXXXXXXXXXXX
```
Once again, if the second block matches, we found the correct byte. We keep
trying bytes until we find one that matches. This process continues until we
successfully find the end of the flag. See
[l33tcrypt_solve.py](l33tcrypt_solve.py) for code that executes this attack.
