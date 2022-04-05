file_t = open("decryptkey.txt","a")
file_t.write("this is the file the holds decrypted data")
file_t.close()

file_t.open("decryptkey.txt", "r")
print(file_t.read())
