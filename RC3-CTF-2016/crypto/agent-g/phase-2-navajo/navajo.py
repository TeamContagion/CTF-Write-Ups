import base64

NAVAJO = {
    '2': "naaki",
    '3': "tááʼ",
    '4': "dį́į́ʼ",
    '5': "ashdlaʼ",
    '6': "hastą́ą́",
    '7': "tsostsʼid",
    "A": "Wóláchííʼ",
    "B": "Shash",
    "C": "Mósí",
    "D": "Bįįh",
    "E": "Dzeeh",
    "F": "Mąʼii",
    "G": "Tłʼízí",
    "H": "Łį́į́ʼ",
    "I": "Tin",
    "J": "Téliichoʼí",
    "K": "Tłʼízí yázhí",
    "L": "Dibé yázhí",
    "M": "Naʼastsʼǫǫsí",
    "N": "Neeshchʼííʼ",
    "O": "Néʼéshjaaʼ",
    "P": "Bisóodi",
    "Q": "kʼaaʼ yeiłtįįh",
    "R": "Gah",
    "S": "Dibé",
    "T": "Tązhii",
    "U": "Nóódaʼí",
    "V": "Akʼehdidlíní",
    "W": "Dlǫ́ʼii",
    "X": "Ałnáʼázdzoh",
    "Y": "Tsáʼásziʼ",
    "Z": "Béésh dootłʼizh",
    "=": "="
}

by_length = sorted(NAVAJO.items(), key=lambda x: len(x[1]), reverse=True)

def encode(s):
    b32 = base64.b32encode(bytes(s, 'ascii'))
    print(str(b32, 'ascii'))
    navajo = ""
    for ch in b32:
        navajo += NAVAJO[chr(ch).upper()] + " "


    return navajo.strip()

def decode(s):
    plain = ""
    while s:
        found = False
        for letter, word in by_length:
            if s.startswith(word):
                s = s[len(word)+1:]
                plain += letter
                found = True
                break
        if not found:
            raise ValueError("Invalid start word %s" % s)

    plain = base64.b32decode(plain)

    return str(plain, 'ascii')


message = "Agent G:  Well done!  We knew you would be a perfect candidate for this mission.  You will soon receive an encrypted blob.  The spaces will be in positions 3 and 6.  Good luck.  http://ctf.greggernaut.com/sam-tso-sends-his-regards"
encoded = encode(message)
decoded = decode(encoded)
print(message)
print(encoded)
print(decoded)

