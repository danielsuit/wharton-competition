def currencyConversion(price):
   if price[0] == '$':
      price = price.replace(',', '')
      return round(float(price[1:]),2)
   elif price[0] == '₹':
      price = price.replace(',', '')
      return round(float(price[1:])*0.012,2)
   elif price[0:2] == 'R$':
      price = price.replace(',', '')
      return round(float(price[2:])*0.19,2)
   elif price[0] == '¥':
      price = price.replace(',', '')
      return round(float(price[1:])*0.14,2)
   elif price[0:3] == 'GBX':
      price = price.replace(',','')
      return round(float(price[6:])*0.0113,2)
   return float(price)