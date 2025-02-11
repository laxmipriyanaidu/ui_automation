l=[1,2,2,3,3,4,5,6,7,5,6]
dict={}
for i in l:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
