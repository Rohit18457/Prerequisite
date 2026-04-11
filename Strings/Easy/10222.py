keyboard="`1234567890-=QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,./"
str=input()
result=""
for ch in str:
  if ch==" ":
    result+=" "
  else:
    idx=keyboard.find(ch)
    result+=keyboard[idx-2]
print(result)