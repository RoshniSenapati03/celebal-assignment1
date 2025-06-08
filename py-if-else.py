def check_number(num):
  if num > 0 :
    print("Positive")
  elif num < 0 :
    print("Negative")
  else:
    print("Zero")

if __name__ == '__main__':
  n = intt(iput("Enter a number: "))
  check_number(n)
