#!/usr/bin/python

from round import *

def average_round(num_of_rounds, num_questions, odds_of_answering):
    scores = np.array([0.0, 0.0])

    for i in range(0, num_of_rounds):
        scores += np.array(list(round(num_questions, odds_of_answering)))

    scores /= num_of_rounds

    return scores
