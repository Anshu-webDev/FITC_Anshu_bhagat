// Program to find best buying and selling days
import java.util.ArrayList;

// Solution structure
class Interval {
	int buy, sell;
}

class ProductBuySell {
	// This function finds the buy sell schedule for maximum profit
	void stockBuySell(int price[], int n)
	{
		
		if (__)
			return;

		int count;

		
		ArrayList<Interval> sol = new ArrayList<Interval>();

		
		int i;
		while (__) {
			
			while (__ && __))
				i++;

			
			if (i == n - 1)
				{

				}

			Interval e = new Interval();
			e.buy =;
			// Store the index of minima

			
			while (___ && ___))
				i++;

			// Store the index of maxima
			e.sell =;
			

			
			count++;
		}

		// print solution
		if (__)
			System.out.println("There is no day when buying the stock "
							+ "will make profit");
		else
			for (int j = 0; j < count; j++)
				System.out.println("Buy on day: " + sol.get(j).buy
								+ "	 "
								+ "Sell on day : " + sol.get(j).sell);

		return;
	}

	public static void main(String args[])
	{
		ProductBuySell stock = new StockBuySell();

		// product prices on consecutive days
		int price[] = { 100, 180, 260, 310, 40, 535, 695 };
		int n = price.length;

		// fucntion call
		stock.stockBuySell(price, n);
	}
}


