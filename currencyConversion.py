def currencyConversion(price):
   if price[0] == '$':
      price = price.replace(',', '')
      price = float(price[1:])
   elif price[0] == '₹':
      price = price.replace(',', '')
      price = float(price[1:])*0.012
   elif price[0:2] == 'R$':
      price = price.replace(',', '')
      price = float(price[2:])*0.19
   elif price[0] == '¥':
      price = price.replace(',', '')
      price = float(price[1:])*0.14
   elif price[0:3] == 'GBX':
      price = price.replace(',','')
      price = float(price[6:])*0.0113
   return round(price, 2)