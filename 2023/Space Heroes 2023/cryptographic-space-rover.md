# Cryptographic Space Rover
**Category:** Crypto

**Points:** 473

**Solved By:** Apicius

## Challenge
>NASA has sent this custom program off to a remote space rover, luckily it already had Python and all the dependencies installed so we don't have to worry about transferring those. It will print the CPU usage and some fun other facts about the system when it's run. It seems to run an equal number of time to the number of characters entered. For some reason, certain characters at certain indexes cause new processes to spawn... can you help us find what characters to avoid at certain indexes?
>
>*Author: teeman22*

Files: `nasa_crypto.py`

## Solution

This was for sure my favorite challenge of the competition, as I got to do some cool scripting.

Reading `nasa_crypto.py` reveals how we have to solve the challenge: brute force guessing.

```python
def main():
    session_uuid = uuid.uuid4()
    flag = open('flag.txt', 'r').readline().strip('\n').lower()
    logo(session_uuid)

    print("Please enter characters:: ")
    user_guess = input().lower().strip("\n")

    for i in range(0, len(flag)):
        if i+1 > len(user_guess):
            print_top(guess=None, uuid=session_uuid)
            exit(-1)
        elif (user_guess[i] != flag[i]):
            print_top(guess=False, uuid=session_uuid)
        else:
            print_top(guess=True,uuid=session_uuid)

    if user_guess == flag:
        print(f"Thanks; we'll avoid these characters: {flag}")

if __name__ == "__main__":
    main()
```

The main function prompts the user for a guess of the flag. It then loops along the flag and checks whether the guessed character at that location is the same as the flags. If it isnt, it passes guess=False. If it is, it passes guess=True. If the user guess is too short, it passes nothing and then exits the program.

Checking the print_top function we can see our returned indicator for if the guess is correct:

```python
def get_dashes(perc):
    dashes = "|" * int((float(perc) / 10 * 4))
    empty_dashes = " " * (40 - len(dashes))
    return dashes, empty_dashes

def print_top(guess, uuid):
    cat_check = 0
    if(guess == True):
        setproctitle.setproctitle(str(uuid))
        setproctitle.setthreadtitle(str(uuid))

    print(f"top - {str(datetime.timedelta(seconds=psutil.boot_time()))}")
    percs = psutil.cpu_percent(interval=0, percpu=True)
    for cpu_num, perc in enumerate(percs):
        dashes, empty_dashes = get_dashes(perc)
        line = " CPU%-2s [%s%s] %5s%%" % (cpu_num, dashes, empty_dashes, perc)
        print(line)

    virtual_memory = psutil.virtual_memory()
    print(f"MiB Swap :\t{virtual_memory.total / 1024 / 1024:.2f} total\t{virtual_memory.free / 1024 / 1024:.2f} free\t{virtual_memory.used / 1024 / 1024:.2f} used\t{virtual_memory.active / 1024 / 1024:.2f} active")
    swap_memory = psutil.swap_memory()
    print(f"MiB Swap :\t{swap_memory.total / 1024 / 1024:.2f} total\t{swap_memory.free / 1024 / 1024:.2f} free\t{swap_memory.used / 1024 / 1024:.2f} used")

    listOfProcessNames = []
    for proc in psutil.process_iter():
        pInfoDict = proc.as_dict(attrs=['pid', 'username', 'cpu_percent', 'memory_percent', 'status', 'name']) # Get process detail as dictionary
        listOfProcessNames.append(pInfoDict) # Add to list

    print(f'{"PID":>6}{"USER":>10}{"%CPU":>6}{"%MEM":>6}{"STATUS":>15}{"NAME":>45}')
    for elem in listOfProcessNames:
        print(f'{elem["pid"]:>6}{elem["username"]:>10}{elem["cpu_percent"]:>6}{elem["memory_percent"]:>6.2f}{elem["status"]:>15}{elem["name"]:>45}')

    if (guess == True):
        setproctitle.setproctitle("python3")
        setproctitle.setthreadtitle("python3")
```

When guess is true, it sets the proc title to be the uuid that was set in the main function. Knowing this, we can check the output and count how many uuids to see how many characters we got correct. I wrote a script to do this, and then send the guess to the remote server.

```python
from pwn import * 
context.log_level = 'error'

def send_guess(flag):
    r = remote("spaceheroes-cryptographic-space-rover.chals.io", 443, ssl=True, sni="spaceheroes-cryptographic-space-rover.chals.io")
    for i in range(0,26):
        if i == 8:
            uuid = (r.recvline()).decode().strip().replace(" ", "").replace("|","")
        else:
            r.recvline()

    r.sendline(flag.encode())
    
    count = 0
    while True:
        try:
            line = r.recvline().decode()
            if uuid in line:
                count+=1
        except:
            break
    print(f"{count} - {flag}")
    if count >= len(flag):
        return flag
    r.close()
    return None    

initflag = "shCTF{"
asciiString = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

while True:
    for char in asciiString:
        flag = initflag+char
        flag = send_guess(flag)
        if flag is not None:
            initflag = flag
            continue
```

This script loops through all ascii characters, and then uses those to progressively guess the flag. It checks to see if the current guess is right by checking the number of uuids printed out. To make it easier, I silenced all output from the actual program and just let it guess.

![image](https://user-images.githubusercontent.com/17153535/233864578-554dd32b-a776-4441-a35c-d66ad6b51110.png)


**Flag:** `shCTF{MET30RS_4R3NT_aS_b4D_4S_sL0W_cpu}`