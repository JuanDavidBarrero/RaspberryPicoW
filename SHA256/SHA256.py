import hashlib

hashObj = hashlib.sha256()

hashObj.update(b"Hades lobo blanco")

rst = hashObj.digest()

print(rst.hex())