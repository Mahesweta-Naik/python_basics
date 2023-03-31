'''#Traversing a linked list(single linked list)
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval

    def Atbegining(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode

    def Atend(self,newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        laste=self.headval
        while(laste.nextval):
            laste=laste.nextval
        laste.nextval=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("the mentoined node is absent")
        NewNode=Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval=NewNode
        
            
        
list = SLinkedlist()
list.headval=Node("mon")
e2=Node("tue")
e3=Node("wed")

#link 1st node to 2nd node
list.headval.nextval = e2

#link 2nd node to 3rd node
e2.nextval = e3

list.Atbegining("sun")

list.Atend("thus")
list.Inbetween(list.headval.nextval.nextval,"fri")
list.listprint()
#deletenode
class Node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.start_node = None
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item," ")
                n=n.ref
    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.ref = self.start_node
        self.start_node=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
        while n.ref is not None:
            n=n.ref
        n.ref=new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("list has no element")
            return
        self.start_node=self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("list has no element")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None

    def delete_element_by_value(self,x):
        if self.start_node is None:
            print("list has no element")
            return
        if self.start_node.item==x:
            self.start_node = self.start_node.ref
            return

        n= self.start_node
        while n.ref is not None:
            if n.ref.item==x:
                break
            n=n.ref

        if n.ref is None:
            print("item is not found")
        else:
            n.ref=n.ref.ref

    def search_item(self,x):
        if self.start_node is None:
            print("list has no element")
            return
        n=self.start_node
        while n is not None:
            if n.item==x:
                print("item found")
                return True
            n=n.ref
        print("item not found")
        return False           
         
    def get_count(self):
         if self.start_node is None:
             return 0
         n=self.start_node
         count = 0
         while n is not None:
            count= count+1
            n=n.ref
         return count

    def insert_at_index(self,index,data):
        if index==1:
            new_node=Node(data)
            new_node.ref=self.start_node
            self.start_node=new_node
        i=1
        n=self.start_node
        while i<index-1 and n is not None:
            n=n.ref
            i=i+1
        if n is None:
            print("index out of bound")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
            
new=Linkedlist()
new.insert_at_end(5)
new.insert_at_end(10)
new.insert_at_end(15)
new.insert_at_end(20)
new.insert_at_end(25)
new.insert_at_end(30)
new.insert_at_end(35)
new.insert_at_end(40)
new.insert_at_end(45)
new.traverse_list()
new.delete_at_start()
print("after deletion at the begining")
new.traverse_list()
new.delete_at_end()
print("after deletion at the end")
new.traverse_list()
new.delete_element_by_value(30)
print("after deleting specifiied value")
new.traverse_list()
new.search_item(5)

new.search_item(25)
print("no of nodes:",new.get_count())
new.insert_at_index(3,8)
new.traverse_list()
#double linked list
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
            temp=self.head
            count=0
            while temp is not None:
                temp=temp.next
                count+=1
            return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous=new_node
            self.head=new_node

    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtbegining(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.previous=temp

    def insertAtposition(self,value,position):
        temp=self.head
        count=0
        while temp is not None:
            if count==position-1:
                break
            count+=1
            temp=temp.next
        if position==1:
            self.insertAtBegining(value)
        elif temp is None:
            print("there are less than -1 element in the linked list")
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node=Node(value)#1500
            new_node.next=temp.next#2000
            new_node.previous=temp
            temp.next.previous=new_node
            temp.next=new_node

    def deleteFromBegining(self):
        if self.isEmpty():
            print("linked list is empty")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.previous=None

    def deleteFromLast(self):
        if self.isEmpty():
            print("linked list is empty")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None

    def deleteFromPosition(self,position):
         if self.isEmpty():
            print("linked list is empty")
         elif position == 1:
             self.deleteFromBegining()
         else:
             temp=self.head
             count=1
             while temp is not None:
                 if count == position:
                     break
                 temp=temp.next
                 count=count+1
             if temp is None:
                 print("there are less elemnt than {} in the linked list")
             elif temp.next is None:
                 self.deleteFromLast()
             temp.previous.next=temp.next
             temp.next.previous=temp.previous
             temp.next=None
             temp.previous=None
                                
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp = temp.next

x=DoubleLinkedList()
print(x.isEmpty())
x.insertAtBegining(5)
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.insertAtEnd(0)
x.printLinkedList()

x.deleteFromPosition(1)
x.printLinkedList()'''

#a python function which accepts 2 linked lists cointaing interger data and an integer, n
#and merges 2 linked lists, such that list2 is mergerd with list1 after n numbers of node

'''class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def merge_lists(self, list1, list2, n):
        current_node = list1.head
        for i in range(n-1):
            if not current_node:
                return "List 1 is too short!"
            current_node = current_node.next
        if not current_node:
            return "List 1 is too short!"
        temp = current_node.next
        current_node.next = list2.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = temp

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


# create first linked list
list1 = LinkedList()
list1.insert(1)
list1.insert(2)
list1.insert(4)
list1.insert(3)
list1.insert(5)

# create second linked list
list2 = LinkedList()
list2.insert(9)
list2.insert(8)
list2.insert(11)

# merge list2 with list1 after n=2 nodes
list1.merge_lists(list1, list2, 2)

# display merged linked list
list1.display()'''

#Q2--original list (12 95 140 110 40) new list (12 95 100 110 40),replace with max no
'''class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def replace_max(self, new_data):
        if not self.head:
            return "List is empty!"
        max_node = self.head
        curr_node = self.head.next
        while curr_node:
            if curr_node.data > max_node.data:
                max_node = curr_node
            curr_node = curr_node.next
        max_node.data = new_data

    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


# create linked list
list1 = LinkedList()
list1.insert(12)
list1.insert(95)
list1.insert(140)
list1.insert(110)
list1.insert(40)

# replace maximum element with new value
list1.replace_max(100)

# display modified linked list
list1.display()'''

#retrive all the data(name, age, gender) present in a queue by  males and females
'''class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def get_people_by_gender(self, gender):
        people = []
        for person in self.items:
            if person.gender == gender:
                people.append(person)
        return people

q = Queue()
q.enqueue(Person('Alice', 25, 'female'))
q.enqueue(Person('Bob', 30, 'male'))
q.enqueue(Person('Charlie', 20, 'male'))
q.enqueue(Person('David', 27, 'male'))
q.enqueue(Person('Eve', 22, 'female'))

people = q.get_people_by_gender('female')
if people:
    for person in people:
        print(f"Name: {person.name}, Age: {person.age}, Gender: {person.gender}")
else:
    print("No people of the given gender found in the queue.")'''
