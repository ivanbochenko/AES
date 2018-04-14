from Crypto.Cipher import AES
import time

start_time = time.time()
# from Crypto.Random import get_random_bytes


file = open("100mb.json", 'rb')
if file.mode == 'rb':
    data = file.read()

file.close()

key = b'\xa1+\xde1/AG;^v\r\xcd+Z\x97h\x91\xcb\x8c\t\xdd\x13fQ\x13\x9e\x9b\x91x\xb6\xad\x06'
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

file_out = open("encrypted.bin", "wb")
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]

print("--- %s seconds ---" % (time.time() - start_time))
