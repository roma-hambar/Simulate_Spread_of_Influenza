"""
Assignment 2 task 2
Written by Roma Hambar (31223958) for FIT9136
Created on 14/05/2020
Last Date Modified: 06/06/2020
Description: To simulate the spread of Influenza virus among a set of 200 people who have a set of Friends as given in
the a2_sample_set.txt. In this simulation, we denote the health of patient in terms of health points ranging from 0-100
where 0 signifies poor health and 100 as perfect health. On the first day of simulation, we assume that all people have
an average health of 75 points. On the day of first day of simulation, the first person in the data set is assigned some
health points which will denote whether the person has influenza and is contagious. If the first person is contagious,
the person will spread the virus based on his viral_load i.e. the amount of virus that can be spread to other person
meeting their friends. To decide whether the infected person will meet a particular friend will be decided on the basis
of the meeting_probability that is given. Meeting_Probability is a quantity that defines the level of social distancing
measures that have been imposed. The simulation will be carried out the said number of simulation days.
End the end of the simulation, we will get the count of infected people on each day.
In this task, we will generate a list of all Patient objects from the given file records.
"""


from a2_31223958_task1 import *
import math
import random

class Patient(Person):
    # we create an instances list to store all the instances of Patient class that were created in the current
    # simulation
    instances = []

    #  __init__ method is teh default method that is called when we are creating a new instance of any class or
    #  retrieving an already created instances. Patient instances will have the the following attributes:
    # 1. first_name : First Name of the Patient
    # 2. last_name: Last Name of the Patient
    # 3. health: Health Points of the Patient in the initial simulation
    # 4. friends[]: List of all Patient objects that the inidividual is in contact with.
    # 5. instances[]: All the instances of Patient objects created will be stored in the instances list.
    def __init__(self, first_name, last_name, health):
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
        self.friends = []
        self.__class__.instances.append(self)

    # get_health method is used to retrieve the health points of a Patient.
    def get_health(self):
        return self.health

    # set_health method is called in two cases:
    # 1. when a person meets an infected person and his health points decreased due the viral load passed.
    # 2. when the person sleeps at the end of each day, the health points are increased.
    def set_health(self, new_health):
        self.health = new_health

    # is_contagious method will decide whether the Patient is capable of spread the virus to its friends based on the
    # health points
    # 76-100 health points: perfect health, not contagious
    # 75 health points: average health, not contagious
    # 50-74 health points: fair health, not contagious
    # 30-49 health points: contagious
    # 0-29 health points: poor health, contagious.
    def is_contagious(self):
        hp = round(self.health)
        contagious = False
        if (0 <= hp <= 49):
            contagious = True
        elif (50 <= hp <= 100):
            contagious = False
        return contagious

    # calculate_viral_load method will return the viral_load that the Patient is capable to pass on to its Friends.
    def calculate_viral_load(self):
        hp = self.health
        viral_load = 5 + (math.pow((hp - 25), 2) / 62)
        return viral_load

    # infect method is called when the Patient is capable of passing on the virus to its Friend during a meeting.
    # based on the given conditions, new health points are calculated based on the range of viral_load.
    # hp_a : old health points of the Patient(Friend)
    # hp_b : new health points after getting infected
    def infect(self, viral_load):
        hp_a = self.health
        if (hp_a <= 29):
            hp_b = hp_a - (0.1 * viral_load)
        elif (29 < hp_a < 50):
            hp_b = hp_a - (1.0 * viral_load)
        else:
            hp_b = hp_a - (2.0 * viral_load)
        # The health points of a Patient will lie within the range of 0-100
        if (hp_b < 0):
            hp_b = 0
        if (hp_b > 100):
            hp_b = 100
        self.health = hp_b

    # At the end of each day, every person in the simulation will go to sleep and regain 5 health points.
    def sleep(self):
        hp = self.health
        hp += 5
        # The health points of a Patient will lie within the range of 0-100
        if (hp < 0):
            hp = 0
        if (hp > 100):
            hp = 100
        self.health = hp

    # __new__ method is used to create a new instance of the class Patient cls by invoking the __init__ method to create
    # new object. super method is used to reference to the parent class referenced by cls.
    # @classmethod
    def __new__(cls, first_name, last_name, health):
        instance = super(Person, cls).__new__(cls)
        return instance

    # getPatientInstances method will return the existing Patient objects with first_name and last_name given.
    # This method is invoked when we created Friends objects or when the simulation is executed again.
    # cls.instances[] will have all the Patient objects created during the simulation.
    @classmethod
    def getPatientInstances(cls, first_name, last_name):
        for instance in cls.instances:
            if (instance.first_name == first_name and instance.last_name == last_name):
                return instance

    # printPatientInstances method will return all the instances of the Patient object that have been created and stores in
    # instances list.
    @classmethod
    def printPatientInstances(cls):
        for instance in cls.instances:
            print(instance.__dict__)

