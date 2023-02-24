from ucryptolib import aes
import ujson

person = {"name":"Juan","Pet":"Hades","Job":True}

crypto = aes(b"hola mundo hades",1)
data = ujson.dumps(person)
data_bytes = data.encode()

block_size = 16
padding_size = block_size - (len(data_bytes) % block_size)
padding = b'\x00' * padding_size
padded_data = data_bytes + padding
enc = crypto.encrypt(padded_data)

print(f"the encrypt message is \n \t{enc} \n")

data_enc = enc.hex()
byte_str = bytes.fromhex(data_enc)

crypto2 = aes(b"hola mundo hades",1)
dec = crypto2.decrypt(byte_str)

print(f"the decrypt message is \n \t {dec.decode('utf-8')}")