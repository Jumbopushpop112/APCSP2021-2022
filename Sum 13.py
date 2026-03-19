def sum13():
    sum = 0
    hasThirteen = False
    for num in nums:
      if num == 13:
          hasThirteen = True
          continue
      if hasThirteen == False:
          sum += num
      else:
          hasThirteen = False
    return sum
      
