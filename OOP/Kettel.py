"""
class:Template for creating objects.All objects created using the same class will have the same characteristic.
object:an instance of a class.
instantiate:create an instance of a class.
method:a function defined a class.
attributes:a variabel bound to an instance of a class.
"""

class Kettle(object):

    power_source='Electricity'#Class attribute that all the instances share, like static in c++ or java

    def __init__(self,make,price):#constructor
        self.make=make
        self.price=price
        self.on=False

    def switch(self):
        self.on=True


kenwood=Kettle('kenwood',8.55)#kenwood is referance variable
print(kenwood.make)
print(kenwood.price)

kenwood.price=12.75
print(kenwood.price)

hamilton=Kettle('Hamilton',14.55)
print(hamilton.make)
print(hamilton.price)
print('Model:{}={},{}={}'.format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))
print('Model:{0.make}={0.price},{1.make}={1.price}'.format(kenwood,hamilton))

print(hamilton.on)
hamilton.switch()
print(hamilton.on)

Kettle.switch(kenwood)#Calling without using instance
print(kenwood.on)

kenwood.power=3.5#We can create other variabels outside the class of a specific instance e.g.'kenwood'.
print(kenwood.power)
print('Model:{0.make}={0.power},{1.make}={1.price}'.format(kenwood,hamilton))

print('Switch to atomic power')
Kettle.power_source='Atomic'# power_source updated
kenwood.power_source='Gas'# Only kenwood power_source is updated
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
