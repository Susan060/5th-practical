##with open("example1.txt","a")as file:
##        num=int(input("enter the number of lines"))
##        for i in range(num):
##         line=input("enter a line :")
##         content=file.write(line+"\n")

##num=int(input("enter the line number you need to delete"))
##with open("example1.txt","r") as file:
##        lines=file.readlines()
##        print(lines)
##print("After deletion")
##if 0<num<=len(lines):
##        del lines[num-1]
##with open('example1.txt','w') as file:
##        print(lines)
##        file.writelines(lines)


##import os
##if os.path.exists("example.txt"):
##    print("the file exists")
##


##class Bankaccount:
##        def __init__(self,ac_holder,balance):
##                self.ac_holder=ac_holder
##                self.balance=balance
##        def deposit(self,amount):
##                if amount>0:
##                        self.balance+=amount
##                        print("The deposited balance is ",amount," and new balance ",self.balance)
##                else:
##                        print("The deposited balance must be positive")
##        def withdraw(self,amount):
##                if amount>0:
##                        if amount<=self.balance:
##                                self.balance-=amount
##                                print("Withdarwn amount is ",amount, " and new balance is ",self.balance)
##                        else:
##                                print("Insufficient balance")
##
##                else:
##                        print("Withdrawal amount must be positive.")
##        def get_balance(self):
##                return self.balance
##
##account=Bankaccount("Alice",3000)
##account.deposit(1000)
##account.withdraw(500)
##print("Final Balance: ",account.get_balance())



##class Rectangle:
##        def __init__(self,length,breadth):
##                self.length=length
##                self.breadth=breadth
##        def area(self):
##                area=self.length*self.breadth
##                print("The area of the rectangle is ",area)
##        def perimeter(self):
##                perimeter=2*(self.length+self.breadth)
##                print("The perimeter of the rectangle is ",perimeter)
##
##r=Rectangle(10,5)
##r.area()
##r.perimeter()


##class Complexnumber:
##        def __init__(self,real,imag):
##                self.real=real
##                self.imag=imag
##        def __add__(self,other):
##                real_part=self.real+other.real
##                imag_part=self.imag+other.imag
##                return Complexnumber(real_part,imag_part)
##        def __mul__(self,other):
##                real_part=self.real*other.real
##                imag_part=self.imag*other.imag
##                return Complexnumber(real_part,imag_part)
##        def __repr__(self):
##                return f"{self.real}+{self.imag}i" if self.imag >=0 else f"{self.real}+{self.imag}i"
##complex1=Complexnumber(2,3)
##complex2=Complexnumber(1,4)
##
##result_add=complex1+complex2
##result_mul=complex1*complex2
##print("Addition is ",result_add)
##print("Multiplication is ",result_mul)

##class Calculator:
##        def add(self, *args):
##                total=0
##                for num in args:
##                        total+=num
##                return total
##calc=Calculator()
##result1=calc.add(1,2)
##result2=calc.add(5,10,15)
##result3=calc.add(100,220,300,400)
##
##print("The result of first parameter is ",result1)
##print("The result of second parameter is ",result2)
##print("The result of third parameter is ",result3)

##class Animal:
##    def __init__(self, name, age):
##        self.name = name
##        self.age = age    
##    
##    def speak(self):
##        return print(self.name,"makes sound")
##
##class Dog(Animal):
##    def __init__(self, name, age, breed):
##        super().__init__(name, age)
##        self.breed = breed
##
##    def speak(self):
##        return print(self.name," barks")
##
##class Cat(Animal):
##    def __init__(self, name, age, color):
##        super().__init__(name, age)
##        self.color = color  
##    
##    def speak(self):
##        return print(self.name," meow")
##
##
##dog = Dog("Buddy", 3, "Golden Retriever")
##cat = Cat("Whiskers", 2, "Black")
##
##print(dog.name ," is a",dog.age," year-old",dog.breed, " dog.", dog.speak())
##print(cat.name ," is a",cat.age," year-old",cat.color, " dog.", cat.speak())

