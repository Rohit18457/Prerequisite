def reverse(num):
  rev=0
  while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
  return rev

def isPalindrome(num):
  return num==reverse(num)

t=int(input())
for i in range(t):
  num=int(input())
  count=0

  while not isPalindrome(num):
    rev=reverse(num)
    num+=rev
    count+=1
  print(count,num)
