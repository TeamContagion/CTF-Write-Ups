>Being said that move instruction is enough to build a complete computer, anyway move on while you can.
>
>[move](move)


The first thing I did was to put this into my vagrant box, run `file` on it, and then execute it.
```bash
$ file move
move: ELF 32-bit LSB  executable, Intel 80386, version 1 (GNU/Linux), statically linked, stripped
$ ./move
Guess a flag: flag
Wrong Flag!
```
Well, that was somewhat expected. Let's look under the hood, shall we? I opened the binary in Binary Ninja and there was not a whole lot of stuff to look at in the assembly. Taking a look at the strings next, I noticed something very helpful: the binary had been packed with UPX Packer.

[![UPX Packer String](alexctf_2017_upx.png)](alexctf_2017_upx.png)

So I took to Google and found the UPX packer version 3.91 that was used to pack this binary (found [here](https://github.com/upx/upx/releases/tag/v3.91)). I downloaded it, extracted the archive, and looked at the usage.
```bash
$ ./upx-3.91-amd64_linux/upx -h
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2013
UPX 3.91        Markus Oberhumer, Laszlo Molnar & John Reiser   Sep 30th 2013

Usage: upx [-123456789dlthVL] [-qvfk] [-o file] file..

Commands:
  -1     compress faster                   -9    compress better
  --best compress best (can be slow for big files)
  -d     decompress                        -l    list compressed file
  -t     test compressed file              -V    display version number
  -h     give this help                    -L    display software license

Options:
  -q     be quiet                          -v    be verbose
  -oFILE write output to 'FILE'
  -f     force compression of suspicious files
  --no-color, --mono, --color, --no-progress   change look

Compression tuning options:
  --brute             try all available compression methods & filters [slow]
  --ultra-brute       try even more compression variants [very slow]

Backup options:
  -k, --backup        keep backup files
  --no-backup         no backup files [default]

Overlay options:
  --overlay=copy      copy any extra data attached to the file [default]
  --overlay=strip     strip any extra data attached to the file [DANGEROUS]
  --overlay=skip      don't compress a file with an overlay

Options for djgpp2/coff:
  --coff              produce COFF output [default: EXE]

Options for dos/com:
  --8086              make compressed com work on any 8086

Options for dos/exe:
  --8086              make compressed exe work on any 8086
  --no-reloc          put no relocations in to the exe header

Options for dos/sys:
  --8086              make compressed sys work on any 8086

Options for ps1/exe:
  --8-bit             uses 8 bit size compression [default: 32 bit]
  --8mib-ram          8 megabyte memory limit [default: 2 MiB]
  --boot-only         disables client/host transfer compatibility
  --no-align          don't align to 2048 bytes [enables: --console-run]

Options for watcom/le:
  --le                produce LE output [default: EXE]

Options for win32/pe, rtm32/pe & arm/pe:
  --compress-exports=0    do not compress the export section
  --compress-exports=1    compress the export section [default]
  --compress-icons=0      do not compress any icons
  --compress-icons=1      compress all but the first icon
  --compress-icons=2      compress all but the first icon directory [default]
  --compress-icons=3      compress all icons
  --compress-resources=0  do not compress any resources at all
  --keep-resource=list    do not compress resources specified by list
  --strip-relocs=0        do not strip relocations
  --strip-relocs=1        strip relocations [default]

Options for linux/elf:
  --preserve-build-id     copy .gnu.note.build-id to compressed output

file..   executables to (de)compress

This version supports:
    AMD64-darwin.macho               Mach/AMD64
    ARMEL-darwin.macho               Mach/ARMEL
    amd64-linux.elf                  linux/ElfAMD
    amd64-linux.kernel.vmlinux       vmlinux/AMD64
    amd64-win64.pe                   win64/pe
    arm-linux.elf                    linux/armel
    arm-linux.kernel.vmlinux         vmlinux/armel
    arm-wince.pe                     arm/pe
    armeb-linux.elf                  linux/armeb
    armeb-linux.kernel.vmlinux       vmlinux/armeb
    armel-linux.kernel.vmlinuz       vmlinuz/armel
    fat-darwin.macho                 Mach/fat
    i086-dos16.com                   dos/com
    i086-dos16.exe                   dos/exe
    i086-dos16.sys                   dos/sys
    i386-bsd.elf.execve              BSD/386
    i386-darwin.macho                Mach/i386
    i386-dos32.djgpp2.coff           djgpp2/coff
    i386-dos32.tmt.adam              tmt/adam
    i386-dos32.watcom.le             watcom/le
    i386-freebsd.elf                 BSD/elf386
    i386-linux.elf                   linux/elf386
    i386-linux.elf.execve            linux/386
    i386-linux.elf.shell             linux/sh386
    i386-linux.kernel.bvmlinuz       bvmlinuz/386
    i386-linux.kernel.vmlinux        vmlinux/386
    i386-linux.kernel.vmlinuz        vmlinuz/386
    i386-netbsd.elf                  netbsd/elf386
    i386-openbsd.elf                 opnbsd/elf386
    i386-win32.pe                    win32/pe
    m68k-atari.tos                   atari/tos
    mips-linux.elf                   linux/mipseb
    mipsel-linux.elf                 linux/mipsel
    mipsel.r3000-ps1                 ps1/exe
    powerpc-darwin.macho             Mach/ppc32
    powerpc-linux.elf                linux/ElfPPC
    powerpc-linux.kernel.vmlinux     vmlinux/ppc32

UPX comes with ABSOLUTELY NO WARRANTY; for details visit http://upx.sf.net
```

So the argument I needed to use was `-d` to decompress.
```bash
$ ./upx-3.91-amd64_linux/upx -d move -o move_unpacked
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2013
UPX 3.91        Markus Oberhumer, Laszlo Molnar & John Reiser   Sep 30th 2013

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
  10308504 <-   2619128   25.41%  netbsd/elf386  move_unpacked

Unpacked 1 file.
```

Now I had an unpacked binary. Turns out that even though this was the correct thing to do, this actually was even worse to look at! Literally every instruction was a `MOV`...?!
[![mov instructions](alexctf_2017_movs_1.png)](alexctf_2017_movs_1.png)

I did some intense googling and found out that this binary was created using a tool called [movfuscator](https://github.com/xoreaxeaxeax/movfuscator). I tried to find a deobfuscator for it, however the only one that I could find did not do any good. So I kept looking and came across an [interesting writeup](http://wiki.yobi.be/wiki/MoVfuscator_Writeup) on movfuscator that had a [tracer program](http://wiki.yobi.be/wiki/MoVfuscator_Writeup#Traces) that would look at 1-byte memory writes using [Intel PIN](https://software.intel.com/en-us/articles/pin-a-binary-instrumentation-tool-downloads). So, I downloaded Intel PIN, compiled the program as instructed, and tried to use it. I also came across [this other CTF writeup](http://www.mma.club.uec.ac.jp/tokyowesterns-writeups/0ctf.html#momo-reverse-3pts) that used the same tool I was using in a CTF context. The way it was using it was to look at the patterns in the 1-byte writes, and see what was happening in response to changes in the input.

I applied this same type of thinking to the output that I was receiving. Since I knew that the flag started with `ALEXCTF{`, I used this to understand the output from the tracer program.

First, I tested using an empty string.
```bash
$ (echo "" | ../../../pin -t obj-ia32/tracer.so -- ../../../../move_unpacked); xxd trace-1byte-writes.bin
Guess a flag: Wrong Flag!
0000000: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000010: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000020: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000030: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000040: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000050: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000060: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000070: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000080: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000090: 0101 0000                                ....
```

Then, I started adding the flag format characters in one at a time and observed the changes.
```bash
$ (echo "A" | ../../../pin -t obj-ia32/tracer.so -- ../../../../move_unpacked); xxd trace-1byte-writes.bin
Guess a flag: Wrong Flag!
0000000: 0000 0100 0101 0000 0101 0000 0101 0000  ................
0000010: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000020: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000030: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000040: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000050: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000060: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000070: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000080: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000090: 0101 0000                                ....

$ (echo "AL" | ../../../pin -t obj-ia32/tracer.so -- ../../../../move_unpacked); xxd trace-1byte-writes.bin
Guess a flag: Wrong Flag!
0000000: 0000 0100 0000 0100 0101 0000 0101 0000  ................
0000010: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000020: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000030: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000040: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000050: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000060: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000070: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000080: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000090: 0101 0000                                ....
```

I noticed that there seemed to be 1 byte for each character in the flag. `0101 0000` indicated an incorrect character, and `0000 0100` indicated a correct character.
I then started to write a script that would do this for me automagically, but realized I had an issue that would make things take a lot longer.
My idea was to simply loop over all characters and check the binary output and see if I had put in a correct character. But what about lowercase vs. uppercase characters?
I had done some preliminary scripting and realized that if I had to check 52 letters + symbols + digits, this would take *a lot* longer than if I could just check lowercase.

Luckily, there was also an output for this!
```bash
$ (echo "Al" | ../../../pin -t obj-ia32/tracer.so -- ../../../../move_unpacked); xxd trace-1byte-writes.bin
Guess a flag: Wrong Flag!
0000000: 0000 0100 0000 0000 0101 0000 0101 0000  ................
0000010: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000020: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000030: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000040: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000050: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000060: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000070: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000080: 0101 0000 0101 0000 0101 0000 0101 0000  ................
0000090: 0101 0000                                ....
```

An output of `0000 0000` indicated the right letter but wrong case. So I then finished my script so that I checked for these cases and brute forced the flag.
Here is my full solution code
```python
from string import ascii_lowercase, digits
import os

allChars = digits + '_}' + ascii_lowercase

flag = 'ALEXCTF{'
wrong = '\x01\x01\x00\x00'
right = '\x00\x00\x01\x00'
case = '\x00\x00\x00\x00'

def tryFlag(f):
    os.system('(echo "{}" | ../../../pin -t obj-ia32/tracer.so -- ../../../../move) > /dev/null'.format(f))
    data = open('trace-1byte-writes.bin', 'rb').read()
    offset = len(f) * 4
    return data[offset - 4:offset]

while flag[:-1] != '}':
    for c in allChars:
        result = tryFlag(flag + c)
        if result == case:
            c = c.upper()
            result = tryFlag(flag + c)
            
        if result == right:
            flag += c
            print flag
            break
```

The resulting flag was `ALEXCTF{M0Vfusc4t0r_w0rk5_l1ke_m4g1c}`