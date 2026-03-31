#This is a trivia quiz about the sport Formula 1 - players will be able to answer questions about this sport
#Multi-choice and short answer questions and true or false questions

#V1 - put in import modules, constants and welcome banner
#V2 - put in some skeleton functions, put in helper functions(clear text and cleaned input), worked on menu
#V3 - put in a list for the questions
#V4 - started working on main function and some other functions. webbrowser
#V5 - worked on insructions, show information, and changed list to dictionairy and added answers
#V6 - Worked on name and age input
#V7 - Finished age input and asking if user ready
#V8 - The quiz part is now finished all i need to do left is the score, final score at the end and also the end page
#V9 - need to add a system where users can see what they answered for each question at the end.

#Import modules
import os #this module will clear the terminal
import string #This module will allow me to use cleaned to remove punctuation etc
import webbrowser #This module will allow me to import a webbrowser, a link to the f1 wikipedia page

#Constants
MIN_AGE = 11 #Constant sets the minimum age a user can be to do the quiz
MAX_AGE = 18 #Constant sets the maximum age a user can be to do the quiz

#Helper functions

def clear_text(): #function that clears the text from the terminal
    os.system('cls' if os.name == 'nt' else 'clear' )

def cleaned_input(user_input: str) -> str: #function that cleans input
      cleaned = user_input.lower() #lower cases all letters
      cleaned = cleaned.replace(" ", "") #removes the spaces inside the words
      cleaned = cleaned.strip(string.punctuation) # removes special characters and punctuations
      return cleaned


#Functions
def banner():#The banner that will apear at the start and end of my program
    print("""
███████╗░█████╗░██████╗░███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░░░███╗░░  ████████╗██████╗░██╗██╗░░░██╗██╗░█████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║██║░░░██║██║░░░░░██╔══██╗░████║░░  ╚══██╔══╝██╔══██╗██║██║░░░██║██║██╔══██╗
█████╗░░██║░░██║██████╔╝██╔████╔██║██║░░░██║██║░░░░░███████║██╔██║░░  ░░░██║░░░██████╔╝██║╚██╗░██╔╝██║███████║
██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║╚═╝██║░░  ░░░██║░░░██╔══██╗██║░╚████╔╝░██║██╔══██║
██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║███████╗  ░░░██║░░░██║░░██║██║░░╚██╔╝░░██║██║░░██║
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝""")

def welcome_text(): #A welcome text player will see before they do this quiz, also be able to choose from the menu
    print("\n============= Welcome to this Formula1 quiz! =============")
    print("This is a quiz where you will be able to answer questions about Formua 1")
    print("\n=====Menu=====")
    print("1. Play Quiz")
    print("2. Instructions")
    print("3. Information")
    print("4. Exit")

def show_instructions(): #function to show the user the instructions for the quiz
    print("\n =====INSTRUCTIONS=====")
    print("\nAnswer each questiony by typing in your answer or choice")
    print("For mutli choice questions choose and type a number from 1-4")
    print("For True or false questions type in 'true' or 'false'")
    print("For short answer questions type in your answer")
    print("Your score will be shown at the end \n")

def show_information(): #function to show the user the content/information about formula1 for the quiz
    print("\n =====INFORMATION=====")
    print("")
    webbrowser.open('https://en.wikipedia.org/wiki/Formula_One')
    

#dictionairy for the questions
questions = {
    1: "1.How many drivers on an F1 Grid? \n 1.22 \n 2.20 \n 3.18 \n 4.26 \n",
    2: "2.Which f1 driver has won the most races? \n 1.Max Verstappen \n 2.Lewis Hamilton \n 3.Ayrton Senna \n 4.Michael Schumacher \n",
    3: "3.Max Verstappen won the World Drivers Championships in 2025. True or False? \n ",
    4: "4.What country is the Red Bull Ring in? \n",
    5: "5.What year was the first Formula 1 race? \n 1.2000 \n 2.1900 \n 3.1950 \n 4.1980 \n",
    6: "6.How many points does the driver who comes first get? \n ",
    7: "7.Which driver has had the most total starts? \n 1.Max Verstappen \n 2.Lewis Hamilton \n 3.Fernando Alonso \n 4.Michael Schumacher \n",
    8: "8.Who was the youngest driver to start a race? \n 1.Max Verstappen \n 2.Kimi Antonelli \n 3.Oliver Bearman \n 4.Lance stroll \n",
    9: "9.Which team has won the most constructers? \n 1.Ferrari \n 2.Mclaren \n 3.Redbull \n 4.Mercedes \n",
    10: "10.Which of the curcuits are not on the 2026 f1 calendar? \n 1.Circuit De Monaco, Monaco \n 2.Red Bull Ring, Spielberg \n 3.Albert Park Circuit, Melbourne \n 4.Intercity Istanbul Park, Istanbul \n",
    11: "11.What is the least amount of races in a season ever? \n 1.5 races \n 2.8 races \n 3.7 races \n 4.3 races \n",
    12: "12.Which year had the most races in a season? \n 1.2024 \n 2.2018 \n 3.2025 \n 4.2012 \n",
    13: "13.What two Grand Prix's has been held every Formula 1 season? \n 1.Spanish and British Grand prix \n 2.Dutch and British Grand prix \n 3. Monaco and British Grand prix \n 4. Italian and British Grand prix \n",
    14: "14.What Grand Prix is the first to host a night race? \n 1.Abu Dhabi \n 2.Singapore \n 3.Miami \n 4.Las Vegas \n",
    15: "15.F1 is the most dangerous sport. True or False? \n "
}
 
