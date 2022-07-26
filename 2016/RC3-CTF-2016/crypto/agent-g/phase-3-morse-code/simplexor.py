key = "thereisnomeaninginthismessagedonotseekforoneyouwillfailwhyareyouevendecodingthiswowwhatawasteoftimeyouregoingtorunoutoftimeatthisratetrololo"
plaintext = """Agent G: Awesome Work!
Encoded payload uses this alphabet: ,-.0123456789abcefhiklmoprst
http://ctf.greggernaut.com/its-just-a-one-time-thing"""

print(len(key))
print(len(plaintext))


def do_chunk(key_chunk, plain_chunk):
    image = ''
    for ch_cover, ch_plain in zip(key_chunk, plain_chunk):
        image += chr(ord(ch_cover.upper()) ^ ord(ch_plain))
    chunk = ":".join("{:02x}".format(ord(c)) for c in image)
    return chunk.upper()


chunk_size = 14
i = 0
while len(key) > 0:
    key_chunk = key[:chunk_size]
    plain_chunk = plaintext[:chunk_size]
    key = key[chunk_size:]
    plaintext = plaintext[chunk_size:]
    print(i)
    i += 1
    print(key_chunk)
    print(do_chunk(key_chunk, plain_chunk))
    print(plain_chunk)
    print('-' * chunk_size)
