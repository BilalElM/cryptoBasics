from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import scrypt
from hashlib import sha3_512

# 521 na officiële statement van Crystal zelf die aanradend dat je curves gebruikt van minsten 512.
# veel hededaagse encryptie modellen ondersteunden geen hogere encryptie modellen die meer dan 256 zijn.

private_key = ECC.generate(curve='P-521')
public_key = private_key.public_key()


shared_key = sha3_512(public_key.export_key(format='DER')).digest()
print(shared_key)

aes_key = scrypt(shared_key, b'salt', 16, N=2**14, r=8, p=1)
print(aes_key)

message = "Quantum computers hate this simple trick."
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())


cipher_aes_dec = AES.new(aes_key, AES.MODE_EAX, nonce=cipher_aes.nonce)
decrypted_message = cipher_aes_dec.decrypt_and_verify(ciphertext, tag)

print("encrypted:", ciphertext)
print("decrypted:", decrypted_message.decode())
