# Reverse Box - Reversing, 50 Points

See [solve.py](solve.py) for annotated solution.

```
# gdb ./reverse_box -x solve.py
GNU gdb (Debian 7.11.1-2) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./reverse_box...(no debugging symbols found)...done.
Breakpoint 1 at 0x80485b1

Breakpoint 1, 0x080485b1 in ?? ()
[Inferior 1 (process 46371) exited normally]

Breakpoint 1, 0x080485b1 in ?? ()
[Inferior 1 (process 46375) exited normally]

<snip>

Breakpoint 1, 0x080485b1 in ?? ()
[Inferior 1 (process 46377) exited normally]

Breakpoint 1, 0x080485b1 in ?? ()
[Inferior 1 (process 46587) exited normally]
seed is 214
Breakpoint 2 at 0x80486db
Breakpoint 3 at 0x80486e0

Breakpoint 2, 0x080486db in ?? ()

Breakpoint 1, 0x080485b1 in ?? ()

Breakpoint 3, 0x080486e0 in ?? ()
[Inferior 1 (process 46588) exited normally]
TWCTF{5UBS717U710N_C1PH3R_W17H_R4ND0M123D_5-B0X}
(gdb) q
```
