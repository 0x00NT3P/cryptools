#!/usr/bin/env python
import click
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

@click.group()
def cryptools():
    pass

@cryptools.command()
@click.option('--key', required=True, help="key value")
@click.option('--iv', required=True, help="iv value")
@click.option('--message', required=True, help="text to encrypt")
@click.pass_context
def encrypt(ctx, key, iv, message):

    messageBytes = message.encode('utf-8')
    ivBytes = iv.encode('utf-8')
    keyBytes = key.encode('utf-8')

    cipher = Cipher(algorithms.AES(keyBytes), modes.CBC(ivBytes))

    # Agregar padding
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(messageBytes) + padder.finalize()

    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()

    hex_text = ct.hex().upper()
    print(f"Encrypted (hex): {hex_text}")

@cryptools.command()
@click.option('--key', required=True, help="user's name")
@click.option('--iv', required=True, help="iv value")
@click.option('--cryptogram', required=True, help="cryptogram to decrypt")
@click.pass_context
def decrypt(ctx, key, iv, cryptogram):
    # Clave (32 bytes → AES-256)
    keyBytes = key.encode('utf-8')

    # IV fijo de 16 bytes (¡para pruebas!)
    ivBytes = iv.encode('utf-8')

    ciphertext = bytes.fromhex(cryptogram)

    # Crear cifrador AES CBC
    cipher = Cipher(algorithms.AES(keyBytes), modes.CBC(ivBytes), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descifrar y quitar padding
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Quitar padding PKCS7
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(decrypted_padded) + unpadder.finalize()

    print("Decrypted:", plaintext.decode())


if __name__ == '__main__':
    cryptools()
