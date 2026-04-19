n=int(input())
for i in range(n):
  s=input()
  if s=='1' or s=='4' or s=='78':
    print("+")
  elif s[len(s)-1]=='5' and s[len(s)-2]=='3':
    print("-")
  elif s[0]=='9' and s[len(s)-1]=='4':
    print("*")
  else:
    print("?")