# Simulate_Spread_of_Influenza
Python simulate the spread of Influenza virus among a set of 200 people. A dummy dataset was used to show social connections among Friends.

In this simulation, we denote the health of patient in terms of health points ranging from 0-100
where 0 signifies poor health and 100 as perfect health. On the first day of simulation, we assume that all people have
an average health of 75 points. On the day of first day of simulation, the first person in the data set is assigned some
health points which will denote whether the person has influenza and is contagious. If the first person is contagious,
the person will spread the virus based on his viral_load i.e. the amount of virus that can be spread to other person
meeting their friends. To decide whether the infected person will meet a particular friend will be decided on the basis
of the meeting_probability that is given. Meeting_Probability is a quantity that defines the level of social distancing
measures that have been imposed. The simulation will be carried out the said number of simulation days.
End of the simulation, we will get the count of infected people on each day.
