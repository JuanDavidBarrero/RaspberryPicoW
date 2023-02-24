from ucryptolib import aes
import ujson

person = {"name":"Juan","Pet":"Hades","Job":True}

crypto = aes(b"hola mundo hades",1)
data = ujson.dumps(person)
data_bytes = data.encode()

enc = crypto.encrypt(data_bytes + b'\x00' * ((16 - (len(data_bytes) % 16)) % 16))
print(f"the encrypt message is \n \t{enc.hex()} \n")

data_enc = enc.hex()
byte_str = bytes.fromhex(data_enc)


crypto2 = aes(b"hola mundo hades",1)
dec = crypto2.decrypt(byte_str)

print(f"the decrypt message is \n \t {dec.decode('utf-8')}")