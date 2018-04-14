from Crypto.Cipher import AES
import time

start_time = time.time()

key = b'\xa1+\xde1/AG;^v\r\xcd+Z\x97h\x91\xcb\x8c\t\xdd\x13fQ\x13\x9e\x9b\x91x\xb6\xad\x06'
file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]


cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

file = open("decrypted.json", 'wb')
if file.mode == 'wb':
    file.write(data)

file.close()

print("--- %s seconds ---" % (time.time() - start_time))
