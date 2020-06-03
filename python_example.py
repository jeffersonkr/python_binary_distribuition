from models.people import People

def create_and_use_people():
    person = People(name="Jefferson", age=30)
    print(person)
    person.get_older()
    print(person.age)