# run_simulation function will start the simulation model for spread of infection for said number of days.
# the function is passed three arguments:
# days: the number of days the simulation should be executed,
# meeting_probability: probability that two people will meet,
# patient_zero_health: initial health of the first patient
def run_simulation(days, meeting_probability, patient_zero_health):
    initial_health = 75
    patient_list = load_patients(initial_health)
    patient_zero = patient_list[0]
    patient_zero.set_health(patient_zero_health)
    contagious_count_list_per_day = []
    # Each day in the simulation, a patient will go and meet his friends based on the meeting probability. If any of the
    # two are contagious, the virus would be passed to the other person thus infecting the other person. If both are
    # contagious, both will pass the infection to each other. New health is calculated for every person who is infected.
    # At the end of the day, a count of contagious people would be calculated. Also, at the end of the day, every person
    # will go to sleep and regain health points.
    # contagious_count_list_per_day will store the count of contagious people per day.
    for d in range(days):
        contagious_count_per_day = 0
        for patient in patient_list:
            for friend_name in patient.get_friends():
                friend_obj = Patient.getPatientInstances(friend_name.split(' ')[0], friend_name.split(' ')[1])
                # random.random() will generate a float point integer that lies between 0 and 1. We will use this
                # function to decide whether a meeting will take place or not. If any of the two people in the meeting
                # are contagious, the viral load is calculated for the infected person and passed on to th eother person
                # thus, reducing the other person's health points
                if random.random() < meeting_probability:
                    viral_load_from_patient = 0
                    viral_load_from_friend = 0
                    if patient.is_contagious():
                        viral_load_from_patient = patient.calculate_viral_load()
                    if friend_obj.is_contagious():
                        viral_load_from_friend = friend_obj.calculate_viral_load()
                    patient.infect(viral_load_from_friend)
                    friend_obj.infect(viral_load_from_patient)
        # At the end of day, we will count the number of contagious people and every patient goes to sleep.
        for patient in patient_list:
            if (patient.is_contagious()):
                contagious_count_per_day += 1
            patient.sleep()
        contagious_count_list_per_day.append(contagious_count_per_day)
    return contagious_count_list_per_day

# load_patients function will read the file records for all the patients involved in the simulation. All the patients
# involved the simulation will have their health points set to 75 which signifies average health. From the file records,
# we get information of all the friends that the patient meets. This function is responsible for creating patient
# objects along with linking all the Friends (Patient) objects to the respective Patient objects
def load_patients(initial_health):
    file = open('a2_sample_set.txt', 'r')
    data = file.readlines()
    patient_name_list = []
    patient_list = []
    friend_list = []
    # Create Patient Object
    for lines in data:
        lines = lines.replace('\n', '')
        # Retrieve patient name and its friends from the data records.
        patient_name_list.append(lines.split(":")[0])
        friend_list.append(lines.split(":")[1])
    # While creating Patient objects, we will not create duplicate Patient objects by checking whether instance of that
    # particular object already exists.
    for person_name in patient_name_list:
        first_name, last_name = person_name.split(" ")[0], person_name.split(' ')[1]
        if Patient.getPatientInstances(first_name, last_name):
            patient_list.append(Patient.getPatientInstances(first_name, last_name))
        else:
            patient_list.append(Patient(first_name, last_name, initial_health))

    # Populate Friends of Patients.
    # While creating Friend(patient) objects, we will not create duplicate Patient objects by checking whether instance
    # of that particular object already exists. Instance of Friend object will be searched on the basis of first_name
    # and last_name.
    for rows in range(0, len(patient_name_list)):
        person_name = patient_list[rows]
        friends = [friend_list[rows]]
        for f in friends:
            f_list = f.split(",")
            for names in f_list:
                f_name, l_name = names.split(' ')[1], names.split(' ')[2]
                friend = Patient.getPatientInstances(f_name, l_name)
                person_name.add_friend(friend)
    file.close()
    return patient_list

if __name__ == '__main__':
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)
    # # Sample output for the above test case (15 days of case numbers):
    # # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    # #
    # # Note: since this simulation is based on random probability, the
    # # actual numbers may be different each time you run the simulation.
    #
    # # Another sample test case (high meeting probability means this will
    # # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    # # sample output:
    # # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200,
    # # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]