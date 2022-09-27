def currencyConversion(price):
   if price[0] == '$':
      return float(price[1:])
   elif price[0:3] == 'GBX':
      return float(price[3:])*1.2