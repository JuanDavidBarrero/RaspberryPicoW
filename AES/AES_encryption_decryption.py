from ucryptolib import aes
import ujson
import random

person = {"name":"Juan","Pet":"Hades","Job":True}

#iv = byte_array = bytearray([0] * 16)
iv = bytes([random.randint(0, 255) for _ in range(16)])
key =  bytes([random.randint(0, 255) for _ in range(32)])

crypto = aes(key,1,iv)
data = ujson.dumps(person)
data_bytes = data.encode()

block_size = 16
padding_size = block_size - (len(data_bytes) % block_size)
padding = b'\x00' * padding_size
padded_data = data_bytes + padding
enc = crypto.encrypt(padded_data)

print(f"the encrypt message is \n \t{enc.hex()} \n")

data_enc = enc.hex()
byte_str = bytes.fromhex(data_enc)

crypto2 = aes(key,1,iv)
dec = crypto2.decrypt(byte_str)

print(f"the decrypt message is \n \t {dec.decode('utf-8')}")