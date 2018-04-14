from Crypto.Random import get_random_bytes
# data = open("100mb.json", 'r')
# if data.mode == 'r':
#     contents = data.read()
#     print(contents)
#
# data.close()

key = get_random_bytes(32)
print(key)
