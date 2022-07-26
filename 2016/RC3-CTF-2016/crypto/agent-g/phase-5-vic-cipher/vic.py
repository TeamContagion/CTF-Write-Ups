import string


class Grid(object):
    def __init__(self, keyword, spaces, alphabet=string.ascii_lowercase + "./"):
        if keyword:
            self.keyword = keyword
        else:
            self.keyword = alphabet[:8]
        self.spaces = sorted(spaces)
        self.alphabet = alphabet
        remaining = sorted(list(set(alphabet) - set(self.keyword)))

        self.grid = [
            [str(n) for n in range(10)],
            list(self.keyword),
            remaining[:10],
            remaining[10:],
        ]

        for space in self.spaces:
            self.grid[1].insert(space, " ")

        self.lookup = {}
        for ch in alphabet:
            if ch in self.grid[1]:
                self.lookup[ch] = ("", 1)
            elif ch in self.grid[2]:
                self.lookup[ch] = (str(spaces[0]), 2)
            elif ch in self.grid[3]:
                self.lookup[ch] = (str(spaces[1]), 3)
            else:
                raise ValueError("Grid not large enough for entire alphabet")

    def __str__(self):
        out = ""
        for row in self.grid:
            for col in row:
                out += col + " "
            out += "\n"
        return out

    def encode(self, message):
        encoded = ""
        for ch in message:
            if ch in self.lookup:
                locator = self.lookup[ch]
                encoded += locator[0] + str(self.grid[locator[1]].index(ch))
            else:
                raise ValueError("Character '%s' not in alphabet (%s)" % (ch, self.alphabet))

        return encoded

    def encode_with_key(self, message, key):
        if not key.isdigit():
            raise ValueError("Key must be digital")
        encoded = self.encode(message)

        to_add = key * (len(encoded) // len(key) + 1)

        final = ""

        for c, k in zip(encoded, to_add):
            final += str((int(c) + int(k)) % 10)

        return final

    def decode(self, ciphertext):
        decoded = ""
        index = 0
        for ch in ciphertext:
            ch = int(ch)
            if ch in self.spaces and index == 0:
                index = self.spaces.index(ch) + 1
            else:
                decoded += self.grid[index + 1][ch]
                index = 0

        return decoded

    def decode_with_key(self, ciphertext, key):
        if not key.isdigit():
            raise ValueError("Key must be digital")

        to_add = key * (len(ciphertext) // len(key) + 1)
        print(to_add)
        final = ""

        for c, k in zip(ciphertext, to_add):
            delta = int(c) - int(k)
            final += str(delta % 10)

        print(final)

        return self.decode(final)


plain = """take.care.of.this.problem....39.553469,-119.864375,39.158076,-119.787425,43.485954,25.716452,34.260902,-88.766856,31.300248,131.078382,47.772447,-116.829302,41.199670,-80.486106,42.244626,-71.003112,42.120352,-76.900029,40.718361,-73.936826,42.424801,-84.527512,-22.659735,14.565248,53.814100,-3.055051,51.353292,0.503093,40.524943,-112.248105"""
alphabet = ",-.0123456789abcefhiklmoprst"
g = Grid("", (3, 6), alphabet)
print(g)
print(g.encode(plain))
encoded = g.encode_with_key(plain, "1948")

n = 5
for s in [encoded[i:i+n] for i in range(0, len(encoded), n)]:
    print(s, end= ' ')
