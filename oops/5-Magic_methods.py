class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):#if we want too add salary of employees just by giving their names
        #we have to create a custom method for ourselves
        return self.pay + other.pay

    def __len__(self):#if we want find length of name of employees just by giving their name
        #we have to create a custom method for ourselves
        return len(self.fullname())


emp_1 = Employee('sahib', 'singh', 50000)
emp_2 = Employee('Brian', 'Giggs', 60000)

# print(emp_1 + emp_2)

print(len(emp_1))
