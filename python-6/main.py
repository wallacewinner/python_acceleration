from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_department(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return True


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.__code = code
        self.__name = name
        self.__salary = salary

    @abstractmethod
    def calc_bonus(self):
        return self.__salary * 0.15

    @staticmethod
    def get_hours(self):
        return 8


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('managers', 1)

    def calc_bonus(self):
        return self.__salary * 0.15

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, name):
        self.__departament.name = name
        return True


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__departament = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sale(self):
        return self.__sales

    def put_sale(self, sale):
        self.__sales += sale
        return True

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, name):
        self.__departament.name = name
        return True
