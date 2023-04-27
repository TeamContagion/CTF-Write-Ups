# I've got the same combination on my luggage!
**Category:** Crypto

**Points:** 205

**Solved By:** Apicius

## Challenge
>During the Battle for Druidia, the Spaceballs were able to obtain the code for the Druidia shield gate: 12345. Fortuantely, the Spaceballs had lost that battle, and Druidia lived to breathe another day. However, these security breaches were concerning and so Druidia decided to up their security. This is where you, Spaceballs' top mathematician, comes into play. We are making yet another ploy for Druidia's fresh air, and we need your help figuring out their password. We have obtained the hash of the new combination as well as the algorithm which generated the hash, which we have supplied to you. Find that combination, the fate of Planet Spaceball rests in your hands!

> NOTE: The "combination" will be in flag format, i.e. shctf{...}
>
>*Author: monkey_noises*

Files: `hash.txt, luggage_combination.py`

## Solution

The problem gives us a 'hash' of length 240 and a function that derives that hash.

Hash: `783f3977627a693a320f313e421e29513e036e485565360a172b00790c211a7b117b4a7814510b2d4b0b01465448580a0369520824294c670c3758706407013e271b624934147f1e70187c1c72666949405c5b4550495e5e02390607217f11695a61587c6351536b741d301d6d182c48254e7f4927683d19`

Code:
```python
from pwn import *

plaintext = b'****************************************'
key1 = b'****************************************'
key2 = b'****************************************'

def shield_combination(p, k1, k2):
	A = xor(p, k1, k2)
	B = xor(p, k1)
	C = xor(p, k2)
	return A + B + C

print(shield_combination(plaintext, key1, key2).hex())
```

This code shows that the hash is simply a combination of xor(p,k1,k2), xor(p,k1), and xor(p,k2). Because the xor was used multiple times, this challenge is easily solvable. First, we should split the flag into it's three component parts:

```
flag
a = "783f3977627a693a320f313e421e29513e036e485565360a172b00790c211a7b117b4a7814510b2d" 
b = "4b0b01465448580a0369520824294c670c3758706407013e271b624934147f1e70187c1c72666949" 
c = "405c5b4550495e5e02390607217f11695a61587c6351536b741d301d6d182c48254e7f4927683d19"
```

Then with this, we can derive the keys by using chunk A in reverse. We xor A with B, and that gives us key2, and we xor A with C, and that gives us key1. From here, all we have to do is plug it into xor(p,k1,k2) and we get the flag.

![image](https://user-images.githubusercontent.com/17153535/233865036-b07772ce-bbfc-44a3-9411-9c7a2a1b42a1.png)

**Flag**: `shctf{on3_e1GHt_hUnDR3d_D-R-U-I-D-I-A__}`