
for i in range(5):
  x=int(input())
  p=0
  for i in range(2,x+1):
    if x%i==0:
      p=0
      break
    rev=0
    while x>0:
      rem=x%10
      rev+=rem*10
      x=x//10
    for i in range(2,rev+1):
      if rev%i==0:
        p=1
  p=2
  if p==0:
    print("Not prime")
  elif p==1:
    print("Prime")
  else:
    print("Empire")
