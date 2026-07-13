def max_profit(prices):
  min_price = float('inf')
  max_profit=0
  for price in prices:
    min_price = min(min_price,price)
    profit = price - min_price
    max_profit=max(max_profit,profit)
  return max_profit

prices=[45000,35000,27800,23950,280000,269000,5200,4500]
res=max_profit(prices)
print(res)