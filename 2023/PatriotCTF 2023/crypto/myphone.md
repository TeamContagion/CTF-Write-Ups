# My Phone!
**Category:** Crypto

**Points:** 100 (beginner)

**Solved By:** Gido, sy1vi3

## Challenge
>Some weird triangle man stole my phone, he taunted me by sending me his location but it seems to be encrypted with some odd cipher I've never seen before, could you please help me get my phone back?

>Flag format: PCTF{city_name}

>Author: @txnner


Files: 

![cipher.png](https://github.com/gidoBOSSftw5731/CTF-Write-Ups/blob/pctf2023-myphone/2023/PatriotCTF%202023/crypto/myphonepics/cipher.png)

## Solution

This crypto challenge was fairly straightforward, where you were given a photo with ciphertext. First, it was immediately obvious (thanks to sy1vi3 for this) that it was a set of coordinates for a location, due to the two periods and comma along with the context from the question.

Once that was figured out, it was also determined (via scrolling through https://dcode.fr, thanks to 0xk7 for the pointer on where to look) to be using the Gravity Falls Bill Cipher.

![FOURSIX.SEVENSIXEIGHT,-NINETWO.ONETWOFOUR](https://raw.githubusercontent.com/gidoBOSSftw5731/CTF-Write-Ups/pctf2023-myphone/2023/PatriotCTF%202023/crypto/myphonepics/dcodrfr.png "FOURSIX.SEVENSIXEIGHT,-NINETWO.ONETWOFOUR")

At this point, it was pretty trivial to plug these in to Google Maps (thanks sy1vi3 for doing it before I finished the deciphering) and read which city came back. 

![46.768,-92.124 Duluth](https://raw.githubusercontent.com/gidoBOSSftw5731/CTF-Write-Ups/pctf2023-myphone/2023/PatriotCTF%202023/crypto/myphonepics/gmaps.png "46.768,-92.124 Duluth")

At this point, we have the answer for the flag.

**Flag:**  `PCTF{duluth}`
