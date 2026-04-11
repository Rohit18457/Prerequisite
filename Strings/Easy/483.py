def reverse(left,right,s):
  while left<=right:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1

s=list(input())
left=0
right=0

while right<len(s):
  if s[right]==' ':
    reverse(left,right-1,s)
    left=right+1
  right+=1
  
  
if len(s)>0:
  reverse(left,right-1,s)
print("".join(s))