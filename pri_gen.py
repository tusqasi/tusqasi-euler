# module with prime related stuff

import math
def if_prime(n):
	
	for i in range(2,int(math.sqrt(n))):
		
		if (n%i)==0:
			yield 0
			
		else:
			yield 1
			
