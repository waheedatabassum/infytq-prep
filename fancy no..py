n=int(input())
n1=n2=n
max=0
while n:
    c=0
    l=n%10
    n=n%10
  while n1:
      r=n%10
      n1=n1//10
      if l==r:
          c+=1
    if m<c:
            m=c
            n1=n2
        if(m=1):
            print("not fancy")
            else:
            print("fancy")
