def get_country_codes(prices):
    codes = []
    arr = prices.split(", ")
  
    for i in range(len(arr)):
        codes.append(arr[i][:arr[i].index('$')])
  
    return ", ".join(codes)