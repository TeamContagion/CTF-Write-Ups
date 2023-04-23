# Welcome to the World of Tomorrow
**Category:** Crypto

**Points:** 235

**Solved By:** Apicius

## Challenge
>Good news everyone! We have been tasked with deciphering a secret message from a less than friendly group of aliens! We know that they use the results of the popular "_Alien Wordle_" game as a key for their daily encryption method, that they love old human ciphers, and we got a copy of their game in progress. The bad news is, none of us can read alienese. Can you figure out the message?

>Submit the result like this: shctf{decrypted_text_here}
>
>*Author: Cody*

Files: `Alien_Wordle.png, cipher.txt`

## Solution

The first thing I did with this challenge was check the Alien_Wordle.png image.

![image](https://user-images.githubusercontent.com/17153535/233865199-e02268ad-ae78-4730-87de-541662d6ea14.png)

Knowing that this challenge is Futurama themed, I searched for a Futurama alien language cipher. This allowed me to decode this image with the final row of the wordle being: `STAR__S_`. This means that the expected answer for the Wordle is STARDUST. 

With cipher.txt being `trt3_db_mz1gq_fekdf_x1ty`, and the challenge description saying that the aliens liked old ciphers, I decided to throw it into vigenere. Lo and behold, that popped the flag.

![image](https://user-images.githubusercontent.com/17153535/233865201-ad9f5f9c-bf9b-472b-a67d-558cecee4675.png)

![image](https://user-images.githubusercontent.com/17153535/233865207-4b987cda-facb-4929-99dd-c0d4fb758c40.png)

**Flag**: `shctf{byt3_my_sh1ny_metal_flag}`