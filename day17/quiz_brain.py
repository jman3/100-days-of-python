class QuizBrain:
    def __init__(self, list_of_question):
        self.question_number = 0
        self.question_list = list_of_question
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score: {self.score} / {self.question_number}")
        print("\n")

    def show_final_score(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score} / {self.question_number}")