from kvizquestionmodel import Question
from kvízdata import question_data
from kvizbrain import QuizBrain

question_list = []

for one_question in question_data:
    question_t = (one_question["text"])
    question_a = (one_question["answer"])
    new_question = Question(question_t, question_a)
    question_list.append(new_question)


#print(question_list)

quiz = QuizBrain (question_list)
while quiz.has_question () == True:
    quiz.next_question()
print("Dokončili jste kvíz")
print(f"Vaše skóre je {quiz.score} / {quiz.question_number}")