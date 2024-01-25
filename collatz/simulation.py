import math
import matplotlib.pyplot as plt 
from tqdm import tqdm
def collatz(n):
	if (n < 1):
		return 0
	num = n
	steps = 0
	while (num != 1):
		if (num % 2 == 0):
			num = num/2
			steps += 1
		else:
			num = 3*num+1
			steps += 1
	return steps

def main():
	xs = []
	ys = []
	upper_bound = 100000

	for i in tqdm(range(upper_bound)):
		xs.append(i)
		ys.append(collatz(i))

	plt.scatter(xs, ys, color='skyblue', s=0.3)
	# Add labels and a title
	plt.xlabel('Steps until 4-2-1-loop')
	plt.ylabel('Number')
	plt.title('Collatz Conjecture')

	#plt.show()
	plt.savefig("./images/example.png")


if __name__ == "__main__":
	main()