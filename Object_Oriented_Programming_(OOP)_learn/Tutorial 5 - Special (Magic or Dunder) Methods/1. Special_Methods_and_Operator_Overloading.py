#What are Special (aka Magic/Dunder) Methods?
#Special Methods are a set of predefined methods you can use to enrich your classes. They let you emulate
#the behavior of built-in (existing) types in your own-made Classes and to implement Operator Overloading.
#You can find the full list of Special Methods online, but in this Tutorial we are only going to cover 
#these:
#--> __init__
#--> __repr__
#--> __str__ 
#--> __add__

#So technically these method/functions (like __add__ and __repr__) already exist in Python, like you can
#run them without any problems such as 'print(int.__add__(1, 2))' and 'print(emp_1.__repr__())'. However
#what makes them special is that they can also be modified/built-on to fit the needs of your Class by e.g.
#'def __repr__(self):' in your Class and modifying however you want below.

#Side note: Special Methods are commonly recognized by the double underscores in front and behind the
#function. Hence thats why they are sometimes called 'Dunder' (double under) Methods.

#////////////////////////////////////

#What is Operator Overloading (Polymorphism)?
#Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
#It is where Python allows the same operator name or symbol to be used for multiple operations/behave
#differently in different contexts. 
#e.g.
print(1 + 2)
print('a' + 'b')
print(['apple', 'orange'] + ['banana', 'grape'])

#From here, we can see that the '+' operator is used in multiple ways. It can be used to add two integers,
#join (concat) two strings and merge two lists. This is achieved because the '+' operator is overloaded 
#by an int class and str class. But where is the '__add__' Special Method? The '+' operator is actually
#just a representation of the '__add__' special method, and when the '+' operator is called, what actually
#going on is this:
print(int.__add__(1, 2))                                          #for '+' on integers
print(str.__add__('a', 'b'))                                      #for '+' on strings
print(list.__add__(['apple', 'orange'], ['banana', 'grape']))     #for '+' on lists
