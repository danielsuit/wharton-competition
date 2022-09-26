def exchangeConversion(exchange):
   if exchange == 'B3 S.A.':
      exchange = 'BVMF'
   elif exchange == 'BSE LTD':
      exchange = 'BOM'
   elif exchange == 'Hong Kong Exchanges And Clearing Ltd':
      exchange = 'HKG'
   elif exchange == 'London Stock Exchange':
      exchange = 'LON'
   elif exchange == 'Nasdaq':
      exchange = 'NASDAQ'
   elif exchange == "New York Stock Exchange Inc.":
      exchange = 'NYSE'
   elif exchange == 'Shanghai Stock Exchange':
      exchange = 'SHA'
   elif exchange == 'Shenzhen Stock Exchange':
      exchange = "SHE"
   elif exchange == 'Toronto Stock Exchange':
      exchange = "TSE"
   return exchange