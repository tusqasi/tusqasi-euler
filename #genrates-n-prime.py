#genrates n prime numbers
import math

def gen_prime(n):

	#number of prime
	
	i= 1
	
	lst_primes = []
	while n >= i:
		if n % i == 0:
			i += 1 
			continue
		else:
			lst_primes.append(i)
			i += 1
	return lst_primes
print(gen_prime(9))