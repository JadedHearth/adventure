#!/usr/bin/python
x = "."

class Parent():        # define parent class
   def twoplustwo(self):
      global x
      print('I say 2 + 2 ='+" "+str(2 + 2)+ x)
      if x == ",":
          print("and that is final!")

class Child(Parent): # define child class
   def twoplustwo(self):
      print('No 2 + 2 = fish!')
      global x
      x = ","

p = Parent()            # instance of parent
p.twoplustwo()          # parent calls method

c = Child()             # instance of child
c.twoplustwo()          # child calls overridden method

p.twoplustwo()          # parent method still exists