#dictionairy for the answers to the questions
answers = {
    1: "1",
    2: "2",
    3: "false",
    4: "austria",
    5: "3",
    6: "25",
    7: "3",
    8: "1",
    9: "1",
    10: "4",
    11: "3",
    12: "1",
    13: "4",
    14: "2",
    15: "false"
}

question_numbers = 15 #number of questions in the quiz so that the final score can be number/the total number of questions which is 15

#Play quiz function/code - piece of code where the main part of the code is
def play_quiz():
    clear_text()
    banner()

    #asking for name
    name = input("What is your name?: ")

    #asking for age
    clear_text()
    banner()
    while True:
        age = input("Before we start please enter your age in digits: ") #asks the user for input of their age

        if age.isdigit():
            age = int(age)
            break
        else:
            print("Please enter a number in digits") #if they type their age in letters or anything else it will say to type in digits


    if age < MIN_AGE or age > MAX_AGE: #if age is outside of the boundary they will be told they are too old or young and it will return to menu
            print("You are too young or too old to do this quiz!!")
            input("Please press enter to return to return to the menu")
            return
    
    #asking if user ready
    clear_text()
    banner()
    ready = cleaned_input(input("Are you ready to start the quiz? (Yes or No): ")) #asks the user if they are ready or not
    if ready not in ["yes", "y"]: #if they are ready to start the quiz and types in yes or y it starts but if not it returns to menu
        print("Come back when you are ready for the quiz!")
        return
    
    clear_text() 
    print(f"Welcome to this quiz {name}") #welcomes the player to the quiz and tells them to start, takes input(name) and turns it to output
    input("Please press enter to start")

    score = 0 #starting score
    history = [] #this will store the data like the answers user do so at the end they can see what they answered wrong etc

    for key, question in questions.items():
        clear_text()
        print(question)
        user_answer = cleaned_input(input("Answer: "))
        correct_answers = answers[key]

        if user_answer == correct_answers: #player will either be told they got ans right or wrong if wrong they get told correct answer
            print("that is correct!!")
            score += 1 #for every question right they get +1 score
        else:
            print(f"That answer was not incorrect, the correct answer was {correct_answers}")

        history.append({
        "question" : question,
        "your answer" : user_answer,
        "correct answer" : correct_answers
    })

        input("press enter to go to the next question ") #users press enter to go to next question through input

    clear_text() #what the users will see after the quiz is finished
    banner()
    print("==== the quiz is finished!! ====")
    print(f"Name: {name}")
    print(f"score: {score}/{question_numbers}") # scoring system out of 15
    see = cleaned_input(input("would you like to see your answers? (Yes or No): ")) #ask users if they want to see answers

    if see == "yes":
        clear_text
        print("==== your answers ====") #answer history witht the question, what they answer and the correct answer
        for entry in history:
            print(f"Question: {entry['question']}")
            print(f"Your answer: {entry['your answer']}")
            print(f"Correct answer: {entry['correct answer']}\n")

    input("Please press enter to return to menu") #takes user back to menu

#Main code
def main(): #function calls to the banner and welcome text function
    clear_text
    while True:
        banner()
        welcome_text()
        choice=input("Choose one of the options (1/2/3/4):") #tells user to either choose play quiz, info instruction or quit
        choice=cleaned_input(choice)

        if choice == "1": #choice 1 will take players to the quiz
            play_quiz()

        elif choice == "2": #choice 2 will take players to the instructions
            clear_text()
            show_instructions()
            next = input("Type 'play' to start game or 'menu' to return to the menu: ")
            next = cleaned_input(next)

            if next == "play":
                clear_text()
                play_quiz()
            else:
                clear_text()
                continue
    
        elif choice == "3": #choice 3 will take players to the info page
            clear_text()
            show_information()
            next = input("Type 'play' to start game or 'menu' to return to the menu: ")
            next = cleaned_input(next)

            if next == "play":
                clear_text()
                play_quiz()
            else:
                clear_text()
                continue

        elif choice == "4": #choice 4 will make the code stop because players dont want to do it
            clear_text()
            print("Goodbye!")
            break

        else:
            print("Invalid menu option.\n")
            clear_text()

main()