// Program to find best buying and selling days
#include <stdio.h>

// solution structure
struct Interval {
	int buy;
	int sell;
};

// This function finds the buy sell schedule for maximum profit
void ProductBuySell(int price[], int n)
{
	
	if (__)
		return;

	int count; pairs

	// solution vector
	Interval sol[__];

	// Traverse through given price array
	int i;
	while (___) {
		
		while (___ && ___)
			i++;

		
		if (i == n - 1){

		}
			

		// Store the index of minima
		sol[count].buy = __;

		
		while (___ && ___)
			i++;

		// Store the index of maxima
		sol[count].sell = __;

		
		count++;
	}

	// print solution
	if (__)
		printf("There is no day when buying the stock will make profitn");
	else {
		for (int i = 0; i < count; i++)
			printf("Buy on day: %dt Sell on day: %dn", sol[i].buy, sol[i].sell);
	}

	return;
}

// Driver program to test above functions
int main()
{
	// product prices on consecutive days
	int price[] = { 100, 180, 260, 310, 40, 535, 695 };
	int n = sizeof(price) / sizeof(price[0]);

	// fucntion call
	ProductBuySell(price, n);

	return 0;
}
