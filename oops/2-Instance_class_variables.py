class Employee:
    raise_amount=1.04# class variable
    
    def __init__(self, first, last, pay):#this method will take instance of the class as it's first variable 
        self.first = first          #f or emp_1 it is acting as emp_1.first=first
                                    
        self.last = last            
        
        self.email = first + '.' + last + '@email.com'
        
        self.pay = pay

    def fullname(self): #self is actually object(instance) that is calling this method in the class
        return '{} {}'.format(self.first, self.last)
        
    def raise_salary(self):
        self.pay=int(self.pay*self.raise_amount)
        #we can access the class variables using name of the class or the instance the class
        #i.e is either Employee.raise_amount or self.raise_amount
        return self.pay

emp_1 = Employee('sahib', 'singh', 50000) #emp_1 is the instance of the class Employee
emp_2 = Employee('berry', 'james', 60000)

print(emp_1.fullname()) #Output = sahib singh

print(Employee.fullname(emp_1)) #Output = sahib singh

print(emp_1.raise_salary())
#During this first we chck that variable is instance variable then it is checked wthether it is Class variable

#To confirm this we can check the namespace of the instance of the class using :-
#print(emp_1.__dict__) as there is no variable raise_amount here in this dictionaary

print(Employee.raise_amount)
#but when we check namespace of class we namespace of class using 
#print(Employee.__dict__) we will find that raise_amount variable

#Employee.raise_amount=1.05 
#changes the value for class variable

#print(emp_1.raise_amount)


#but 
emp_1.raise_amount=1.066
#will change the value for only that point of  time this is prooved by using these commands




print(emp_1.__dict__)  
#now namespace of emp_1 will not contain the value till we change it

