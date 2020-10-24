import fernet as f
import time
def encrypt(token,psw,level=1):
	start = time.time()
	for i in range(level):
		token = str(f.encrypt(token, psw),"utf-8")
	end = time.time()
	print('Time taken to encrypt is : '+str(end-start))
	return token
def decrypt(token,psw,level=1):
	token = bytes(token, 'utf-8')
	start = time.time()
	for i in range(level):
		token = f.decrypt(token,psw)
	end = time.time()
	print('Time taken to decrypt is : '+str(end-start))
	return str(token, 'utf-8')
