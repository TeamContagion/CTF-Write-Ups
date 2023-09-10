# Guardians-of-the-Galaxy
**Category:** Reverse Engineering

**Points:** 231

**Solved By:** Apicius

## Challenge
>Only those who know the password can unlock the power of the system. But be warned, the password is as elusive as the Guardians themselves - **hidden in the depths of Xandar or floating in the vastness of Knowhere.**

>Are you ready to take on the challenge and prove yourself a true Guardian? Remember, as Groot would say, **'I am Groot'** is not the password you are looking for.
>
>*Author: bl4ckp4r4d1s3*

Files: `guardians_of_the_galaxy.bin`

## Solution

This reverse engineering challenge required that you send a properly formatted 'password' to the program in order to get the flag. However, it would seem that the password *is* the flag.

![image](https://user-images.githubusercontent.com/17153535/233864817-c840676c-fc03-4240-8653-38b7dcb0265c.png)

We're first prompted with an enter password screen. This doesn't do us much good so I opened it in Ghidra like any responsible reverse engineer-er.

Inside the main function there is some logic to check whether the password you entered is correct. First it checks if the password is 27 characters long, then checks if certain parts of it are equal to certain strings. These strings look suspicious, though.

![image](https://user-images.githubusercontent.com/17153535/233864840-138536e5-4709-4233-aa86-9f80107f19cf.png)

When observing the code closely, the atox and r functions are performing operations on the 3 substrings of the flag and then checking to see if you've entered it properly. These can be easily reversed by seeing how the functions work.

![image](https://user-images.githubusercontent.com/17153535/233864852-f3731db7-7444-4b6e-8193-8b42644d4ed5.png)

![image](https://user-images.githubusercontent.com/17153535/233864862-da4264b9-e1f8-47d3-9394-5e455e697cc0.png)

For the function r, it seems that the characters are having four subtracted from their value. This can be simply reversed by just doing the opposite: adding four. With atox on the other hand, all it's doing is converting the string to hex. If we reverse these and recombine them, we get the flag.

![image](https://user-images.githubusercontent.com/17153535/233864876-ff472cc5-92ec-4dc9-b720-9eb6c3e34f69.png)

**Flag:**  `shctf{5ky_1s_n0t_th3_l1m1t}`