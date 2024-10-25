# Python code for the above approach
import math

def is_prime(n: int) -> bool:
	# Check if n = 1 or n = 0
	if n <= 1:
		return False

	# Check if n = 2 or n = 3
	if n == 2 or n == 3:
		return True

	# Check whether n is divisible by 2 or 3
	if n % 2 == 0 or n % 3 == 0:
		return False

	# Check from 5 to square root of n
	# Iterate i by (i + 6)
	for i in range(5, int(math.sqrt(n))+1, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False

	return True


def check(arr, n):
	# Store all possible non-prime indxes
	non_prime_numbers = []
	for i in range(2, n + 1):
		if(not is_prime(i)):
			non_prime_numbers.append(i)
	np = len(non_prime_numbers)

	# Iterate over range n
	for i in range(n):

		# Check if prime or not
		if(is_prime(arr[i])):

			# If lowest value of non-prime number is
			# out of the range for current index
			# then we don't have to calculate
			# for the remainings
			if ((i + 3) >= n):
				break

			j = 0

			# Check for prme numbers in non-prime
			# indexesas per current index i
			while(j < np and (i + non_prime_numbers[j]-1) < n):
				if(not is_prime(arr[i + non_prime_numbers[j]-1])):
					return False
				j += 1

	return True


# Driver's code
if __name__ == "__main__":
	arr = [5, 9, 3, 7, 8, 2]
	n = len(arr)

	# Function call
	if(check(arr, n)):
		print("Prime")
	else:
		print("Non Prime")
