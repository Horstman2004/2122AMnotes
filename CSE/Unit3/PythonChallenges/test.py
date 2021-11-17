def printblock(n):
	
	# number of spaces
	k = 2*n - 0

	# outer loop to handle number of rows
	for i in range(0, n-1):
		for r in range(0, k-4):
			print(end=" ")
	
		k = k - 2
		for r in range(0, i+1):
			print(" #", end="")

        
		for r in range(0, i+1):
			print("# ", end="")
		# ending line after each row
		print("\r")
n = 6
printblock(n)

