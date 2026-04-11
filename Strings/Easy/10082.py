keyboard="`1234567890-=QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,./"

n=int(input())
for i in range(n):
  result=""
  str=input()
  for ch in str:
    if ch==" ":
      result+=" "
    else:
      idx=keyboard.find(ch)
      result+=keyboard[idx-1]
  print(result)
