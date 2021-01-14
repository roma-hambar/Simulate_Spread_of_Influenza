"""
Assignment 2 task 3
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
End of the simulation, we will get the count of infected people on each day.
In this task, we will plot the graph of count of contagious people along the number of days.
Comments for output of Test scenarios:
Test Scenario A :
    1. Number of days: 30
    2. Meeting probability: 0.6
    3. Patient zero health: 25 health points
    From scenario_A.png, we can observe that since the social distancing is not very strictly followed by all Patients,
    the infection spreads amongst all 200 people by the end of 30 days due to patient zero's poor health.
Test Scenario B:
    1. Number of days: 60
    2. Meeting probability: 0.25
    3. Patient zero health: 49 health points
    From scenario_B.png, we can conclude that the patient zero's health points play a crucial role in determining how
    quickly the virus spread inspite of strictening social distancing. ALthough the disease spreads slowly amongst
    considerable number of Patients due to lesser meeting probability.
Test Scenario C:
    1. Number of days: 90
    2. Meeting probability: 0.18
    3. Patient zero health: 40 health points
    From scenario_C.png, we can conclude that if strict social distancing rules are implied, the spread of virus can be
    contained drastically, thus flattening the curve instantly within the first few days.
"""

from task2 import *
import matplotlib.pyplot as plt

# visual_curve function is used to generate a plot of contagious people count vs number of days by calling the
# run_simulation method defined in task2 for Patient class. The arguments required for run_simulation are passed in the
# visual_curve function to get a list of count of contagious people during the period of simulation
# This function will print the count of contagious people at the end of simulation for asked number of days.
def visual_curve(days, meeting_probability, patient_zero_health):
    contagious_count_list = run_simulation(days, meeting_probability, patient_zero_health)
    print(contagious_count_list)
    # Using matplotlib plot method, we will plot the graph of number of days on X-axis and count of contagious people
    # on Y-axis
    plt.plot(contagious_count_list)
    plt.ylabel("Count of Contagious People")
    plt.xlabel("No of Days")
    # plt.savefig("scenario_C.png")
    plt.show()

if __name__ == '__main__':
    # Read input from user
    days = int(input("Enter number of days:"))
    meeting_probability = float(input("Meeting Probability:"))
    patient_zero_health = float(input("Health of Patient Zero:"))
    visual_curve(days,meeting_probability,patient_zero_health)
