import rsa

publicKey, privateKey = rsa.newkeys(512)

pesan = "hello geeks"

encpesan = rsa.encrypt(pesan.encode(),publicKey)
  
print("Pesan Asli : ", pesan)
print("encrypted pesan : ", encpesan)

decpesan = rsa.decrypt(encpesan, privateKey).decode()
  
print("Deskripsi pesan : ", decpesan)
