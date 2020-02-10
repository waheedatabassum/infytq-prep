l=list(map(int,input().split()))
n=[1,2,3,4,5]
#get a value
print(n[2])
#get length
print(len(n))
#append to list
n.append(6)
print(n)
#remove from list
n.remove(1)
print(n)
#insert into position
n.insert(0,1)
print(n)
#remove with pop
n.pop(2)
print(n)
#reversing the list
n.reverse()
print(n)
#sorting the list
n=[2,4,3,5,1]
n.sort()
print(n)
#reverse sort
n.sort(reverse=True)
print(n)
