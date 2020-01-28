def max_profit_of_stocks(stock_prices):
    """Return max profit you could make from a list of stocks.
    Index of stock_prices is time that had passed since trading started.
    Value of stock_prices is value of stock at that time
    """

    if len(stock_prices) < 2:
        print("Max profit does not exist. List must have more than one value in order to trade stocks.")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    #start at index one, because we can't buy and sell at index 0
    for i in range(1, len(stock_prices)):
        current_price = stock_prices[i]
        
        #Can we get a better profit by buying at min_price and selling at the current_price
        difference = current_price - min_price
        max_profit = max(max_profit, difference)
        
        #update minimum price
        min_price = min(min_price, current_price)


    return max_profit

stock_prices = [10, 7, 5, 8, 11, 9]
print(max_profit_of_stocks(stock_prices))
stock_prices = [10, 9, 8, 7, 6, 5]
print(max_profit_of_stocks(stock_prices))