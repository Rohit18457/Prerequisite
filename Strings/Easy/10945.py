import string
s=input()
s=s.strip()

result=""

for ch in s:
  if ch!=" " and ch not in string.punctuation:
    result+=ch
result=result.lower()

low=0
high=len(result)-1
flag=True
print(result)

while low<high:
  if result[low]!=result[high]:
    flag=False
    break
  else:
    low+=1
    high-=1
    
if flag:
  print("You won't be eaten!")
else:
  print("Uh oh..")

