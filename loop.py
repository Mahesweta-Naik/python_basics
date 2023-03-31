'''#for loop
#odd-->square it,even-->cube it
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    res.append(row_data)
print(res)
#list comprehension
print([ele**2 if ele%2!=0 else ele**3
       for row in mat for ele in row])
#in dynamic
print([[ele**2 if ele%2!=0 else ele**3
      for ele in row] for row in mat ])
#Q2
mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
arr=[]
for j in listb:
    for i in mylist:
        if i==j:
            a=(i,mylist.index(i))
            arr.append(a)
print(arr)
#or
for i in listb:
    arr.append((i,mylist.index(i)))
print(arr)
#list comp
print([(i,mylist.index(i)) for i in listb])
#dictioary comp
print({i:mylist.index(i) for i in listb})
#Q3
sentences=["a new world record was made","in the holly city of Ayodhya",
           "on the eve of diwali on tuesday","with over three lakh diya or earthen lamps",
           "lit up simultaneously on the banks of the sarayu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']
res=[]
for i in sentences:
    row_data=[]
    for word in i.split():
        if word not in stopwords:
            row_data.append(word)
    res.append(row_data)
print(res)
#Q4
arr=list(map(int,input().split(",")))
num1=sum(arr[:arr.index(5)])+sum(arr[arr.index(8)+1:])
l=arr[arr.index(5):arr.index(8)+1]
num2=" "
for i in l:
    num2+=str(i)
print(int(num2)+num1)
#Q5
s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
    def rotate(ss,n):
        n=str(n)
        s=0
        for i in n:
            s+=int(i)**2
            if s%2==0:
                return ss[-1]+ss[:-1]
            else:
                return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))
#Q6
def nearest_palindrome(n):
      def ispalindrome(n):
          return str(n)==str(n)[::-1]
      i=n+1
      while True:
           if ispalindrome(i):
                return i
           i+=1
n=int(input("Enter the number:"))
print(nearest_palindrome(n))
#or
import sys
def nearest_palindrome(n):
    for i in range(n+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
n=int(input("Enter the number:"))
print(nearest_palindrome(n))
#Q7
def fun(p_details,medical_speciality):
    max_visit=0
    P=p_details.count('P')
    E=p_details.count('E')
    O=p_details.count('O')
    if P>E and p>0:
        speciality=medical_speciality["p"]
    elif E>P and E>O:
        speciality=medical_speciality["E"]
    else:
        speciality=medical_speciality["O"]
    return speciality

medical_speciality={"P":"Pedriatrics","O":"Otrhopedicts","E":"ENT"}
list1=list(map(str,input(),split()))
speciality=fun(p_details,medical_speciality)
print(speciality)
#Q8
s1=input()
s2=input()
s3=" "
for i in s1:
    for j in s2:
        if i==j:
            s3+=j
print(s3.replace(" ",""))'''

