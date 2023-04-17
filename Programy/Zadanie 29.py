list1=input().split()
list2=input().split()
for i in list1:
    if i not in list2:
        print(i)