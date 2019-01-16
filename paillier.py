from __future__ import absolute_import
import random
import math

def millerrabin(n):
    if n % 2 == 0:
        return False
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s =s/2
    s  = int(s)    
    for var in range(10):
        a = random.randint(2, n - 1)
        x = pow(a, s,n)
        if x == 1 or x == n - 1:
            continue
        for var2 in range(r - 1):
            x = pow(x, 2,n)
            if x == n - 1:
                break
        else:
            return False
    return True
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        print('modinv does not exist')
    else:
        return x % m
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def lcm(x, y):
   return x * y // gcd(x, y)
def primenumber(f):
  start = random.randint(pow(10, f-1),pow(10, f))
  while(1):
      if(millerrabin(start)):
        return start
      start =  random.randint(pow(10, f-1),pow(10, f))
def Paillier(f,encode):
   ######CREATE KEYS######
   p1= primenumber(f) # Begin with two random prime numbers
   p2= primenumber(f)
   ###PUBLIC KEYS --- g, n
   n = p1*p2 
   g= n+1 #any number coprime to n
   print(n)
   ###PRIVATE KEYS --- lamb, mu
   lamb = lcm(p1-1,p2-1) 
   L = (pow(g, lamb, n*n)-1)//n
   mu = modinv(L, n) # equal to (L(g^lambda mod(n^2)))^-1
   # where L(x) = (x-1)//
   #####ENCRYPTION#######
   r = 65537 ## can be any number coprime to n, adds randomness to encryption process
   ciphertext = (pow(g,encode, n*n) * pow(r, n, n*n))%(n*n) ## Encryption is  c=g^{m}* r^{n} mod (n^2)
   return ciphertext 
def PaillierSolve(encrypted, mu, y, n): #y is lambda
  c = encrypted
  if(c < n*n): #Ciphertext must be split if > N^2
     L = (pow(c, y, n*n)-1)//n
     m = (L *mu)%n ## Decryption is L(c^y mod(n^2)) * mu mod(n)
    # where L(x) = (x-1)//n
     return m
  print("C too big")
