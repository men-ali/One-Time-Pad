#Sushma Mahadeo and Alicia Mendez Medina 
#Crypto OTP
import sys, random, os, string, math
def keygen(s):
    return [ord(i) for i in s] #Obtains the ASCII value of each letter in the string

def randn(N):
    n = len(N) #Gets the length of the string
    """Generating a random letter from ASCII all uppercase, the amount of letters are
    determined by the length of the message -n. The random letters are join together in a string"""
    x=' '.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(n))
    print("Random key: ",x)
    return x

def encrypt(plaintext, key):
    plaintext= keygen(plaintext) #Keygen is used to get the ASCII value of the plaintext
    key = key.split() #Since key is a string, it is split to obtain individual element
    """Key is converted to ascii, then to bin, but removing the first to elements, and converting that to binary.
    The process is done for all values in key"""
    key = [int(bin(ord(i))[2:]) for i in key]
    print("Binary key: ", key)
    ciphertext = []
    """For each value in plaintext and key, gets zip - returns iterator of tuples, and the XOR of each value is taken """
    for i, j in zip(plaintext, key):
        p = format(i ^ j ,'b') # b for binary
        ciphertext.append(p)

    return ' '.join(ciphertext) #values are join together to form a string

def decrypt(ciphertext, key):
    #ciphertext is a string so it needs to be split
    ciphertext = ciphertext.split()
    key = key.split()
    """Key is converted to ascii, then to bin, but removing the first to elements, and converting that to int.
       The process is done for all values in key"""
    key = [int(bin(ord(i))[2:]) for i in key]
    """ciphertext is converted to int.
    The process is done for all values in key"""
    ciphertext = [int(i, 2) for i in ciphertext]
    plaintext = []

    """For each value in ciphertext and key, gets zip - returns iterator of tuples, and the XOR of each value is taken """
    for x, y in zip(ciphertext, key):
         p = x ^ y
         plaintext+=(chr(int(p))) #bin is converted to int and then to character

    return ' '.join(plaintext) #the plaintext is converted to a string


def main():
    m = input("Enter the message: ")
    m = m.upper() #message is converted to uppercase
    ms = m.strip() #since message is a string, it is unjoined
    key = randn(m)

    ciphertext = encrypt(ms, key)
    print("Ciphertext: ",ciphertext)
    
    file = open("Ciphertext.txt", 'w')
    file.write(ciphertext)
    file.close()

    plaintext = decrypt(ciphertext, key)
    print("Plaintext:" ,plaintext)

main()