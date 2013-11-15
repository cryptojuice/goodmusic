""" Create base64 encode Scrypt hashes and random salts
"""
import sys
import scrypt
import base64
from os import urandom

PYTHON3 = sys.version_info >= (3, 0)

def enbase64(byte_str):
    """
    Encode bytes to base64
        Args:
            byte_str : bytes to encode

    """
    return base64.b64encode(byte_str)


def debase64(byte_str):
    """
    Decode base64 encoded bytes
        Args:
            byte_str : bytes to decode
    """
    if PYTHON3 and isinstance(byte_str, str):
        string = bytes(byte_str, 'utf-8')
    return base64.b64decode(byte_str)


def generate_hash(password, salt):
    """ Returns a base64 encoded password hash

        Args:
            password (str): Password string
            salt : Random base64 encoded string
    """
    password = password.encode('utf-8')
    scrypt_hash = scrypt.hash(password, salt)
    return enbase64(scrypt_hash)


def generate_random_salt(length=64):
    """ Generate random salt
        Args:
            length (int): The length of salt to return. default = 64
    """
    return enbase64(urandom(length))


def verify_password(password, password_hash, salt):
    """ Given a password, hash, salt this function verifies the password
        is equal to hash/salt.

        Args:
            password (str): The password to check.
    """
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    scrypt_hash_base64 = generate_hash(password, salt)

    if password_hash == scrypt_hash_base64:
        return True

    return False
