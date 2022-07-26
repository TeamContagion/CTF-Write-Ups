#!/usr/bin/python
from Crypto.Cipher import AES
from Crypto import Random
import SocketServer as ss
import signal
import base64


from secret import KEY, FLAG

PORT = 6003


class AESCipher:
    def __init__(self, key):
        assert(len(key) == 32)
        self.key = key
        self.bs = AES.block_size

    def unpad(self, text):
        """PKCS7 unpad"""
        last_byte = ord(text[-1:])
        if last_byte > self.bs:
            return text
        if text[-last_byte:] != chr(last_byte) * last_byte:
            return text
        return text[:-last_byte]

    def pad(self, text):
        """PKCS7 pad"""
        pad_num = (self.bs - len(text) % self.bs)
        return text + chr(pad_num) * pad_num

    def encrypt(self, raw):
        """Encrypt using AES in CBC mode."""
        raw = self.pad(raw)
        iv = Random.new().read(self.bs)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        """Decrypt using AES in CBC mode. Expects the IV at the front of the string."""
        enc = base64.b64decode(enc)
        iv = enc[:self.bs]
        enc = enc[self.bs:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        dec = cipher.decrypt(enc)
        return self.unpad(dec)


def hello(req):
    req.sendall(b"Hello World!\n")


def admin(req):
    print("Admin requested!")  # Ring bell


def decrypt(req):
    req.sendall("Send me some data to decrypt: ")
    data = recvline(req).strip()
    p = AESCipher(KEY).decrypt(data)
    req.sendall(base64.b64encode(p) + "\n")


def secret(req):
    def encrypt(req):
        req.sendall("Send me some data to encrypt: ")
        data = recvline(req).strip()
        c = AESCipher(KEY).encrypt(data)
        req.sendall(base64.b64encode(c) + "\n")

    def flag(req):
        # secure the flag
        data = AESCipher(KEY).encrypt(FLAG)
        req.sendall(data + "\n")

    handlers = {
        b"encrypt": encrypt,
        b"flag": flag
    }

    req.sendall("Send me an encrypted command: ")
    data = recvline(req).strip()
    data = AESCipher(KEY).decrypt(data)

    for cmd, func in handlers.iteritems():
        if cmd in data:
            func(req)
            break


handlers = {
    "hello": hello,
    "admin": admin,
    "decrypt": decrypt,
    "secret": secret
}


def recvline(req):
    buf = b""
    while not buf.endswith(b"\n"):
        buf += req.recv(1)
    return buf


class RequestHandler(ss.BaseRequestHandler):
    def handle(self):
        req = self.request

        signal.alarm(5)

        req.sendall("Welcome to the secure flag server.\n")
        req.sendall("Send me a command: ")
        data = recvline(req).strip()
        for cmd, func in handlers.iteritems():
            if cmd in data:
                func(self.request)
                break
        req.close()


class TCPServer(ss.ForkingMixIn, ss.TCPServer):
    pass


ss.TCPServer.allow_reuse_address = True
server = TCPServer(("0.0.0.0", PORT), RequestHandler)

print("Server listening on port %d" % PORT)
server.serve_forever()
