from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    dictionary_text = dictionary["text"]
    dictionary_answer = dictionary["answer"]
    new_question = Question(dictionary_text, dictionary_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz :)")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")