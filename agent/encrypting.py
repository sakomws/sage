from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode

def encrypt_message(public_key_file, hashed_message):
    with open(public_key_file, "rb") as f:
        public_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_rsa.encrypt(hashed_message.encode('utf-8'))
    return b64encode(ciphertext).decode('utf-8')

def decrypt_message(private_key_file, encrypted_message):
    with open(private_key_file, "rb") as f:
        private_key = RSA.import_key(f.read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    ciphertext = b64decode(encrypted_message.encode('utf-8'))
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext.decode('utf-8')

# Paths to the public and private key files
# public_key_file = "public.pem"
# private_key_file = "private.pem"


# # Encrypt the message
# encrypted_message = encrypt_message(public_key_file, message)
# print("Encrypted message:", encrypted_message)

# # Decrypt the message
# decrypted_message = decrypt_message(private_key_file, encrypted_message)
# print("Decrypted message:", decrypted_message)