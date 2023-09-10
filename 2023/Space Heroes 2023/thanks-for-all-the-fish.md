# Thanks for all the Fish
**Category:** Reversing

**Points:** 248

**Solved By:** Apicius

## Challenge
> *Welcome, human, to the 42nd centennial dolphin acrobatics show! Better get to it. These dolphins aren't going to train themselves...**
>
>*Author: Curtíco*

Files: `thanks4allthefish (ELF Binary)`

## Solution

I'm personally a big fan of the Hitchhikers Guide to the Galaxy series, so I'm happy to see a challenge like this.

![hitchhikersguidetothegalaxy-dolphin](https://user-images.githubusercontent.com/17153535/233865152-253c4576-873d-46d5-b626-08069a56d304.gif)

![image](https://user-images.githubusercontent.com/17153535/233865158-15222ba7-8944-48de-9a27-09d9ad6c243e.png)

Running the program ends up just causing it to exit again, likely because the conditions to get the flag have not been fulfilled. Opening it in Ghidra, we can see some of these conditions.

![image](https://user-images.githubusercontent.com/17153535/233865163-cec8f066-8e67-4f47-94f9-f6721aeff57f.png)

It seems to be checking what program is running it based on the `snprintf` statement checking `proc/getppid()/comm`. It doesn't like that it's being run by bash, and would rather be run by tidbits.

I wrote a quick bash script that just calls the binary. When we run it with tidbits, it then starts to do tricks! 

```bash
#!/bin/bash
./tidbits
```

![image](https://user-images.githubusercontent.com/17153535/233865169-9b006c27-cb0c-440f-a7af-5f06c67363d3.png)

It doesn't like that we ran out of tidbits for it, and we can see this in the code.

![image](https://user-images.githubusercontent.com/17153535/233865174-7bd8186c-28df-43c1-a797-d41b99f3bcd5.png)

It wants to have 5 tidbits in /proc/\*/comm. To get this, I simply wrote another script called tidbits with an infinite loop in it, and then ran `./tid/tidbits&` four times, and then ran the script again. This then got us our flag, and showed us the most intelligent creature on the planet. Sucks to get only third place.

![image](https://user-images.githubusercontent.com/17153535/233865180-579c0aed-1537-46cc-b4bc-ea1641c51497.png)

**Flag:** `shctf{0k_but_h4v3_y0u_s33n_th3_m1c3}`
