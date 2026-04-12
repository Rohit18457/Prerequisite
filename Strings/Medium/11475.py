def isPalindrome(str,start):
  left=start
  right=len(str)-1
  while left<right:
    if str[left]!=str[right]:
      return False
    left+=1
    right-=1
  return True

s=input()
n=len(s)

for i in range(n):
  if isPalindrome(s,i):
    result=s
    for j in range(i-1,-1,-1):
      result+=s[j]
    print(result)
    break