class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        inp = input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (Trues/False): ")
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        self.check_answer(inp, correct_answer)

    def check_answer(self, inp, answer):
        if inp.lower() == answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("That is wrong!!")
        print(f"Correct answer is {answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
