class Person:
  num = 1
  def __init__(b, name, age):
    b.name = name
    b.age = age

  def myfunc(a):
    print("Hello my name is " + a.name)

p1 = Person("Vijay", 36)
p1.myfunc()

p1.age=40
print("Age is %d"%p1.age)
print("Num is %d"%Person.num)


def create_adder(x): 
    def adder(y): 
        return x+y 
  
    return adder 

print(create_adder(15))  
add_15 = create_adder(15) 
  
print (add_15(10))
