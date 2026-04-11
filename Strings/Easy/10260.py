s=input()
s=s.upper()

res=s[0]
for i in range(1,len(s)):
  if s[i]==s[i-1]:
    continue
  else:
    res+=s[i]
    
result=""
for ch in res:
  if ch=='B' or ch=='F'or ch=='B' or ch=='V':
    result+='1' 
  elif ch=='C' or ch=='G' or ch=='J' or ch=='K' or ch=='Q' or ch=='S' or ch=='X' or ch=='Z':
    result+='2'
  elif ch=='D' or ch=='T':
    result+='3'
  elif ch=='L':
    result+='4'
  elif ch=='M' or ch=='N':
    result+='5'
  elif ch=='R':
    result+='6'
  else:
    continue
print(result)