# This code for AES algorithm using genetic algothm functions

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os,random
import main_genalgo
import base64
    
class aes_algo:

    # Encrypt plaintext
    def encrypt(plaintext,cipher):
        # # Create a padder for PKCS7 padding
        padder = padding.PKCS7(128).padder()
        # Pad the plaintext
        padded_data = padder.update(plaintext) + padder.finalize()
        
        # Create an encryptor object
        encryptor = cipher.encryptor()

        # Encrypt the padded data
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        return ciphertext

    # Decrypt ciphertext
    def decrypt(ciphertext,cipher):
        # Create an unpadder for PKCS7 padding
        unpadder = padding.PKCS7(128).unpadder()
        # Create a decryptor object
        decryptor = cipher.decryptor()
        # Decrypt the ciphertext
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        # Unpad the decrypted data
        plaintext = unpadder.update(padded_data) + unpadder.finalize()

        return plaintext
def main(plain_text):
    # Generate a random 128-bit AES key
    key0 = os.urandom(16)
    key = main_genalgo.gen_algo.genetic_algorithm((key0.decode('cp1252')))
    
    # Generate a random initialization vector (IV)
    iv = b'\xf6a\x17\x13\xb9b\x08\xa2\x99\xd0\x91\xbd\xbd\xe7(\x9c'
    # Create an AES cipher object with CBC mode genetic algorithm key
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    # plain_text = input("Enter the plain text: ")
    encrypted_text = aes_algo.encrypt(plain_text.encode(),cipher)
    decrypted_text = aes_algo.decrypt(encrypted_text,cipher)
    
    print("Plaintext:", plain_text)
    print("AES key: ",key0)
    print("AES key with genetic algo: ",key.decode('cp1252'))
    print("Encrypted data with genetic algo key: ",encrypted_text)
    print("Decrypted data:", decrypted_text)
    


flag = True
try:
    main(plain_text="Hello world")
except:
    flag = False
while(flag == False):
    try:
        main(plain_text="Hello world")
        flag = True
    except:
        flag = False