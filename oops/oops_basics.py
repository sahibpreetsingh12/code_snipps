class Employee:

    def __init__(self, first, last, pay):#this method will take instance of the class as it's first variable 
        self.first = first          #f or emp_1 it is acting as emp_1.first=first
                                    
        self.last = last            
        
        self.email = first + '.' + last + '@email.com'
        
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('sahib', 'singh', 50000)
emp_2 = Employee('berry', 'james', 60000)

print(emp_1.fullname()) #Output = sahib singh

print(Employee.fullname(emp_1)) #Output = sahib singh
