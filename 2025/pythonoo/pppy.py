import random
import time
class Animal:
    def talk(self):
        print("moo..heha..woof")
    def walk(self):
        print("Animal walk")
    def sleep(self):
        print("Animal Sleep")
class Cow(Animal):
    def talk(self):
        print("Moo…")
    def walk(self):
        print("Cow walk")
class Donkey(Animal):
    def talk(self):
        print("bray…")
class Dog(Animal):
    def talk(self):
        print("bark…")
    def walk(self):
        print("Dog walk..")
class Poodle(Dog):
    def talk(self):
        print("poodle bark..")
    def walk(self):
        print("poodle walk..")
if __name__ == "__main__":
    random.seed(time.time())
    animal_classes = [Cow, Donkey, Dog, Poodle]
    a = random.choice(animal_classes)()
    a.talk()
    a.walk()
    a.sleep()
