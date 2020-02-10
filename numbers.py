n=int(input())
n1=n
#finding of last and first digits open
f=n%10
while n:
    r=n%10
    n=n//10
    print(f,r)
    #finding of no.of digits in a no.
    n=n1
    count=0
    while n:
        n=n//10
        count+=1
print(count)

    #finding of last and first digits close
    n=n1
    m=count/2
    i=0
    
while n:
    r=n%10
    n=n/10
    if(n==m-1):
        m1=r
        m2=n%10
        break
    i+=1
print(m1,m2)
   
    
   

