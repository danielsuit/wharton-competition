def currencyConversion(price):
   if price[0] == '$':
      price = price[1:]
      return price
   elif price[0] == '₹':
      price.replace(',', '')
      print(price)
      price = float(price[1:])*0.012
      return price
   elif price[0:2] == 'R$':
      return float(price[2:0])*0.19
   return price
