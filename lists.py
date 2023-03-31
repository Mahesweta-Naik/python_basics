#LIST-->Ordered--default index

'''list1=[]
print(list1,type(list1))
list2=[10,20,30,40,50]
print(list2,type(list2))
list3=[10,20.10,30+3j,True,"Python"]
print(list3,type(list3))
list4=(list[100,200,300])
print(list4)
list5=[101,102,103,104]
print(list5)
list5.append(106)
print(list5)
list5.insert(0,51) #index,value
print(list5)
list5.insert(4,350) #index,value
print(list5)
list5.remove(101)
print(list5)
list5.pop() #pops the last value as default
print(list5)
list5.pop(3) #pops the content of given index value
print(list5)
del list5[1] #deletes the content of the given index value
print(list5)'''


#Q1
'''def count(string):
    char_count=0
    num_count=0
    for i in string:
        if i.isalpha():
            char_count+=1
        elif i.isdigit():
            num_count+=1
        else:
            continue
    return [char_count,num_count]

string=input("Enter a string: ")
print(count(string))'''


#Q2
'''def number_of_pairs(list,sum):
    num=0
    for i in list:
        index=list.index(i)+1
        for j in range(index,len(list)):
            if(i+list[j]==sum):
                num=num+1
    return num
list=[1,2,7,4,5,6,0,3]
print(number_of_pairs(list,6))'''


#Q3
'''def func(str):
    a=""
    if(len(str)<2):
        a= "-1"
    elif(len(str)==2):
        a=str+str
    else:
        a=str[0:2:]+str[-2:]
    return a

str=input("Enter a string: ")
print(func(str))'''


#Q4
'''def ing(str):
    new=""
    if (len(str)<3):
        new=str
    elif (str[-3:]=="ing"): 
        new=str+"ly"
        
    else:
       new=str+"ing"
    return new
str=input("Enter a string: ")
print(ing(str))'''


#Q5
'''def check_double(number):
    double=2*number
    count=0
    for i in number:
        if i in double:
            count+=1
        else:
            return False
            break
    if count==len(number):
         return True

number=input()
print(check_double(number))'''



#Q6
#sorted will always return a list
'''def more_than_average(marks):
    sum=0
    count=0
    for i in marks:
        sum+=i
        avg=sum/10
    for j in marks:
        if j>avg:
            count=count+1
            percent=(count/10)*100
    return percent

def sort(marks):
    marks=sorted(marks)
    return marks

def generate_frequency(marks):
    freq=[]
    for x in range(26):
        count=0
        for y in marks:
            if x==y:
                count+=1
        freq.append(count)
    return freq

marks=[12,18,25,24,2,5,18,20,20,21]
print(more_than_average(marks))
print(sort(marks))
print(generate_frequency(marks))'''


#Q7
'''def translate(str1):
    dict1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
    list1=[]
    for i in str1:
        list1.append(dict1[i])
    return list1
str1=["merry","christmas"]
print(translate(str1))'''


#Q8
'''def subarray(n1,n2):
    arr=[]
    for i in range(n1,n2+1):
        arr.append(i)
        print(arr)
        result=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            result.append(arr[i:j+1])
    return result
        
n1=int(input("Enter the starting num:"))
n2=int(input("Enter the ending num:"))
print(subarray(n1,n2))'''

    
        

       
#Q8 Alternate
'''n1=int(input())
n2=int(input())
result=[]
array=[i for i in range(n1,n2+1)]
print(array)'''


























        
        
    
        


