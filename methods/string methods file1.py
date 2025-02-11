s2=('py thon')
print(len(s2))
print(s2[0:4])
str1='hi priya how r u'
result=str1.capitalize()
print(result)
str1='hi priya how r u'
result=str1.title()
print(result)
str1='python welcomes python by learning python '
result=str1.count('p')
print(result)
str1='laxmi12342@gmail.com'
result=str1.endswith('gmail.com')
print (result)
str1='jaanu junnu python'
result=str1.find('j')
print(result)
result=str1.find('a')
print(result)
result=str1.find('a',-2,10)
print(result)
str1='jaanu junnu academy with lots of intelligence'
result=str1.find('lots',21)
print(result)
str2='hello team good morning'
result=str2.split(" ")
print(result)
result=str2.split(",")
print(result)
str3='hello&team&good&morning'
result=str3.split('&')
print(result)
str4="this$is$priya"
a=str4.split('$')
print(a)
result="$".join(a)
print(result)
result=" ".join(a)
print(result)
str1='LAXMI PRIYA'
result=str1.lower()
print(result)
str2='laxmi priya'
result=str2.upper()
print(result)
str3='Hi hOw R U'
result=str3.swapcase()
print(result)
str4='hello jaanu what r u doing'
str5=str4.replace('a','o')
print(str5)
str1="    hello!!!!!!!laxmi%%%%"
result=str1.strip(' ')
print(result)
str2="&&&&goodmorning$$$$$"
result=str2.strip('&')
print(result)
str3='good night'
str1='123$56@87%'
result=str1.isdigit()
print(result)
str1='123456789'
result=str1.isdigit()
print(result)
str2='as12run3as5'
result=str2.isalpha()
print(result)
str2='laxmi'
result=str2.isalpha()
print(result)
str3='1,2,3,4'
result=str3.isnumeric()
print(result)
str2='hi team how r u'
result=str2.istitle()
print(result)
str1='Hi Team'
result=str1.istitle()
print(result)
STR1='this is python'
result=STR1.islower()
print(result)
str1="THIS IS PYTHON"
result=str1.isupper()
print(result)
str1='good mng% team'
result=str1.isspace()
print(result)
str2="welcome python"
result=str2.isidentifier()
print(result)
str1="_welcome 123 python"
result=str1.isidentifier()
print(result)
str1=""
dict1=("a","1","b","2","c","3")
result=str1.maketrans('1','2','3')
print(result)
str1='_22demo123'
result=str1.isidentifier()
print(result)
str2='1,2,3,4,2.3,1.5'
result=str2.isnumeric()
print(result)
str1='hello world'
result=str1.isspace()
print(result)
s1='hello team {name} world2 {name3}'
result=s1.format(name3='4',name='jaanu')
print(result)
s = "this is python %s and I am paying for %s and cost is %d" % ('class','class',1000)
print(s)
s = "Python"
centered_string = s.center(10,'p')
print(centered_string)
s='this is python\n iam laxmi priya\n my daughter is junnu\n'
result=s.splitlines()
print(result)
