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
	while (i < n-1):


		while (price[i] > price[i+1] and i < n-1):
			i += 1


		if price[i] < price[i+1]:

			# Store the index of minima
			buy = i
		i += 1


		while (i < n-1 and price[i]<price[i+1]):
			i += 1

		# Store the index of maxima
		sell = i

		print("Buy on day: ",buy,"\t",
				"Sell on day: ",sell)
		
# Driver code
# product prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]

n = len(price)

# Fucntion call
productBuySell(price, n)


