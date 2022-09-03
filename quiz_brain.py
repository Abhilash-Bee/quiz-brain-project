import html


class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_no = 0
        self.question_list = question_list

    def still_has_question(self):
        return len(self.question_list) > self.question_no

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        return f"Q.{self.question_no}: {html.unescape(current_question.question)}"
        # self.check_answer(user_answer, current_question.answer, self.question_no)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
