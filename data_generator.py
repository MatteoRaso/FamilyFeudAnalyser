#!/usr/bin/python

#This is where we actually get the data and plot it.

import matplotlib.pyplot as plt
from average_round import *

#If you check commit abee0a, you'd see that 5000 rounds is a reasonable
#number if you want to get an accurate representation. Just to be safe,
#I'm upping this to 20000, since I imagine the results will be more prone
#to bias at certain odds.
num_rounds = 20000

for i in range(2, 9):
    A_score = []
    B_score = []

    for j in range(0, 10000):
        scores = average_round(num_rounds, i, j / 10000)
        A_score.append(scores[0])
        B_score.append(scores[1])

    x_axis = np.linspace(0, 0.9999, 10000)

    plt.plot(x_axis, A_score, x_axis, B_score)
    plt.title("Odds of Each Family Winning With " + str(i) + " Questions")
    ax = plt.subplot(111)
    ax.plot(x_axis, A_score, label = "Family A Average Score")
    ax.plot(x_axis, B_score, label = "Family B Average Score")
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
    plt.savefig("Number of Questions = " + str(i) + ".png")
    plt.clf()
