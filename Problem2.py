#Prints the fibonaccie sequence from 1 - 4,000,000 and sums the even numbers.

z = 0
sum = 2

def fib(x, y):
	global z
	global sum
	
	while z < 4000000:
		z = x + y
		if z > 4000000:
			break
		print z
		if z % 2 == 0:
			sum += z
		fib(y, z)
		
fib(1, 2)
print sum
		

	