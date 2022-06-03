# def cem(a, b):
#     print(a+b)


class Person:
    # __age = 0
    _age = 0

    def __init__(self, name):
        self.first_name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.__age:
            raise ValueError('lsdkfnlsdn')
        self.__age = value

    # def move(self):
    #     print(self.first_name)


class Resul(Person):

    def __birthday(self):
        self._age = 3

p = Person(name='Resul')
print(p.age)

p.age = p.age + 1

print(p.age)
p.age += 1

print(p.age)
p.age -= 1


# # class Animal:

# #     def sound(self):
# #         print('...')


# # class Pet:

# #     def sound(self):
# #         print('Feed me')


# # class Dog(Animal, Pet):

# #     def sound(self):
# #         print('Hav hav')
# #         super(Animal, self).sound()
    
# # # animal = Animal()
# # # animal.sound()

# # dog = Dog()
# # dog.sound()