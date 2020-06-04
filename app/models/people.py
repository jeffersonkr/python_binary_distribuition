class People:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return self._name

    @property
    def age(self):
        return self._age

    def eat(self):
        print(f'{self._name} is eating')

    def get_older(self, year=1):
        self._age += year
