# Use the Force

## Setup
This challenge presents the user with a page with one input and the text:
> To find the flag, *Use The Force*... and also the [source](./app.py).

## Obfuscation
The important part of the source is:
```python
def check(text):
    import base64, operator, itertools, zlib
    R = ('eJw1i0sKwzAMRHuULmXwpRTbYIM/QlZoEubwdVoyi4H3mHm9UccnKXaR1bVMQ2PB0Ihp'
         'iqsIuFbMfUMY3bj0iZYsjxiWXxdNktjWmPU+hrwmqG2AJWLrAWoZx3khklH3QkqVGg1/'
         'OOe80bbUjYFOR0zztn++Hv7lCwJAPlc=')
    A = zlib.decompress(base64.b64decode(R)).decode().split('|')
    D = dict(itertools.chain(*(zip(A[i+15], operator.attrgetter(*A[3*i+3:3*i+6])(x))
        for i,x in enumerate((AttrDict(__builtins__), AttrDict(__builtins__), operator, itertools)))))
    try: return not eval(A[20], D, dict(zip(A[19], A[:3]), s=text))
    except: return False
```
We must provide an input `text` that makes this function return `True`.

The values (R, A, D) do not depend on the input, so we can run these lines in
an interpreter to get the values used in that final call to `eval`:
```python
In [177]: D
Out[177]:
{u'a': str,
 u'b': <function operator.sub>,
 u'c': operator.methodcaller,
 u'd': <function all>,
 u'h': itertools.chain,
 u'l': list,
 u'm': <function map>,
 u'n': <function operator.contains>,
 u'o': <function ord>,
 u'p': <function zip>,
 u'r': itertools.repeat,
 u't': itertools.starmap}

In [209]: dict(zip(A[19], A[:3]), s="mytext")
Out[209]: {'s': 'mytext', u'x': u'\x00 ', u'y': u'lower', u'z': u'upper'}

In [148]: A[20]
Out[148]: u'd(t(n,p(r(l(m(o,x))),t(b,p(m(o,c(y)(a(s))),m(o,c(z)(a(s))))))))'
```

To find out what this code is actually doing, we can use string substitution to expand the references in `A[20]`. First we construct a dict with the strings to replace with:
```python
mapping = {
	'a': 'str',
	'b': 'sub',
	'c': 'methodcaller',
	'd': 'all',
	'h': 'itertools.chain',
	'l': 'list',
	'm': 'map',
	'n': 'contains',
	'o': 'ord',
	'p': 'zip',
	'r': 'itertools.repeat',
	't': 'itertools.starmap',
	u'x': "'\x00 '",
	u'y': "'lower'",
	u'z': "'upper'"
}
```

Then we construct the replaced string:
```python
s = ''
for c in A[20]:
    if c in mapping:
        s += mapping[c]
    else:
        s += c
```

Once we clean up the formatting and replace some `methodcaller` invocations
with actual method calls, we get:
```python
all(
  itertools.starmap(
    operator.contains,
    zip(
      itertools.repeat([0,32]),
      itertools.starmap(
        operator.sub,
        zip(s.lower(), s.upper())))))
```

This code goes through each character in the string, subtracting the numerical
value of that character's upper() from its lower(). If for all the characters
in the string this returns 0 or 32, this expression returns True (and the check
fails). So, we need to find a character whose upper() is neither 0 nor 32 away
from its lower(). Unfortunately, none of the ASCII characters fit the bill, but
this program is using unicode, so if we expand our search a bit we can find
one:

```python
allchars = ''.join(unichr(c) for c in range(256*10))
up = allchars.upper()
down = allchars.lower()
matches = [(unichr(i), d) for i, d in
    enumerate([ord(downc) - ord(upc) for upc, downc in zip(up, down)])
    if d not in [0, 32]]
print matches[-1][0]
```

In this way we find out that, among others, the unicode character ֆ (Armenian
Small Letter Feh, who knew!) has a difference of 48 from its uppercase version.
We enter the character into the website and receive the flag.
