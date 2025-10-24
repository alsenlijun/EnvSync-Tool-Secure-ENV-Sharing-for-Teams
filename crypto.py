from cryptography.fernet import Fernet

def _derive(key):
    return Fernet(key.ljust(32, '0')[:32].encode())

def encrypt_file(path, key):
    f = _derive(key)
    data = open(path, "rb").read()
    enc = f.encrypt(data)
    open(path + ".enc", "wb").write(enc)
    print(f"Encrypted -> {path}.enc")

def decrypt_file(path, key):
    f = _derive(key)
    data = open(path, "rb").read()
    dec = f.decrypt(data)
    out = path.replace(".enc","")
    open(out, "wb").write(dec)
    print(f"Decrypted -> {out}")
