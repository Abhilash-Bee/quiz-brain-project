from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []


for question_answer in question_data:
    question = question_answer["text"]
    answer = question_answer["answer"]
    question_bank.append(Question(question, answer))

quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)

# while quiz.still_has_question():
#     data = quiz.next_question()


print("You have completed your quiz")
print(f"Your final score is {quiz.score} of {quiz.question_no}")