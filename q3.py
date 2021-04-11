# Python3 Program to find best buying and selling days


def productBuySell(price, n):

	desc = True
	for i in range(len(price) - 1):
		if price[i] < price[i+1]:
			desc = False
		else:
			desc = True

	if (desc):
		return print("Profit can not be earn at all")
	
	
	i = 0
	while (len(price)):


		while (price[i] and ___):
			i += 1


		if (i == n - 1):


		# Store the index of minima
		buy =
		i =


		while (___ and ___):
			i += 1

		# Store the index of maxima
		sell =

		print("Buy on day: ",buy,"\t",
				"Sell on day: ",sell)
		
# Driver code
# product prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]

n = len(price)

# Fucntion call
productBuySell(price, n)


