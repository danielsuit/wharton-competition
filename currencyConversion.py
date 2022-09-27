def currencyConversion(price):
   if price[0] == '$':
      price = price[1:]
      return float(price)
   return price