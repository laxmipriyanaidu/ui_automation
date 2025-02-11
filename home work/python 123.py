for i in range(0,6):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

print("check both strings are equal or not after reverse")
s1="python"
s2=s1[::-1]
print(s1)
print(s2)
if s1==s2:
    print("Both are equal")
else:
    print("Both are not equal")
