from question_class import Question
from data import questions_data
from brain_class import Brain
import random

Questions = []
for question in questions_data:
    q_text = question["q_text"]
    q_answers = question["q_answers"]
    new_question = Question(q_text,q_answers)
    Questions.append(new_question)

Quiz = Brain(Questions)
i = 0
while Quiz.game_is_on:
    Quiz.next_question(i)
    i+=1