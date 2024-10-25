def leapyear(year):
  if year%4==0:
    if year%100:
      if year%400:
        print(f'{year} Leap year')
      else:
        return False
    else:
      return False
  else:
    print(f'{year} No leap year')
leapyear(2024)
leapyear(1993)
leapyear(2023)
leapyear(2000)
