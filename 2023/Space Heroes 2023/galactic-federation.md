# Galactic Federation
**Category:** Reverse Engineering

**Points:** 221

**Solved By:** Apicius

## Challenge
>After escaping galactic federal prison, you (the legendary Rick Sanchez) have just given yourself Level 9 access to the federation headquarters. Now, you must break into their computer systems and find a way to topple the galactic government.
>
>*Author: monkey_noises*

Files: `galactic_federation.bin`

## Solution

When this program is opened we first get a login page. Guess I need to check if passwords are coded into the binary...

![image](https://user-images.githubusercontent.com/17153535/233864688-2c649a3f-f73b-40f9-9c41-43cfc3751f60.png)

Opening it in Ghidra, we can see the username and password hardcoded in the binary as strings, with a simple obfuscate function running on it in order to make it slightly more annoying to steal.

![image](https://user-images.githubusercontent.com/17153535/233864696-d769214d-f7dd-410c-bace-ef16aa6de61f.png)

```C
#include <stdio.h>
#include <string.h>
int main() {
	char password[] = "hktpu"; 
	for (int i = 0; i < strlen(password); i++) {
		char out = password[i]-'\a';
		printf("%c", out);
	}
}
```

I rewrote the inverse of the simple obfuscate in C, and got the username and password from it:

`username: admin`
`password: 1_l0v3_wR4ngL3r_jE4nS`

With this username and password we can start our search for the flag. Theres a fairly suspicious function called collapse_economy(), and that seems to be what we want to get. The function where collapse_economy() is called checks for two conditions: that the value of the currency is 0, and that the currency is called "usd."

![image](https://user-images.githubusercontent.com/17153535/233864716-e4f2c028-dd83-41d6-8e43-f8bf3c1097ef.png)

The line `currency = currency + (local_60/100) * currency` can be easily taken advantage of by just passing -100 in as our variable so that it sets the currency to be currency + -currency. Then, in another portion of the admin console we can simply change the currency type to USD. We're then given the flag after we collapse the economy.

![image](https://user-images.githubusercontent.com/17153535/233864783-38b30c1d-3f35-4504-b581-51e56946df38.png)

**Flag**: `shctf{w4it_uH_wh0s_P4y1Ng_m3_2_y3L1_@_tH15_gUy?}`