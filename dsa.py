from miller import search as primenums #Prime Numbers Found Using Miller Rabin Primality Test 
from miller import isPrimeOpt as isprime #My Implementation of Miller Rabin Primality Test
from random import randint #Random Integer Function 
from hashlib import sha224 as H #Hash Function
import time
##### Mod Inverse Function #####
# a = number we want the inverse of
# m = prime mod
def modinv(a,m):
	g = gcd(a,m)
	if g != 1: return -1
	else: return pow(a, m-2, m)

def gcd(a,b):
	if a == 0: return b
	return gcd(b%a,a)
##### Initial Parameters #####
## l = Key Length 
## n = Crypographic Strength of Key; Must be less than output of H 
## q = n-bit Prime 
## p = l-bit Prime Such That p-1 = Z*q 
## g = a number such that g^p = 1 mod(p) 
def gen_params(l=2048,n=224): 
	q = [i for i in primenums(2**(n-1), 2**n, 1)][0]
	p = gen_p(q,l,n)
	if p == -1: return gen_params(l,n)
	z = (p-1)//q
	h = 2
	while ( pow(h,z,p) == 1 and h < p): h+=1
	if h==p: return None
	else: g = pow(h,z,p)
	return p,q,g  #Sharable Values

def gen_p(q,l,n): #Very Slow
	lb = 2**(l-1)//q + 1
	ub = 2**(l)//q - 1
	z = randint(lb,ub)
	dt = time.time()
	while not isprime(z*q+1):
		if time.time() - dt >= 2: 
			print("Trying New Params") #attempts to generate new params if taking too long
			return -1
		z = randint(lb,ub)
	return z*q+1	
##### User Keys #####
# x = secret private key
# y = public key
def user_keys(params):
	p,q,g = params
	x = randint(1,q-1)
	y = pow(g,x,p)
	return y,x

##### Signing algorithm #####
# k = random number 1 < k < q
# r = (g^k mod p) mod q != 0
# s = (k^-1 * H(msg) + xr)%q != 0
def sign(msg,params,keys):
	p,q,g = params
	y,x = keys
	k = randint(2,q-1)
	r = pow(g,k,p)%q
	if r == 0: sign(msg,params,keys)
	print(int("0x"+H(msg).hexdigest(),0) + x*r)
	print(modinv(k,q))
	s = (modinv(k,q)*(int("0x"+H(msg).hexdigest(),0)+x*r))%q
	if s == 0: sign(msg,params,keys)
	return r,s

##### Verification algorithm #####
# 0 < r < q and 0 < s < q
# w  = s^-1 mod q
# u1 = H(msg) * w mod q
# u2 = r * w mod q
# v  = (g^u1 * y^u2) mod q
def verify(sig,params,y):
	r,s = sig
	p,q,g = params
	if r < 0 or r > q or s < 0 or s > q: return False
	w = modinv(s,q)%q 
	u1 = (int("0x"+H(msg).hexdigest(),0)*w)%q
	u2 = (r*w)%q
	v = ((pow(g,u1,p)*pow(y,u2,p))%p)%q		
	return v == r

##### Main Method #####
# 1) Generate Params
# 2) Generate Keys
# 3) Sign Message
# 4) Verify Message
if __name__ == "__main__":
	msg = b"Hello"
	print("Generating Params")
	params = gen_params()
	print("Generating Keys")
	keys = user_keys(params)
	print("Params:",params,"\nKeys:",keys) 
	print("Generating Signature")
	sig = sign(msg, params,keys)
	print("Signature:", sig)
	print("Verifying Signature")
	ver = verify(sig,params,keys[0])
	print("Verified:", ver)
