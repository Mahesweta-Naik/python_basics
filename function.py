#Decision making statements
'''#raed a number
n=int(input())
#multiple 3
if(n%5==0 and n%3==0):
    print("its a multiple of 5 and 3")
elif(n%3==0):
    print("its a multiple of 3")
elif(n%5==0):
    print("its a multiple of 5")
else:
    print("invalid")
#1 to 100
for i in range (1,101):
    print(i, end=" ")
print()
#1 to 100 even num
for i in range (2,101,2):
    print(i,end=" ")
print()
#100 to 1
for i in range (100,0,-1):
    print(i,end=" ")
print()
#100 to 1 even no
for i in range (100,0,-2):
    print(i,end=" ")
print()
#100 to 1 odd no
for i in range (99,0,-2):
    print(i,end=" ")
print()
#break
#wap to print 1 to 100 if it hit 50 get out of the loop
for i in range (1,101):
    if i==50:
        break
    else:
        print(i,end=" ")
#continue
for i in range (1,101):
    if i==50:
        continue
    else:
        print(i,end=" ")
#pass
for i in range (1,101):
    if (i==50):
        pass
    print(i,end=" ")'''
#FUNCTIONS
'''#function calling
def function1():
    print("its a function")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
function2(10,20)

def function3(num1,num2):
    num3=num1+num2
    return num3
print("value is",function3(10,20))
#if one of the values is in string we hv to convert the string to number so that it can add otherwise it will concatinate
def function4(num1,num2):
    num3=float(num1)+num2
    return num3
print("value is",function4("10",20))
#Categories of Funtion Based on Arguements
#1: Postional argue
def fun1(n1,n2,n3,n4):
    print("num1=",n1,"num2=",n2,"num3=",n3,"num4=",n4)
fun1(10,20,30,40)
#keyword arguement
def fun2(n1,n2,n3,n4):
    print("num1=",n1,"num2=",n2,"num3=",n3,"num4=",n4)
fun2(n2=10,n1=20,n4=30,n3=30)
#default arguements
def fun1(name,roll,branch="cse",college="GIET"):
    print(name,roll,branch,college)
fun1("mahee",153)
fun1("kavya",145,"ece")
fun1("vicky",165)
fun1("sneha",207)
fun1("adi",199,"cst")
#Variable Number of Arguement
def fun1(*var):
    for i in var:
        print(i,end=" ")
fun1(1,2,3)
print()
fun1(1,2,3,4)
print()
fun1(1,2,3,4,5)
print()
#addition using function
def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    return(sum)
print(add(10,30,60))
print(add(20,40))
#Q1
n1=int(input())
n2=int(input())
n3=int(input())
if n1==7:
    print(n2*n3)
elif n2==7:
    print(n3)
elif n3==7:
    print(-1)
else:
    print(n1*n2*n3)
#Q2
currency=input("name of the currency: ")
n=int(input("amount of money: "))
if currency=="Euro":
      print(n*0.01417)
elif (currency=="Brirish Pound"):
      print(n*0.0100)
elif (currency=="Australian Dollar"):
      print(n*0.02140)
elif (currency=="Canadian Dollar"):
      print(n*0.02027)
else:
      print(-1)
#Q3--write a python program to calculate the total amount of plane ticket booking
a=int(input("Amount of Adult: "))
c=int(input("Amount of children: "))
sum =(a*37550.0+c*12516.7)
tax=sum*(7/100)
total=sum+tax
discount=total*10/100
sum_total=total-discount
print("Total amount = ",sum_total)
#Q4
x=int(input("Number of 5 rs coins:"))
y=int(input("Number of 1 rs coins:"))
z=int(input("Amount of money needed to purchase:"))
possible_amount=x*5+y
if(z<=possible_amount):
    five_rs=int(z/5)
    one_rs=z%5
    print("no of 5rs and 1rs coins:",five_rs,one_rs,)
else:
    print(-1)'''

 


      
        


         
