def currencyConversion(price):
   if price[0] == '$':
      price = price.replace(',', '')
      return float(price[1:])
   elif price[0] == '₹':
      price = price.replace(',', '')
      return float(price[1:])*0.012
   elif price[0:2] == 'R$':
      price = price.replace(',', '')
      return float(price[2:])*0.19
   elif price[0] == '¥':
      price = price.replace(',', '')
      return float(price[1:])*0.14
   return price
