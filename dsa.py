from miller import search as primenums #My Implementation of Miller Rabin Primality Test
from random import randint #Random Integer Function 
from hashlib import sha224 as H #Hash Function
##### Initial Parameters #####
## l = Key Length 
## n = Crypographic Strength of Key; Must be less than output of H 
## q = n-bit Prime 
## p = l-bit Prime Such That p-1 = Z*q 
## g = a number such that g^p = 1 mod(p) 
def params(h,l=2048,n=224):
	q = primenums(2**(n-1), 2**n)[0]
	p = primenums(2**(l-1), 2**l)[0] #change
	z = (p-1)//q
	h = 2
	while ( pow(h,z,p) == 1 and h < p): h+=1
	if h==p: return None
	else: g = pow(h,z,p)
	return p,q,g
##### User Keys #####
# x = secret private key
# y = public key

def user_keys(params):
	p,q,g = params
	x = randint(1,q-1)
	y = pw(g,x,p)
	return y,x
##### Signing algorithm #####
def sign(msg,params):
	k = randint(2,q-1)
	r = pow(g,k,p)%q
	if r == 0: sign(msg,params)
	s = (modinv(k)*(H(msg).hexdigest()+x*r))%q
	if s == 0: sign(msg,params)
	return r,s

##### Verification algorithm #####
def verify(sig,params):
	if r < 0 or r > q or s < 0 or s > q: return False
	w = modinv(s)%q
	u1 = (H(sig).hexdigest()*w)%q
	u2 = (r*w)%q
	v = ((pow(g,u1,p)*pow(y,u2,p))%p)%q		
	

