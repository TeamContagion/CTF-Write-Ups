#!/usr/bin/env python

import bencode
import hashlib

# First open the file and use a library to decode it
f = open('flag.torrent')
data = f.read()
f.close()
decoded = bencode.bdecode(data)

print decoded
# {'announce': '127.0.0.1',
#  'created by': 'mktorrent 1.0',
#  'creation date': 1448521489,
#  'info': {'length': 28,
#           'name': 'flag',
#           'piece length': 2,
#           'pieces': "Tk\x05\x90\x97 ...long string... \xf4\xe1\xf5D"}}

# We observe that "piece length" is set to 2, meaning that each piece is only 2
# bytes long. We have the hashes of each of these 2-byte pieces. Since there
# are only 2^16 possible pieces, we can compute all the possible hashes and
# recover the pieces.

pieces = decoded['info']['pieces']

# The pieces element is the concatenation of all of the SHA1 hashes of the
# pieces. Separate the 160-bit hashes into a list.
piecehashes = []
i = 0
while i < len(pieces):
    piecehashes.append(pieces[i:i+20])
    i += 20

# Iterate through all possible two-byte strings and compute the SHA1 hash to
# build a reverse mapping.
hashes = {}
for b1 in range(256):
    for b2 in range(256):
        s = chr(b1) + chr(b2)
        h = hashlib.sha1(s).digest()
        hashes[h] = s

# Read out the result
print ''.join(hashes[h] for h in piecehashes)
