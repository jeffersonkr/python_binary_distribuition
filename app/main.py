from python_example import create_and_use_people
from models.people import People

if __name__ == "__main__":
    create_and_use_people()
    josue = People(name='josue', age=10)
    print(josue)
    print(josue.age)