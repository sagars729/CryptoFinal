import random
import time
d = {}
def twopow(s):
	if not s in d: d[s] = pow(2,s)
	return d[s]

def trial(n,r,d):
	a = random.randint(2,n-1)
	if pow(a,d,n) - 1 == 0: return True
	for s in range(0,r):
		if pow(a,d*twopow(s),n) == n-1: return True
	return False
 	
def isPrimeOpt(n,t=10):
	if n%2==0: return False
	d,r= n-1, 0
	while(d%2==0):
		r+=1
		d//=2
	for i in range(t):
		if not trial(n,r,d): return False
	return True
def isPrime(n):
	for i in range(2,int(n**.5)):
		if(n%i==0): return False
	return True

def search(a,b,n):
	lis = set()
	start = time.perf_counter()
	while len(lis) <  n:
		i = random.randint(a,b)
		if i%2 == 0: continue
		if isPrimeOpt(i): lis.add(i) 
	end = time.perf_counter()
	#print(end-start)
	return lis
isSquare = lambda a: a>=0 and a**(1/2) == int(a**(1/2))
def factor(n):
	x = int(n**(1/2)+1)
	while not isSquare(int(x**2-n)): x+=1
	y = (x**2-n)**(1/2)
	return x+y,x-y
def run_trial(e,log=True):
	start = time.perf_counter()
	primes = [i for i in search(2**(e-1), 2**e, 2)]
	bench = time.perf_counter()
	factors = factor(primes[0]*primes[1])
	end = time.perf_counter()
	if(log):
		print("Between 2 to the ", e-1, "th and 2 to the ", e, "th power",sep="")
		print("Found primes", primes[0], "and", primes[1], "in", bench-start,"seconds")
		print("Factored product", primes[0]*primes[1], "to", factors, "in", end-bench, "seconds")
	return bench-start, end-bench
def run_trial_opt(e):
	start = time.perf_counter()
	a = primefac.nextprime(random.randint(2**(e-1), 2**e))
	b = primefac.nextprime(random.randint(2**(e-1), 2**e))
	bench = time.perf_counter()
	f = primefac.factorint(a*b)
	end = time.perf_counter()
	return bench-start, end-bench
def run_multiple_trials(e,t=10):
	ptime = 0
	ftime = 0
	for i in range(t):
		dptime, dftime = run_trial(e,False)
		ptime+=dptime
		ftime+=dftime
	print("Found Primes In", ptime/10)
	print("Found Factors In", ftime/10)

#for n in range(26,31):
#	run_multiple_trials(n)



