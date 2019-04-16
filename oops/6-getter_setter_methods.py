class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property#we are defining email as a method in class but we using it as a attribute 
            # of the class using @property decorator
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter#setter methods in python using method.setter decorator
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'cook')
emp_1.fullname = "Ryan smith"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
