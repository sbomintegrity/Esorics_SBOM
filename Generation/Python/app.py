from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))
    return cipher.nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext.decode('utf-8')

if __name__ == "__main__":
    key = get_random_bytes(16)  # AES-128 bit key
    plaintext = "Hello from PyCryptodome!"

    print("Original message:", plaintext)

    nonce, ciphertext, tag = encrypt(plaintext, key)
    print("\nEncrypted message:", ciphertext.hex())

    decrypted = decrypt(nonce, ciphertext, tag, key)
    print("\nDecrypted message:", decrypted)
