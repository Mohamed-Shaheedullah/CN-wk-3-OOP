#
from person import Person

from superhero import Superhero

liam = Person("Liam", 30, "Tall")

# SOLID
# S single responsibility
# 

print(liam.height)
print(liam.age)
print(liam.name)
print(" ")
raf = Person("Raf", 58, "Short")
print(raf.name)
print(raf.age)
print(raf.height)

print(f"I am {raf.name}, my age is {raf.age}, my height is {raf.height}")


superman =Superhero("Superman", "Clark Kent", "Strength", "Lex Luthor")
batman = Superhero("Batman", "Bruce Wayne", "Agility", "Kingpin" )
drstrange = Superhero("Dr Strange", "Stephen Strange", "Magic", "Mephisto")
ironman = Superhero("Iron Man", "Tony Stark", "Armour", "Titanium Man")
print(" ")

print(f"I am {superman.name}, my power is {superman.power}, my name is {superman.identity}, my enmy is {superman.enemy}")

print(f"I am {ironman.name}, my power is {ironman.power}, my name is {ironman.identity}, my enmy is {ironman.enemy}")

print(f"I am {batman.name}, my power is {batman.power}, my name is {batman.identity}, my enmy is {batman.enemy}")

print(f"I am {drstrange.name}, my power is {drstrange.power}, my name is {drstrange.identity}, my enmy is {drstrange.enemy}")
print(" ")
print(" ")
liam.introduce()
print(" ")
print(" ")
ironman.introduce()

drstrange.name_length()
print(" ")
print(" ")

# O in solid meanns open closed principle
#
#
#### setters
# ironman.set_lair("Stark Industries")

# print(ironman.lair)

print(ironman.get_power())