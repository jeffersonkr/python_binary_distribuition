from models.people import People
import time

def create_and_use_people():
    person = People(name="Jefferson", age=30)
    print(person)
    print("testing sleep lib imported wait 1 sec")
    time.sleep(1)
    person.get_older()
    print(person.age)
    