import random 
import math


def is_prime(number):
    if number<2:
        return False
    for i in range (2,number//2+1): 
        if number%i==0:
            return False
    return True


def generate_prime(min_value,max_value):
    prime=random.randint(min_value,max_value)
    while not is_prime(prime):
        prime=random.randint(min_value,max_value)
    return prime

def mod_inverse(e,phi):
    for d in range(3,phi):
        if(d*e)%phi==1:
            return d
    raise ValueError("mod inverse doesnot exsist")


p,q=generate_prime(100,200),generate_prime(100,200)

while p==q:
    q=generate_prime(100,200)

n=p*q

phi_n=(p-1)*(q-1)


e=random.randint(3,phi_n-1)
while math.gcd(e,phi_n)!=1:
    e=random.randint(3,phi_n-1)



d=mod_inverse(e,phi_n)


print("Public key:",e)
print("Private key:",d)
print("n :",n)
print("Phi of n:",phi_n)
print("p:",p)
print("q:",q)



message="Hello world"


message_encoded=[ord(ch) for ch in message]
cipher_text=[pow(ch,e,n) for ch in message_encoded]
print("The cipher text of the message is: ")
print(cipher_text)



message_encoded=[pow(ch,d,n) for ch in cipher_text]
message1="".join(chr(ch) for ch in message_encoded)
print("The original message is: ")
print(message1)
