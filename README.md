# QuizApp
Overview

Narrative: 
St. Joseph High School has a vast student body. The online quiz system for grade 5-8 is depended on a third-party application that take the quiz online. The school authority is planning on installing their own server with a built-in quiz application. that will solve the problems regarding lagging, resource allocation, internet instability and cheating. The authority is hoping that this will enable more functionality and originality of questions to the testing process based on multiple choice questions. The authority is hoping to add more features such as visual representation of physical laws to enhance the understanding of a concept and to test it.
Purpose:
This Quiz Application System intend to solve the problems regarding lagging, resource allocation, internet instability and cheating. This system will facilitate more functionality and originality of questions to the testing process based on multiple choice questions. Extra features include visual representation of physical laws to enhance the understanding of a concept and to test it. Each student will have to login with their unique IDs to take part in the quiz. The instructor will assign and edit tests.

Project Scope:
There are two types of users for this application – teachers and students. Each has their own kind of access to the app. 
•	In-Scope:
o	Students can login with their unique ID
o	Teachers or instructors have the permission to edit and assign questions after login
o	Timed or untimed quiz
o	Score report
o	Maximum 1000 students can take quiz simultaneously
•	Out-of-Scope (what will it not do)
o	It won’t facilitate proctored camera based test.
o	It won’t allow two users with unique IDs to take part in a test from the same device
Project Useability: 
This application is built for a school quiz system, but it can be used to take trivia quiz for club events. The API can be used for websites specializing in taking quizzes online. 

User Requirements

Narrative: The user will be able to open the application on their device. The app will prompt for the user’s identification whether the user’s a student or a teacher. The app will proceed to the account dashboard that will display information for quiz assigned. If a student user clicks on a running quiz he’ll get in the test with a disclaimer of code of conduct. When the user is finished using the app, they can Logout or close the app manually from their device. 

1.	User type 1(Instructors): The instructors will require their username and password to login to the application. The first page displayed will be the dashboard where he can create a new test, edit previously created tests, delete tests and assign a test to a student body. The questions can be loaded from a text file with the layout as follows:

//opens question_bank.txt
Q-1: What is the name of the US capital city? 
A-1: Washington D.C.
Options: Detroit, Michigan, New York, San Diego.
Q-2: What is python?
A-2: Scripting language
Options: Machine language, Instruction, Animal.

The instructor can also choose time limit for the quiz or no time limit at all. Then he can assign the test to a student body with all the IDs as input. This can be parsed from a text file or input manually. There is a symbol “@” before each ID to identify it as an ID such as: @03047777 is a valid ID representation. 

2.	User type 2(Students): The students can open the application and login with their unique school ID of 8 digits. As long as there is any test assigned by the instructor to this ID, the quiz name will appear before him and he will be able to take part in it by clicking on the quiz name. As soon as he starts it, he must finish it. The quiz is finished once he’s done with the test and press submit or the time runs out. Then comes the score report where the score is shown.
Software Requirements
Software Narrative: The application will represent two types of user as two subclasses (Instructor and Student) of parent class User. Each will have their own sets of method. Goals are to make the app more user-friendly by improving how it looks and how it handles user errors, refactor the code to use functions, separate question data from source code by storing questions in a dedicated data file.


•	Software Class APIs 

User: The purpose of this class is to define the data for specific objects that represent a user. Two subclasses – Instructors and Students. Attributes such as userName and password will be tracked for Instructor user and 8 digit ID with @ at the start will be tracked for Student user. 

Variables: userName, password, ID : String 
Data type: Linked list for question bank.
Question Generator: The purpose of this class is to use the data for specific objects that represent a question. The data being text files, cvs. This is an abstract superclass, so each question that is created must contain answer, options, scramble() in it.
Scramble: Method in Question Generator randomizing the options for unique sequences experienced by each test taker
Test: This class creates a test session. Timer, score, get_question, correct_answers methods are in it.
