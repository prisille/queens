
# the 8 queens problem

from __future__ import print_function


def check_board(d, i):
	for j in range(1, i):
		if (d[i-1] == d[j-1]) or (abs(d[i-1]-d[j-1]) == i-j):
			return False
	return True


def print_board(d, size):
	print("--------")

	for i in range(1, size+1):
		print(d[i-1], end='')
	print()

	for i in range(1, size+1):
		for j in range(1, size+1):
			if (d[j-1] == i) and d[j-1] != 0:
				print("X", end='')
			else:
				print(" ", end='')
		print()


def solve_board(size, printSolution = False):
	
	n = 0
	d = [0] * size
	count = 0
	
	while True:
		d[n] = d[n]+1
		if d[n] > size:
			if n == 0:
				break
			n = n-1
		else:
			if check_board(d, n+1):
				if (n == size-1):
					count += 1
					if printSolution:
						print("Solution = %d" % count)
						print_board(d, size)
						print()
				else:
					n = n+1
					d[n] = 0
	return count

if __name__ == '__main__':
		
	solve_board(5, True)
