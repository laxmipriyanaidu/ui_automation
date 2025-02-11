s="rekhanadh naidu"
dict={}
for item in s:
    if item not in dict:
        dict[item]=1
    else:
        dict[item]+=1
print(dict)
#find number of occurances present in the list or string
