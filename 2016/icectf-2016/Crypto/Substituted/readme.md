# Substitute (Crypto - 30 Points,  1217 solves)

> We got a substitute flag, I hear they are pretty lax on the rules... [crypted.txt](https://play.icec.tf/problem-static/crypted_a888cc3cc9e064482ab8b61d0b19ca0b1b1ce88238c63f03c306d33947cf113b.txt) seems awfully suspicious, do you think you can figure out what they're hiding?

Solution
--------

'''
Lw!

Gyzvecy ke WvyVKT!

W'zz by reso dsbdkwksky tzjq teo kly ujr. Teo keujr, gy joy dksurwmq bjdwv vorakeqojalr jmu wkd jaazwvjkwemd. Vorakeqojalr ljd j zemq lwdkeor, jzklesql gwkl kly juxymk et vecaskyod wk ljd qekkym oyjzzr vecazwvjkyu. Decy dwcazy ezu vwalyod joy kly Vjydjo vwalyo, kly Xwqymyoy vwalyo, kly dsbdkwkskwem vwalyo, glwvl wd klwd emy, jmu de em. Jzcedk jzz et klydy vwalyod joy yjdwzr boeiym keujr gwkl kly lyza et vecaskyod. Decy myg ymvorakwem cykleud joy JYD, kly vsooymk dkjmujou teo ymvorakwem, jzemq gwkl ODJ. Vorakeqojalr wd j xjdk twyzu jmu wd xyor wmkyoydkwmq klesql. De iwvi bjvi, oyju sa em decy veez vwalyod jmu ljxy tsm!

El jmu teo reso oyveoud cr mjcy wd WvyVKT{jzgjrd_zwdkym_ke_reso_dsbdkwksky_tzjqd}.
'''

We are given subsitution text and need to find out the cipher.

A very good online tool to help you crack the ciphertext is [Crypto Club](http://www.cryptoclub.org/tools/cracksub_topframe.php)'s Substitution Cipher Cracker.

This is a easy enough subsitution cipher that frequency analysis is not necessary.

Since we know the flag format is icectf{xxxxxx} we can quickly identify some letters as shown:

W = I
V = C
Y = E
V = C (Redundent for Completeness)
K = T
T = F

So by solving 5 of 26 letters the plaintext so far looks like this:

'''
i'    e          tit te f    f   t e    . f   t    ,  e   e  t   i      ic c   t            it      ic ti   . c   t                    i t   ,   t       it  t e    e t  f c    te   it       tte   e     c    ic te .    e  i   e     ci  e     e t e c e    ci  e , t e  i e e e ci  e , t e     tit ti   ci  e ,   ic  i  t i    e,          .      t      f t e e ci  e     e e  i       e  t      it  t e  e    f c    te  .    e  e  e c   ti    et       e  e , t e c   e t  t       f   e c   ti  ,        it     . c   t        i       t fie       i   e   i te e ti   t     .     ic    c ,  e            e c    ci  e          e f  !

       f         ec           e i  icectf{      _ i te _t _    _    tit te_f    }.
'''

After comparing the ciphertext to the plaintext you can start to identify small words. After a short while trying some letters and comparing the strings to the english langauge you should arrive at (or at least enough to get the flag):

'''
i'll be your substitute flag for the day. for today, we are studying basic cryptography and its applications. cryptography has a long history, although with the advent of computers it has gotten really complicated. some simple old ciphers are the caesar cipher, the vigenere cipher, the substitution cipher, which is this one, and so on. almost all of these ciphers are easily broken today with the help of computers. some new encryption methods are aes, the current standard for encryption, along with rsa. cryptography is a vast field and is very interesting though. so kick back, read up on some cool ciphers and have fun!

oh and for your records my name is icectf{always_listen_to_your_substitute_flags}.
'''

Flag: 'icectf{always_listen_to_your_substitute_flags}'

