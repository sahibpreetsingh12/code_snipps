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
    
    @classmethod #decorator to make classmethods
    #instead of regular methods which take instance of class as the first argument
    def from_string(cls,name): #first argument is class name
        first,last,pay=name.split('-')
        return cls(first,last,pay)
    
    @staticmethod #static methods are used when we are not accessing class or object of class
    #inside a method
    def check_day(dates):
        if dates.weekday()==5 or dates.weekday()==6:
            return False
        return True
        

emp_1 = Employee('sahib', 'singh', 50000) #emp_1 is the instance of the class Employee
emp_2 = Employee('berry', 'james', 60000)

#if isinstance(emp_2,Employee):#to check if object is instance of the class
#    print('True')

    
name1='sahib-singh-40000'

emp_3=Employee.from_string(name1)

if isinstance(emp_3,Employee):#to check if object is instance of the class
    print('True you are the employee')


import datetime
day=datetime.date(2019,4,15)

print(emp_1.check_day(day))#this shows static method can be accessed by instance of the class
print(Employee.check_day(day))#this shows static method can be accessed directly by the class