##n=int(input("enter a number"))
##try:
##        x=n/0
##except:
##        print("DIVISIONBYZERO!")
##else:
##        print("no error occured")
##finally:
##        print("This will always run")

##def handleexception():
##        try:
##                with open("Nofile.txt","r")as file:
##                        content=file.read()
##                numbers=[1,2,3]
##                print(numbers[5])
##
##                user_input="abc"
##                result=int(user_input)
##
##        except FileNotFoundError:
##                print("NoFile.txt was not found")
##
##        except IndexError:
##                print("Error: Index out of range")
##
##        except ValueError:
##                print("Error: Invalid value entered. Could not convert to an int")
##        else:
##                print("No error occured")
##        finally:
##                print("This always Executes")
##handleexception()


##class MyCustomError(Exception):
##    pass
##def check_value(value):
##    if value < 0:
##        raise MyCustomError("Value cannot be negative!")
##    return print(value," is not valid") 
##
##try:
##    print(check_value(-5))
##except MyCustomError as e:
##    print(f"Error: {e}")


##class Stack:
##        def __init__(self):
##                self.stack=[]
##        def push(self,item):
##                self.stack.append(item)
##        def pop(self):
##                if not self.is_empty():
##                        return self.stack.pop()
##                else:
##                        return "Stack is Empty"
##        def peek(self):
##                if not self.is_empty():
##                        return self.stack[-1]
##                else:
##                        return "Stack is empty"
##        def is_empty(self):
##                return len(self.stack)==0
##        def size(self):
##                return len(self.stack)
##
##stack=Stack()
##stack.push(10)
##stack.push(13)
##stack.push(14)
##
##print("Top item: ",stack.peek())
##print("Stack Size: ",stack.size())
##print("Popped item ",stack.pop())
##print("Stack size after pop ",stack.size())
##print("Is the stack empty? ",stack.is_empty())


##class Queue:
##    def __init__(self):
##        self.queue = []
##    def enqueue(self, item):
##        self.queue.append(item)
##    def dequeue(self):
##        if not self.is_empty():  
##            return self.queue.pop(0)
##        else:
##            return "Queue is empty!"
##    def peek(self):
##        if not self.is_empty():
##            return self.queue[0]
##        else:
##            return "Queue is empty!"
##    def is_empty(self):
##        return len(self.queue) == 0
##    def size(self):
##        return len(self.queue)
##
##
##queue = Queue()
##
##queue.enqueue(10)
##queue.enqueue(20)
##queue.enqueue(30)
##
##print("Front item:", queue.peek())
##print("Queue size:", queue.size())  
##
##print("Dequeued item:", queue.dequeue())  
##print("Queue size after dequeue:", queue.size())  
##print("Is the queue empty?", queue.is_empty())  




##def find_duplicates(input_list):
##    duplicates = []  
##    for i in range(len(input_list)):
##        if input_list[i] in input_list[:i]:  
##            duplicates.append(input_list[i])
##    return duplicates
##
##input_list = [1, 2, 3, 4, 2, 5, 3, 6, 7, 8, 6]
##duplicates = find_duplicates(input_list)
##print("The original list is ",input_list)
##print("Duplicates in the list:", duplicates)


##my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 40}
##sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
##print("The original dictionary ",my_dict)
##print("Dictionary sorted by values (ascending):", sorted_dict)

##def count_occurrences(tup):
##    count_dict = {}
##    
##    for item in tup:
##        if item in count_dict:
##            count_dict[item] += 1
##        else:
##            count_dict[item] = 1
##    
##    return count_dict
##
##my_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
##
##print("The tuple is ",my_tuple)
##result = count_occurrences(my_tuple)
##print("The number of occurence of element is",result)



##import numpy as np
##a=np.random.randint(50,size=(3,3))
##b=np.random.randint(50,size=(3,3))
##print("Addition is:")
##print(a+b)
##print("Substraction is:")
##print(a-b)
##print("Element wise :")
##print(a*b)
##print("Dot wise :")
####print(np.dot(a,b))



