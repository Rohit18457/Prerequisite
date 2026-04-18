while True:
  n=int(input())
  if n==0:
    break

  ages=list(map(int,input().split()))
  count=[0]*100
  for age in ages:
    count[age]+=1
  result=[]
  for i in range(1,100):
    result+=[str(i)]*count[i]
  print(" ".join(result))