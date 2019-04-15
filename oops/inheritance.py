class Employee:

    def __init__(self, first, last, pay):#this method will take instance of the class as it's first variable 
        self.first = first          #f or emp_1 it is acting as emp_1.first=first
                                    
        self.last = last            
        
        self.email = first + '.' + last + '@email.com'
        
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

class Developer(Employee):#in paranthesis name of the parent class
    
    def __init__(self,first,last,pay,prog_lang):
        
        super().__init__(first,last,pay)# Same as Down Method but useful for single lvel inheritance
        self.prog_lang=prog_lang    
        #Employee.__init__(self,first,last,pay) when we wnat to call __init__ method of parent class
        #In case of mutiple inheritance

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        
        super().__init__(first,last,pay)
        
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_name(self):
        for emp in self.employees:
            print('--->',emp.fullname())
        
    
    

    

emp_1 = Employee('sahib', 'singh', 50000)
emp_2 = Employee('berry', 'james', 60000)

print(emp_1.fullname()) #Output = sahib singh

#print(Employee.fullname(emp_1))

dev_1=Developer('beak','parrot',400,'python')#created obj. of Developer class without putting
#anything in class 

#using methods of Employee(Parent) class
#print(dev_1.fullname())

#using variables of Employee(Parent) class
#print(dev_1.prog_lang)


#help(Developer)

#this shows the Method resolution order(i.e in which order) information is seen 
#by python when we call any method or variable in class i.e

#---> First Developer Class
#---> Second Employee(Parent) class
#---> Third is  Builtin object class



mgr_1=Manager('JIMMY','COOK',90000,[emp_1])

#mgr_1.print_name()

mgr_1.add_emp(emp_2)

mgr_1.print_name()

#mgr_1.rem_emp(emp_1)

#mgr_1.print_name()
