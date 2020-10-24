
#fernet text encrypt and decrypt

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def encrypt(msg,psw):
	msg = str(msg)
	password_provided = str(psw)  # This is input in the form of a string
	password = password_provided.encode()  # Convert to type bytes
	salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
		)
	key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
	message = msg.encode()
	f = Fernet(key)
	encrypted = f.encrypt(message)
	#print(encrypted)
	return encrypted

def decrypt(token,psw):
	password_provided = psw  # This is input in the form of a string
	password = password_provided.encode()  # Convert to type bytes
	salt = b'salt_'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
		)
	key = base64.urlsafe_b64encode(kdf.derive(password))
	f = Fernet(key)
	#return str(f.decrypt(token),"utf-8")
	return f.decrypt(token)