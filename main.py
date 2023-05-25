# Quiz game

# Define the Question class
class Question:
    def __init__(self, question_text, possible_answers, correct_answer):
        self.question_text = question_text
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer

# Set up the quiz

questions = [
    Question("What is the capital of Australia?", ["Sydney", "Canberra", "Melbourne", "Perth"], "Canberra"),
Question("Which country is known as the \"Land of the Rising Sun\"?", ["China", "Japan",
         "South Korea", "Thailand"], "Japan"),
Question("Which country is famous for its tulips and windmills?", ["Belgium", "Netherlands", "Denmark", "Switzerland"],
         "Netherlands"),
Question("Which African country is home to the Great Sphinx and the Pyramids of Giza?", ["Egypt", "Morocco",
         "South Africa", "Kenya"], "Egypt"),
Question(" Which country is the largest producer of coffee in the world?", ["Brazil", "Colombia", "Ethiopia",
         "Vietnam"], "Brazil"),
Question("Which country is the birthplace of pizza?", ["Italy", "Greece", "Spain", "France"], "Italy"),
Question("Which country is famous for its fjords, trolls, and Viking history?", ["Norway", "Sweden",
         "Finland", "Iceland"], "Norway"),
Question(" Which country is the smallest in terms of land area?", ["Monaco", "Vatican City", "Nauru",
         "San Marino"], "Vatican City"),
Question("Which country is home to the famous Angkor Wat temple complex?", ["Thailand", "Cambodia",
         "Indonesia", "Malaysia"], "Cambodia"),
Question("Which country is known for its Maasai tribespeople and wildlife safaris?", ["Kenya", "Tanzania",
         "Namibia", "Botswana"], "Kenya")
]

score = 0

# Start the quiz

for question in questions:
    # ask the questions
    print(question.question_text)
    for index, answer in enumerate(question.possible_answers):
        print(index+1, answer)
    user_answer = input("Your answer (enter the number): ")

    # Check the answer
    if question.possible_answers[int(user_answer)-1] == question.correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is", question.correct_answer)

# End the quiz
print("Quiz complete! Your final score is", score)

