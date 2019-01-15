from miller import search as primenums #Prime Numbers Found Using Miller Rabin Primality Test 
from miller import isPrimeOpt as isprime #My Implementation of Miller Rabin Primality Test
from random import randint #Random Integer Function 
from hashlib import sha224 as H #Hash Function
##### Mod Inverse Function #####
# a = number we want the inverse of
# m = mod
def modinv(a,m):
	for i in range(1,m):
		if((a*i)%m == 1): return i
	return -1
##### Initial Parameters #####
## l = Key Length 
## n = Crypographic Strength of Key; Must be less than output of H 
## q = n-bit Prime 
## p = l-bit Prime Such That p-1 = Z*q 
## g = a number such that g^p = 1 mod(p) 
def gen_params(l=2048,n=224): 
	q = primenums(2**(n-1), 2**n, 1)[0]
	p = gen_p(q,l)#primenums(2**(l-1), 2**l, 1)[0] #Change
	z = (p-1)//q
	h = 2
	while ( pow(h,z,p) == 1 and h < p): h+=1
	if h==p: return None
	else: g = pow(h,z,p)
	return p,q,g  #Sharable Values

def gen_p(q,l):
	lb = 2**(l-1)//q + 1
	ub = 2**(l)//q - 1
	z = randint(lb,ub)
	while not isprime(z*q+1): z = randing(lb,ub)
	return z*q+1	
##### User Keys #####
# x = secret private key
# y = public key
def user_keys(params):
	p,q,g = params
	x = randint(1,q-1)
	y = pw(g,x,p)
	return [y,x]

##### Signing algorithm #####
# k = random number 1 < k < q
# r = (g^k mod p) mod q != 0
# s = (k^-1 * H(msg) + xr)%q != 0
def sign(msg,params,keys):
	p,q,g = params
	y,x = keys
	k = randint(2,q-1)
	r = pow(g,k,p)%q
	if r == 0: sign(msg,params)
	s = (modinv(k,q)*(H(msg).hexdigest()+x*r))%q
	if s == 0: sign(msg,params)
	return [r,s]

##### Verification algorithm #####
# 0 < r < q and 0 < s < q
# w  = s^-1 mod q
# u1 = H(msg) * w mod q
# u2 = r * w mod q
# v  = (g^u1 * y^u2) mod q
def verify(sig,params,y):
	if r < 0 or r > q or s < 0 or s > q: return False
	w = modinv(s,q)%q 
	u1 = (H(sig).hexdigest()*w)%q
	u2 = (r*w)%q
	v = ((pow(g,u1,p)*pow(y,u2,p))%p)%q		
	return v == r

if __name__ == "__main__":
	params = gen_params()
	keys = user_keys(params)
	sig = sign(msg, params,keys)
	ver = verify(sig,params,keys[0])
