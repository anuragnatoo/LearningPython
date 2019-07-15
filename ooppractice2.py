class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def animalspeaks(self):
        print("hello! my name is",self.name)
    def whosyourowner(self):
        print("Path different!")

class Dog(animal):
    def __init__(self,name,age,owner):
        super().__init__(name,age)
        self.owner = owner
    def whosyourowner(self):
        print("My owner is",self.owner)

rocky = Dog("Rocky",4,"Luke")
rocky.animalspeaks()
rocky.whosyourowner()