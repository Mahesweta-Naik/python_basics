'''#Q1
class example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        self.num=num

    def get_num(self):
        return self.num
obj=example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
#Q2
class customer:
    def __init__(self,id):
        self.id= 100
        
c1=customer(200)
print(c1.id)
#Q3
class book:
    def __init__(self):
        self.title=None
my_fav=book()
my_fav.title="Head First Programming"
your_fav=book()
your_fav.title="learn python the hard way"

my_fav.title="Learning Python"

print("my favorite is",my_fav.title)
print("your is",your_fav.title)
#Q4
class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material

    def __str__(self):
        return "Shoe with price:"+str(self.price)+" and material:"+self.material

s1=shoe(1000,"canvas")
print(s1)
print(s1.price,s1.material)
print("the unique id of the object",id(s1))
#Q5
class mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("displaying details")
    def purchase(self):
        self.display()
        print("calculating price")

mobile().purchase()
m1=mobile()
print(m1)
#Q6
class mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price*(discount/100)
        print("Total price of" ,self.brand,"mobile is",self.total_price)
    def amount_return(self):
        return (self.price-self.total_price) 
mob1=mobile("Apple",2000)
mob2=mobile("Samsung",2000)
mob1.purchase()
mob2.purchase()
#Q7
class customer:
             def __init__(self,cust_id,name,age,wallet_balance):
                          self.cust_id=cust_id
                          self.name=name
                          self.age=age
                          self.wallet_balance=wallet_balance
             def update_balance(self,amount):
                          if amount<1000 and amount>0:
                                       self.wallet_balance+=amount
             def show_balance(self):
                          print("The balance is",self.wallet_balance)
c1=customer(100,"Gopal",24,1000)
c1.update_balance(500)
c1.show_balance()
#Q8
class dam:
    def __init__(self,name,length):
                 self.name=name
                 self.__length=length
    def get_length(self):
                 return self.__length
dam1=dam("abc dam:",3.5)
print("dam name:",dam1.name)
print("dam length:",dam1.get_length())
#Q9
class table:
             
             def assign_data(self,glass_top,wooden_top):
                          self.__glass_top=glass_top
                          self.__wooden_top=wooden_top
             def identity_rate(self,glass_top,wooden_top):
                          self.assign_data(glass_top,wooden_top)
             if(self.__glass_top==True):
                          rate=20000
             elif(self.__wooden_top==True):
                          rate=30000
             else:
                          rate=0
             return rate
dining_table=table()
rate-dining_table.identity_rate(False,True)
print(rate)
#Q10
class Vehicle:
             def __init__(self,id,cost,type):
                     self.__vehicle_cost = cost
                     self.__vehicle_id = id
                     self.__vehicle_premium_amount = None
                     self.__vehicle_type = type
             def set_vehicle_id(self,vehicle_id):
                     self.__vehicle_id = vehicle_id
             def set_vehicle_cost(self,vehicle_cost):
                     
                     self.__vehicle_cost = vehicle_cost
             def set_vehicle_amount(self,vehicle_premium_amount):
                     
                     self.__vehicle_premium_amount = vehicle_premium_amount
             def get_vehicle_id(self):
                     
                     return self.__vehicle_id
             def get_vehicle_type(self):
                     
                     return self.__vehicle_type
             def get_vehicle_cost(self):
                     
                     return self.__vehicle_cost
             def get_vehicle_amount(self):
                     
                     return self.__vehicle_premium_amount
             def calculate_premium(self):
                     
                     if self.__vehicle_type=="two_wheeler":
                             
                             self.__vehicle_premium_amount=self.__vehicle_cost*2/100
                     elif self.__vehicle_type=="Four_wheeler":
                             self.__vehicle_premium_amount=self.__vehicle_cost*6/100
                     else:
                             print("Invalid vehicle Type")
             def display_vehicle_details(self):
                     print(self.__vehicle_type,self.__vehicle_cost,self.__vehicle_premium_amount)


v = Vehicle(123,1234,"two_wheeler")
v.calculate_premium()
v.display_vehicle_details()
#Q11
class student:
        def __init__(self):
                self.__student_id=None
                self.__age=None
                self.__marks=None
        def set_student_id(self,student_id):
                self.__student_id=student_id
        def set_age(self,age):
                self.__age=age
        def set_marks(self,marks):
                self.__marks=marks
                
        def get_student_id(self):
                return self.__student_id
        def get_age(self):
                return self.__age
        def get_marks(self):
                return self.marks

        def validate_mark(self):
                if self.__marks>=0 and self.__marks<=100:
                        return True
                else:
                        return False
        def validate_age(self):
                if self.__age>=20:
                        return True
                else:
                        False

        def check_qualification(self):
                if self.validate_mark() and self.validate_age():
                        if self.__marks>=65:
                                return True
                        else:
                                return False
        def display(self):
                print(self.__student_id,self.__age,self.__marks)
                 
s=student()
s.set_student_id(101)
s.set_age(21)
s.set_marks(66)
print(s.check_qualification())
s.display()
#Q12
class student:
        def __init__(self):
                self.__student_id=None
                self.__age=None
                self.__marks=None
                self.__course_id=None
                self.__fees=None
        def set_student_id(self,student_id):
                self.__student_id=student_id
        def set_age(self,age):
                self.__age=age
        def set_marks(self,marks):
                self.__marks=marks
        def set_marks(self,marks):
                self.__marks=marks
                
        def get_student_id(self):
                return self.__student_id
        def get_age(self):
                return self.__age
        def get_marks(self):
                return self.marks

        def validate_mark(self):
                if self.__marks>=0 and self.__marks<=100:
                        return True
                else:
                        return False
        def validate_age(self):
                if self.__age>=20:
                        return True
                else:
                        False

        def check_qualification(self):
                if self.validate_mark() and self.validate_age():
                        if self.__marks>=65:
                                return True
                        else:
                                return False'''

#Q3
class customer:
        def __init__(self,cust_name,quantity):
                self.__cust_name=cust_name
                self.__quantity=quantity
        def set_cust_name(self,cust_name):
                self.__cust_name=cust_name
        def set_quantity(self,quantity):
                self.__quantity=quantity
        def get_cust_name(self):
                return self.__cust_name
        def get_quantity(self):
                return self.quantity

        def validate_quantity(self):
                if self.__quantity in range(1,6):
                        return True
                else:
                        return False
class pizzaService:
        counter=100
        def __init__(self,customer,pizza_type,toppings):
                self.__customer=customer
                self.__pizza_type=pizza_type
                self.__toppings=toppings
                self.__service_id=None
                self.__cost=0

        def set_customer(self,customer):
                self.__customer=customer
        def set_pizza_type(self,pizza_type):
                self.__pizaa_type=pizza_type
        def set_toppings(self,toppings):
                self.__toppings=toppings
        def get_customer(self):
                return self.__customer
        def get_pizza_type(self):
                return self.__pizza_type
        def get_toppings(self):
                return self.__toppings
        def validate_pizza_type(self):
                if self.__pizza_type.l in pizza:
                        return True
                else:
                        return False
        
        
        
                
                
        
                


        





                
                
                                       
                                       
                          
                          
             
 
