#Given a Python list, remove all the even number from the list and save those even number in another list and print both the lists.
a=list(map(int,input().split(" ")))
r=list(filter(lambda n:n%2==0,a))
a=[i for i in a if i not in r]
print("List1=",a)
print("List2=",r)
