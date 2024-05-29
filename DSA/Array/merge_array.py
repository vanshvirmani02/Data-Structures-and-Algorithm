a=[3,3,4,5,6,7,8,9,9,9] 
b=[2,4,10,10]

temp=[]
i,j=0,0
while i <len(a) and j <len(b):
    if a[i]<=b[j]:
        if len(temp)==0 or temp[-1]!=a[i]:
            temp.append(a[i])
        i+=1
    else:
        if len(temp)==0 or temp[-1]!=b[j]:
            temp.append(b[j])
        j+=1

while j < len(b):
    if len(temp)==0 or temp[-1]!=b[j]:
        temp.append(b[j])
    j+=1

while i <len(a):
    if len(temp)==0 or temp[-1]!=a[i]:
        temp.append(a[i])
    i+=1

print(temp)