##import numpy as np
##array=np.random.randint(10,101,size=50)
##mean=np.mean(array)
##median=np.median(array)
##std_deviation=np.std(array)
##variance=np.var(array)
##
##print("Array:",array)
##print("Mean:",mean)
##print("Standard Deviation:",std_deviation)
##print("Variance:",variance)




##import numpy as np
##array=np.random.randint(10,101,size=(4,5))
##print("Array is: ")
##print(array)
##print("All rows")
##row=array[:]
##second_col=array[:,1]
##print(row)
##print("Second column")
##print(second_col)
##print("elements greater than 20")
##elem=array[array>20]
##print(elem)
##sub_2x3=array[:2,:3]
##sub_1x3=array[:1,:3]
##print("sub matrix 2x3 is ",sub_2x3)
##print("sub matrix 1x3 is ",sub_1x3)



##import numpy as np
##import matplotlib.pyplot as plt
##x=np.random.rand(100)
##y=np.random.rand(100)
##plt.scatter(x,y,color='blue',marker='o',edgecolors='black')
##plt.title("Scatter plot of random points")
##plt.xlabel('X values')
##plt.ylabel('Y values')
##plt.show()
          
##import numpy as np
##import matplotlib.pyplot as plt
##x=np.linspace(-10,10,400)
##y1=x**2
##y2=x**3
##plt.plot(x,y1,label='y=x^2',linestyle='-',color='blue')
##plt.plot(x,y2,label='y=x^3',linestyle='--',color='red')
##plt.legend()
##plt.xlabel('x')
##plt.ylabel('y')
##plt.title("plot of y=x2 and y=x3")
##plt.grid(True)
##plt.show()


##import pandas as pd
##data={'Name':['Ram','Hari','shyam'],'Math':[76, 95, 91],'Science':[98, 82, 96],'Computer':[99, 64, 32]}
##df=pd.DataFrame(data)
##print(df)
##print("The average of all three subjects are:")
##print(df['Math'].mean()," for Math")
##print(df['Science'].mean()," for science")
##print(df['Computer'].mean()," for computer")
##print("After a grade  column was added:")
##df['Total marks']=df['Math']+df['Science']+df['Computer']
##
##def grade(marks):
##    if marks>=270:
##        return 'A'
##    elif marks>=240:
##        return 'B'
##    else:
##        return 'C'
##df['Grade']=df['Total marks'].apply(grade)
##print(" DataFrame with grades")
##print(df)
##
##A=df[df['Grade'] =='A']
##
##print("The Filtered dataframe where grade is A ")
##print(A)

##import numpy as np
##array_1d = np.array([1, 2, 3, 4, 5])
##array_2d = np.array([[6, 7, 8, 9, 10],
##                     [11, 12, 13, 14, 15],
##                     [16, 17, 18, 19, 20]])
##
##add = array_2d + array_1d
##mul = array_2d * array_1d
##
##print("Element-wise Addition Result:")
##print(add)
##
##print("\nElement-wise Multiplication Result:")
##print(mul)


##import numpy as np
##A=np.array([[2,1,1],[1,2,3],[3,1,2]])
##B=np.array([1,7,4])
##solution=np.linalg.solve(A,B)
##print("The value of x ,y and z are",solution,"respectively.")


##import numpy as np
##import matplotlib.pyplot as plt
##x = np.linspace(0, 2 * np.pi, 100)
##y = np.sin(x)
##plt.plot(x, y, label='y = sin(x)')
##plt.title('Plot of y = sin(x)')
##plt.xlabel('x')
##plt.ylabel('y')
##plt.legend()
##plt.show()





##import pandas as pd
##df = pd.read_csv('employees.csv')
##top= df.nlargest(5, 'SALARY')
##print("Top 5 Highest Paid Employees:")
##print(top)
##average_salary_by_department = df.groupby('DEPARTMENT_ID')['SALARY'].mean()
##print("\nAverage Salary by Department:")
##print(average_salary_by_department)

lcount=0
wcount=0
with open("example1.txt","r") as file:
    for line in file:
        lcount+=1
        words=line.split()
        wcount=wcount+len(words)
print("Number of lines is : ",lcount)
print("Number of words is : ", 12)








      
