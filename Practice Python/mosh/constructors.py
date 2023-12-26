class Person:
    def __init__(self,name):
        self.name = name
        print(f"Welcome {name}")
    def talk(self,name2,name1):
        self.name2=name2
        self.name1=name1
        print(f"{name1} is Talking dirty to {name2}")
person1 = Person('Amit')
person1.talk(name2='Tanishka',name1="Amit")