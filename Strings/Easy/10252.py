s1=input()
s1=s1.lower()

s2=input()
s2=s2.lower()
result=""
for ch in s1:
  if ch in s2:
    result+=ch

result=''.join(sorted(result))
print(result)

