import cv2
import os
import numpy as np

img = cv2.imread("563930.jpg").astype(np.uint8)

msg = input("Enter secret message: ")

password = input("Enter password: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

# Encryption
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("Encryptedmsg.jpg", img)

os.system("start Encryptedmsg.jpg")

# Decryption
message = ""

n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")

if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("Not a valid key.")
