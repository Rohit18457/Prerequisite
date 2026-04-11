s,t=input().split()

if s in t:
  print("Yes")
else:
  
  j=0
  i=0
  while i<len(s) and j<len(t):
    if s[i]==t[j]:
      i+=1
      j+=1
    else:
      j+=1
  if i==len(s):
    print("Yes")
  else:
    print("NO")

