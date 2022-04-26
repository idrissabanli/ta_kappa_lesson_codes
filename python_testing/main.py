# import datetime

# datetime.datetime.strptime()


# class Car:
#     engine = 3000

#     @classmethod
#     def change_engine(cls, new_engine):
#         cls.engine = new_engine

# bmw = Car()
# print(bmw.engine)

# Car.change_engine(4000)

# print(bmw.engine)
# merc = Car()

# print(merc.engine)


class Employee():

    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'
    
    @classmethod
    def read_from_str(cls, full_name_as_str):
        f_name, l_name = full_name_as_str.split()
        return cls(first_name=f_name, last_name=l_name)

ad_soyad = input('Ad, soyadinizi daxil edin: (AD SOYAD) ')

emp = Employee.read_from_str(ad_soyad)
ad_soyad = input('Ad, soyadinizi daxil edin: (AD SOYAD) ')

emp2 = Employee.read_from_str(ad_soyad)

print(emp.get_full_name())
print(emp2.get_full_name())
