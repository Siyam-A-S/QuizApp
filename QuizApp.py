# Import necessary modules
import random

# Define classes for User, Instructor, Student, QuestionGenerator, and Test
class User:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

class Instructor(User):
    def __init__(self, userName, password):
        super().__init__(userName, password)
        self.tests = []

    def create_test(self, testName, questions, timeLimit):
        test = Test(testName, questions, timeLimit)
        self.tests.append(test)
        return test

    def assign_test(self, test, studentIDs):
        for studentID in studentIDs:
            student = find_student_by_id(studentID)
            if student:
                student.tests.append(test)

class Student(User):
    def __init__(self, userName, password, studentID):
        super().__init__(userName, password)
        self.studentID = studentID
        self.tests = []


#Generates question from text file
class QuestionGenerator:
    def __init__(self, questionFile):
        self.questions = []
        with open(questionFile, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('Q-'):
                    question = {'question': line[3:], 'options': [], 'answer': ''}
                elif line.startswith('A-'):
                    question['answer'] = line[3:]
                    self.questions.append(question)
                elif line.startswith('Options:'):
                    options = line[9:].split(',')
                    for option in options:
                        question['options'].append(option.strip())

    def scramble(self):
        for question in self.questions:
            random.shuffle(question['options'])

class Test:
    def __init__(self, testName, questions, timeLimit=None):
        self.testName = testName
        self.questions = questions
        self.timeLimit = timeLimit
        self.answers = {}

    def get_question(self, questionNumber):
        if questionNumber in self.answers:
            return None
        else:
            return self.questions[questionNumber]

    def correct_answer(self, questionNumber, answer):
        self.answers[questionNumber] = answer

    def score(self):
        correct = 0
        for questionNumber, answer in self.answers.items():
            if answer == self.questions[questionNumber]['answer']:
                correct += 1
        return correct / len(self.questions)

# Define functions for finding a student by ID and displaying a score report
def find_student_by_id(studentID):
    for student in students:
        if student.studentID == studentID:
            return student
    return None

def display_score_report(test, student):
    print('Test:', test.testName)
    print('Student:', student.userName)
    print('Score:', test.score())

# Main program
students = [
    Student('John Doe', 'password', '03047777'),
    Student('Jane Doe', 'password', '03047778')]


student1 = Student("Siyam","123", "03043178")
instructor = Instructor('Professor X', 'password')
questionGenerator = QuestionGenerator('question_bank.txt')
questionGenerator.scramble()
test = instructor.create_test('Quiz 1', questionGenerator.questions, 1)
instructor.assign_test(test, ['@03047777', '@03047778'])


if __name__ == "__main__":

    print("Welcome to QuizApp!")
    while True:
        user_input = input("Enter 'i' for instructor, 's' for student, or 'q' to quit:")
        if user_input == "i":

            name = input("enter username: ")
            password = input("enter password: ")
            if name == instructor.userName and password == instructor.password:
                test_name = input("Type the name of the test: ")
                action = input("Enter 'c' to create test: ")
                if action == "c":
                    test1 = instructor.create_test(test_name, questionGenerator.questions, 30)
                    type = input("Enter 'a' to assign test: ")
                    if type == "a":

                        instructor.assign_test(test1, ['@03047777', '@03047778'])
                        print("Test has been assigned")
                    else:
                        print("Wrong Command! ")

            else:
                print("Incorrect username or password")





        elif user_input == 's':
            id_input = input("Enter student ID to start test: ")
            if id_input == student1.studentID:
                print("Give answer to each question to finish the test")
                score = 0
                for i in range(len(test.questions)):
                    question = test.get_question(i)
                    if question:
                        print('Question', i + 1, ':', question['question'])

                        # generate_options
                        x = ['a', 'b', 'c', 'd']
                        opt = {}
                        for i in range(4):
                            print(x[i] + '.' + question['options'][i])
                            opt[x[i]] = question['options'][i]

                        key = [k for k, v in opt.items() if v == question['answer']]


                        # Check if the answer is correct
                        answer = input("Type the correct option: ")
                        if answer == key[0]:
                            print("That's right! ")
                            score += 1

                        else:
                            print("Wrong! Correct answer is: ", question['answer'])

                    else:
                        print("No questions found!")

                print("Score: ", score)




        elif user_input == 'q':
            break




