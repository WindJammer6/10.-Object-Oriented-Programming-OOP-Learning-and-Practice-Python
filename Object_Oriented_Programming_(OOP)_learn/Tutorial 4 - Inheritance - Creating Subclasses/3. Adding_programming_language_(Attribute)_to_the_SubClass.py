class Employee:

    raised_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  

    def apply_raise(self):
       self.pay = int(self.pay * self.raised_amount)

    @classmethod
    def set_raised_amt(cls, amount):
        cls.raised_amount = amount


class Developer(Employee):

    raised_amount = 1.10

    #Sometimes we want to initiate more information than our parent Class can handle. To elaborate on
    #this, lets say we want to pass in 1 more attribute (apart from the first, last, and pay attributes)
    #on the Developer's main programming language. However, currently the parent 'Employee' Class
    #cannot cannot accept a 4th programming language attribute. To get around this, we have to give
    #our 'Developer' SubClass its own '__init__' method

    #This is how you give the 'Developer' SubClass its own '__init__' method (quite similar to how you'd
    #do for a normal Class)
    def __init__(self, first, last, pay, programming_language):

        #Normally, what you might be tempted to do is to copy-paste the whole chunk of attributes from
        #the parent 'Employee' Class (self.first = first, self.last = last ...). But you shouldn't
        #do that as you would want your code to be short and non-repetitive. This is what you can do
        #instead:

        #The 'super()' function (from the word 'superclass' (parent Class)) is used to reference to the
        #parent Class and the '.__init__' function is used to reference to the Class's attributes. This
        #code tells Python you want the 'Employee' Class to handle the first, last and pay attributes in
        #your 'Developer' SubClass
        super().__init__(first, last, pay)

        #This is another way you can do this, but not as good as 'super().__init__(first, last, pay)
        #as this one only works for SubClasses with single inheritance, but does not work for multiple
        #inheritance (will go through this concept later)
        #Employee.__init__(self, first, last, pay)

        #Here you have the 4th 'programming_language' attribute added in to the 'Developer' SubClass
        self.programming_language = programming_language     

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

dev_1 = Developer('John', 'Doe', 50000, 'Python')
dev_2 = Developer('Jane', 'Smith', 60000, 'Java')

print(dev_1.email)
print(dev_1.programming_language)


