class Animal:
    def walking(self,name):
        self.name=name
        print(f"{name} is walking")
class Dog(Animal):
    def eating(self,name1):
        self.name1=name1
        print(f"{name1} is a dog and it is eating")
dog1=Dog()
dog1.walking('Amit')
dog1.eating('Amit')
