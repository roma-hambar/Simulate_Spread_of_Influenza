"""
Assignment 2 task 1
Written by Roma Hambar (31223958) for FIT9136
Created on 14/05/2020
Last Date Modified: 06/06/2020
Description: To simulate the social links between people from the given set of data which represents the list of friends
a person has. Here, we use class Person which would be unique for each individual and will have details such as
first_name, last_name and his friends.
In this task, we will generate a list of all Person objects from the given file records.
"""

class Person:
    # Create a list of all the instances of Person Object that have been created in this simulation.
    instances = []

    # __init__ method is built-in method of object class to call an instance of the class Person.
    # The Person object has the following attributes:
    # 1. first_name : First name of the Person
    # 2. last_name : Last name of the Person
    # 3. friends[] : List of Friends (Person) objects which will be populated in the load_people() function
    # 4. instances[] : List of Person Objects till the current simulation time to avoid duplicate objects of the same
    # person.
    # Populate the newly created instance of Person object in instances list.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []
        self.__class__.instances.append(self)

    # add_friend method is used to append the Friend (Person) object to the friends[] list in every Person Object.
    def add_friend(self, friend_person):
        self.friends.append(friend_person)

    # get_name method is used to return the first_name and last_name of the Person object.
    def get_name(self):
        return self.first_name + ' ' + self.last_name

    # get_friends method is used to return a list of all the Friends (Person) names that a Person has.
    # Here, we extract the nam eof the Friend object's name and return all the names in the form of a list.
    def get_friends(self):
        friends_list = []
        for i in self.friends:
            friends_list.append(i.first_name+" "+i.last_name)
        return friends_list

    # __new__ method is used to create a new instance of the class Person cls by invoking the __init__ method to create
    # new object. super method is used to reference to the parent class referenced by cls.
    # @classmethod
    def __new__(cls, first_name, last_name):
        instance = super(Person, cls).__new__(cls)
        return instance

    # getPersonInstances method will return the existing Person objects with first_name and last_name given.
    # This method is invoked when we create Friends objects or when the simulation is executed again.
    @classmethod
    def getPersonInstances(cls, first_name, last_name):
        for instance in cls.instances:
            if (instance.first_name == first_name and instance.last_name == last_name):
                return instance

    # printInstances method will return all the instances of the Person object taht have been created and stores in
    # instances list.
    @classmethod
    def printPersonInstances(cls):
        for instance in cls.instances:
            print(instance, instance.__dict__)

# load_people function is used to read the file records from a2_sample_set.txt, get the names of people involved in
# the simulation model, create theor Person object based on their obtained names.
# Read the names of all the friends that the Person object has, check if the Friend(Person) object was already created
# and then store all the Friends object in friends[] that every Person has.
def load_people():
    file = open('a2_sample_set.txt', 'r')
    data = file.readlines()
    # Initialize lists for storing names of people involved in the simulation, store newly created Person objects.
    # store names of Friends of each individual.
    person_name_list = []
    person_list = []
    friend_list = []
    # Read file records line by line
    for lines in data:
        lines = lines.replace('\n', '')
        # Names of all individuals are stored.
        person_name_list.append(lines.split(":")[0])
        # Names of all the friends corresponding to each individual are stored in the form of lists inside the list.
        friend_list.append(lines.split(":")[1])
    # Using the person_name_list created, we will create Person object instances using first_name and last_name and
    # store them in person_list
    for person_name in person_name_list:
        first_name, last_name = person_name.split(" ")[0], person_name.split(' ')[1]
        if Person.getPersonInstances(first_name, last_name):
            person_list.append(Person.getPersonInstances(first_name, last_name))
        else:
            person_list.append(Person(first_name, last_name))

    # Get instances of already created Person object to populate Friends object list by first_name and last_name of the
    # Person object and populate the friends list of each Person with corresponding Friend(Person) objects.
    for rows in range(0,len(person_name_list)):
        person_name = person_list[rows]
        friends = [friend_list[rows]]
        for f in friends:
            f_list = f.split(",")
            for names in f_list:
                f_name, l_name = names.split(' ')[1], names.split(' ')[2]
                person_name.add_friend(Person.getPersonInstances(f_name, l_name))
    file.close()
    return person_list

if __name__ == '__main__':
    print(load_people())