# Vocaloid Heardle
**Category:** Misc

**Points:** 325

**Solved By:** Apicius

## Challenge
>Well, it’s just too usual to hide a flag in stegano, database, cipher, or server. What if we decide to sing it out instead?
>
>*Author: pamLELcu*

Files: `flag.mp3`, `vocaloid_heardle.py`

## Solution

Before looking at the python script, I thought I'd first give `flag.mp3` a listen. Upon listening to it, it seems that it's spliced together vocaloid songs of about 3 seconds in length each, with the whole file being 33 seconds long.

Next up was to check out the script. I went through the script and added comments detailing what it was doing in order to properly understand it. 

```python
import requests
import random
import subprocess

resources = requests.get("https://sekai-world.github.io/sekai-master-db-diff/musicVocals.json").json()

def get_resource(mid):
    # Gets the resource number (assetbundlename) for the unicode character
    print(f"Mid: {mid}")
    return random.choice([i for i in resources if i["musicId"] == mid])["assetbundleName"]

# Downloads with mid=unicode character at that location in the flag array
def download(mid):
    # Gets the resource for that unicode character
    resource = get_resource(mid)
    # Gets the file for the unicode character and downloads it 
    r = requests.get(f"https://storage.sekai.best/sekai-assets/music/short/{resource}_rip/{resource}_short.mp3")
    filename = f"tracks/{mid}.mp3"
    print(f"Filename: {filename}")
    with open(filename, "wb") as f:
        f.write(r.content)
    return mid

# Opens the flag.txt file and reads it
with open("flag.txt") as f:
    flag = f.read().strip()

# Checks to see if the flag starts with sekai and ends with braces
assert flag.startswith("SEKAI{") and flag.endswith("}")
# Gets only the value of the flag in order to parse it into music 
flag = flag[6:-1]
# Downloads songs for each unicode character in the flag
tracks = [download(ord(i)) for i in flag]

# Combines all of the tracks together
inputs = sum([["-i", f"tracks/{i}.mp3"] for i in tracks], [])
filters = "".join(f"[{i}:a]atrim=end=3,asetpts=PTS-STARTPTS[a{i}];" for i in range(len(tracks))) + \
          "".join(f"[a{i}]" for i in range(len(tracks))) + \
          f"concat=n={len(tracks)}:v=0:a=1[a]"

subprocess.run(["ffmpeg"] + inputs + ["-filter_complex", filters, "-map", "[a]", "flag.mp3"])
```

The function of this script is to take a file `flag.txt` and encode it into unicode characters, fetch a song with an ID that matches the unicode character, and then add the first three seconds of it to the `flag.mp3` file.

Rather than coming up with a fancy way to do this, I solved it using a rather simple method. I created a file named `flag.txt`, supplied unicode characters 33 through 126, and then ran the program. This gave me a folder full of tracks with the title being a number that corresponds with a unicode character. From here I split `flag.mp3` into 11 parts, and then listened to each song and matched it with a unicode character. The resulting characters being:

`[118, 48, 67, 97, 108, 111, 73, 100, 60, 51, 117]`

When I took these numbers and converted them to ASCII I was given the flag.

**Flag:** `SEKAI{v0CaloId<3u}`

