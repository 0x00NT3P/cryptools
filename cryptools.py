#!/usr/bin/env python
import click, os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes

@click.group()
def cryptools():
    pass

@cryptools.command()
@click.option('--key', required=True, help="key value")
@click.option('--message', required=True, help="text to encrypt")
@click.pass_context
def encrypt(ctx, key, message):
    messageBytes = message.encode('utf-8')
    keyBytes = key.encode('utf-8')
    ivBytes = os.urandom(16)

    #cipher = Cipher(algorithms.AES(keyBytes), modes.CBC(ivBytes))
    # cipher = Cipher(algorithms.AES(keyBytes), modes.ECB())
    cipher = Cipher(algorithms.AES(keyBytes), modes.OFB(ivBytes))

    # Agregar padding
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(messageBytes) + padder.finalize()

    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()

    hex_text = ct.hex().upper()
    print(f"IV : {ivBytes.hex().upper()}")
    print(f"Encrypted (hex): {hex_text}")

@cryptools.command()
@click.option('--key', required=True, help="user's name")
@click.option('--iv', required=True, help="iv value")
@click.option('--cryptogram', required=True, help="cryptogram to decrypt")
@click.pass_context
def decrypt(ctx, key, iv, cryptogram):
    ciphertext = bytes.fromhex(cryptogram)
    keyBytes = key.encode('utf-8')
    ivBytes = bytes.fromhex(iv)

    # Crear cifrador AES CBC
    #cipher = Cipher(algorithms.AES(keyBytes), modes.CBC(ivBytes))
    cipher = Cipher(algorithms.AES(keyBytes), modes.ECB())
    decryptor = cipher.decryptor()

    # Descifrar y quitar padding
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Quitar padding PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(decrypted_padded) + unpadder.finalize()

    print("Decrypted:", plaintext.decode())

@cryptools.command()
@click.option('--file', required=True, help="file path")
@click.pass_context
def md5(ctx, file):
    f = open(file, 'rb+')
    data = f.read()

    digest = hashes.Hash(hashes.MD5())
    digest.update(data)
    ct = digest.finalize()
    print(f"MD5 (hex): {ct.hex()}")

if __name__ == '__main__':
    cryptools()
