#!/usr/bin/python

import numpy as np

def round(num_questions, odds_of_answering):
    #How many points each question gets you.
    question_value = 100 / num_questions
    num_strikes = 0
    #Family A will be the one that answers first.
    A_score = 0
    B_score = 0
    #Since we're acting under the assumption that A already answered
    #a question in the stand-off, we start A off with some points.
    A_score += question_value
    num_questions -= 1
    while (num_strikes < 3) and (num_questions > 0):
        #More questions on the board means better chances.
        if np.random.random() < odds_of_answering:
            A_score += question_value
            num_questions -= 1

        else:
            num_strikes += 1

    #Family B goes in for the steal.
    if num_questions > 0:
        if np.random.random() < odds_of_answering:
            B_score += (question_value + A_score)
            A_score = 0

    return A_score, B_score
