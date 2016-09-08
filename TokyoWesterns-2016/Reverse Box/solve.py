#!/usr/bin/python

import gdb
import tempfile

# We know that the following string was produced by the binary when the flag
# was given as input
desired = '95eeaf95ef94234999582f722f492f72b19a7aaf72e6e776b57aee722fe77ab5ad9aaeb156729676ae7a236d99b1df4a'
# The binary looks up the bytes of the input in a lookup table and returns the
# bytes found there. However, the lookup table is randomized, so our task is to
# find the correct table. We know the flag begins with 'TWCTF', so if we
# encrypt that string the beginning of the output should match.
desired_prefix = desired[:len('TWCTF')*2]

seed_set = '*0x80485b1'  # Instruction after the seed for the table has been chosen
before_build = '*0x80486db'  # instruction just before calling the table build function
after_build = '*0x80486e0'  # instruction just after table build function returns

# Disable all existing breakpoints so we can predict where we will stop
for bp in gdb.breakpoints() or []:
    bp.enabled = False

my_bps = []
my_bps.append(gdb.Breakpoint(seed_set))

gdb.execute('set pagination off')

# Iterate through the possible seeds (1 to 255, because it is ANDed with 0xff
# and 0 is not accepted) to find the one that matches
outfile = tempfile.NamedTemporaryFile()
for seed in range(1,256):
    # Run program sending output to outfile
    gdb.execute('run TWCTF{foo} > %s' % outfile.name)
    # Just after seed is randomly chosen by program, overwrite it with our
    # selection
    gdb.execute('set $eax = %d' % seed)
    gdb.execute('continue')
    # Read the program output and see if it matches our desired encryption of
    # 'TWCTF'
    outfile.seek(0)
    out = outfile.read()
    if out.startswith(desired_prefix):
        print 'seed is %d' % seed
        break
outfile.close()

# Now we need to capture the lookup table generated from this seed
my_bps.append(gdb.Breakpoint(before_build))
my_bps.append(gdb.Breakpoint(after_build))

gdb.execute('run TWCTF{foo} > /dev/null')
# Figure out where the lookup table is stored
stack = gdb.parse_and_eval('(unsigned char **)$esp')
lookup = stack.dereference()
gdb.execute('continue')
# override seed
gdb.execute('set $eax = %d' % seed)
gdb.execute('continue')

# Table has been constructed, read it out byte by byte into a reverse lookup
# dict
table = {}
for i in range(256):
    table[int(lookup[i])] = i

# Clean up gdb state
for bp in my_bps:
    bp.delete()

gdb.execute('continue')

# Iterate through the desired output, looking up the bytes in the table
vals = []
i = 0
while i < len(desired):
    byte = int(desired[i:i+2], 16)
    val = table[byte]
    vals.append(val)
    i += 2

print ''.join(chr(x) for x in vals)
