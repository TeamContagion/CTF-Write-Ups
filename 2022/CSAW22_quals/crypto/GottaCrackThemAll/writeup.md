# Gotta Crack Them All

**Category:** Cryptography

**Points:** 64

**Solved By:** Chandi95

## Challenge

> As an intern in the security department, you want to show the admin what a major security issue there is by having all passwords being from a wordlist (even if it is one the admin created) as well as potential issues with stream ciphers. Here's the list of encrypted passwords (including the admin's), the encryption algorithm and your password. Can you crack them all and get the admin's password? Here is the web service that the admin made to encrypt a password: `nc crypto.chal.csaw.io 5002`
>
> NOTE: The flag is just the admin's password.

Files: `encrypt.py`, `leaked_password.txt`, `encrypted_passwords.txt`

## Solution

As the challenge description above states, we are given the encryption algorithm (`encrypt.py`), our own password (`leaked_password.txt`), and the list of encrypted passwords (`encrypted_passwords.txt`). Let's see how the encryption algorithm works:

```python
with open('key.txt','rb') as f:
    key = f.read()

def encrypt(plain):
    return b''.join((ord(x) ^ y).to_bytes(1,'big') for (x,y) in zip(plain,key))
```

First, the encryption key is read in from a file. The `encrypt` function may look a bit confusing, but all it's doing is taking each byte of the plaintext and XOR'ing it with a byte in the key (The `^` symbol means XOR in Python). If there's more plaintext bytes than the length of the key, then the key is repeated. These bytes are then joined together to represent the ciphertext. Knowing the encryption scheme, how are we going to crack the list of passwords?

The answer lies in the properties of XOR. XOR is a logic operator and stands for "eXclusive OR". It returns true only if its arugments are different (ex. false, true returns true). One property of XOR is that it's self-inverting, so if you apply the key to the ciphertext with XOR you get the plaintext. Another interesting property of XOR is that it's associative:

```
A ^ (B ^ C) = (A ^ B) ^ C
```

We know that the plaintext is XORed with the key to produce the ciphertext. We also know that the ciphertext, when XORed with the key, gives us the plaintext. So what happens when we XOR the plaintext and the ciphertext? Well, due to the properties of XOR, we will recover the key!

We 