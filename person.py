


class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

    def introduce(self):
        print(f"I am {self.name}, my age is {self.age}, my height is {self.height}")

