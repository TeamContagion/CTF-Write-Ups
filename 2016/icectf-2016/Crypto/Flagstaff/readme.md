# Flagstaff (Crypto - 120 pts)

> Someone hid his flag here... guess we better give up.

Solution
--------
Let's look at the server to see what it can do. It accepts four commands, two of which seem interesting:
* decrypt: Decrypts the input data.
* secret: Accepts an encrypted command and executes it. One of the accepted
  commands returns the flag, encrypted.

So it looks like we'll need to convince the server to give us the encrypted
flag, then pass that to the decrypt command to get the plaintext. But how do we
execute the secret 'flag' command when it needs to be sent in encrypted form?

Let's take a closer look at how the decryption is done. The block cipher is used in CBC mode, with the IV provided as the first block of the message:
```
iv = enc[:self.bs]
enc = enc[self.bs:]
cipher = AES.new(self.key, AES.MODE_CBC, iv)
dec = cipher.decrypt(enc)
```
Looking closely at the
[formulas for CBC decryption](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_Block_Chaining_.28CBC.29),
we see that:
```
Pi = D(Ci) ^ Ci-1
C0 = IV
```

Thus, P1 = D(C1) ^ IV

This means that the "plaintext" block the server will interpret as a command is
controlled by two components - the decryption of the provided ciphertext block,
and the IV. The decrypted block is impossible for us to control without the
key, but the IV is completely under our control! So, if we find the decryption
of some arbitrary block, we can select an IV that XORs into it to produce
exactly the plaintext we're hoping for.

So what plaintext do we have to produce?
```
handlers = {
    b"encrypt": encrypt,
    b"flag": flag
}

data = recvline(req).strip()
data = AESCipher(KEY).decrypt(data)

for cmd, func in handlers.iteritems():
    if cmd in data:
        func(req)
        break
```
We want the 'flag' function to be called, so we need the text 'flag' to be in
the decrypted data. So, we're aiming to produce a plaintext block including the
4 bytes 'flag'. The steps to do this are:

1. Get the decryption of an all-zeros data block with an all-zeros IV.
2. XOR the desired text ('flag') into the result, use that as the new IV.
3. Try decrypting this ciphertext with the new IV to check it comes out
   containing 'flag'.
4. Send this ciphertext as an encrypted command in response to the 'secret'
   command. Receive an encrypted flag as the output.
5. Use the 'decrypt' command to decrypt the flag.

A script that solves this challenge is provided in
[flagstaff_solve.py](flagstaff_solve.py).
