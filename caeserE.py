##            
####ENCRYPTION CAESER CIPHER   
##text=input("Enter the PLAIN TEXT")
##key=int(input("Enter the key value"))
##print("The plain text is :",text)
##encrypted=''
##
##for char in text:
##    if char.isalpha():
##        start = 65 if char.isupper() else 97
##
##        encrypted=encrypted+chr((ord(char)-start+key)%26+start)
##    else:
##       encrypted+=char
##print("The encrypted form of the plain text is ",encrypted)

##DECRYPTION CAESER CIPHER
encrypt=input("Enter the ENCRYPTED TEXT")
key=int(input("Enter the key value"))
print("The plain text is :",encrypt)
decrypted=''

for char in encrypt:
    if char.isalpha():
        start = 65 if char.isupper() else 97

        decrypted=decrypted+chr((ord(char)-start-key)%26+start)
    else:
       decrypted+=char
print("The decrypted form of the cipher text is ",decrypted)






