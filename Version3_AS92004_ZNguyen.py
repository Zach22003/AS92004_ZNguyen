#This is a trivia quiz about the sport Formula 1 - players will be able to answer questions about this sport
#Multi-choice and short answer questions and true or false questions

#V1 - put in import modules, constants and welcome banner
#V2 - put in some skeleton functions, put in helper functions(clear text and cleaned input), worked on menu
#V3 - put in a list for the questions
#V4 - started working on main function and some other functions. webbrowser

#Import modules
import os #this module will clear the terminal
import string #This module will allow me to use cleaned to remove punctuation etc
import random #This module will allow me to make the computer choose a random question
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
    print("")

def show_information(): #function to show the user the content/information about formula1 for the quiz
    print("info")
    print("")
    webbrowser.open('https://en.wikipedia.org/wiki/Formula_One#Grands_Prix')

def play_quiz(): #function to start the quiz
    pass

#list for the questions
questions = [
    "How many drivers on an F1 Grid? \n 1.22 \n 2.20 \n 3.18 \n 4.26 \nAnswer:"
    "Which f1 driver has won the most championships?"
    "Who won f1 in 2025? \nAnswer:"
    "What team has won the most constructors? \n \nAnswer:"
    "What year was the first Formula 1 race? \n 1.2000 \n 2.1900 \n 3.1950 \n 4.1980 \nAnswer:"
    "How many points does the driver who comes first get? \n ANSWER:"
    "Which driver has had the most total starts? \n 1.Max Verstappen \n 2.Lewis Hamilton \n 3.Fernando Alonso \n 4.Michael Schumacher \nAnswer:"
    "Who was the youngest driver to start a race? \n 1.Max Verstappen \n 2.Kimi Antonelli \n 3.Oliver Bearman \n 4.Lance stroll \nAnswer:"
    "Which team has won the most constructers? \n. 1.Ferrari \n 2.Mclaren \n 3.Redbull \n 4.Mercedes \nAnswer:"
    "Which of the curcuits are not on the 2026 f1 calendar? \n 1.Circuit De Monaco, Monaco \n 2.Red Bull Ring, Spielberg \n 3.Albert Park Circuit, Melbourne \n 4.Intercity Istanbul Park, Istanbul \nAnswer:"
    "What is the least amount of races in a season ever? \n 1.5 races \n 2.8 races \n 3.7 races \n 4.3 races \nAnswer:"
    "Which year had the most races in a season? \n 1.2024 \n 2.2018 \n 3.2025 \n 4.2012 \nAnswer:"
    "What two Grand Prix's has been held every Formula 1 season? \n 1.Spanish and British Grand prix \n 2.Dutch and British Grand prix \n 3. Monaco and British Grand prix \n 4. Italian and British Grand prix \nAnswer:"
    "What Grand Prix is the first to host a night race? \n 1.Abu Dhabi \n 2.Singapore \n 3.Miami \n 4.Las Vegas \nAnswer:"
    "F1 is the most dangerous sport. True or False? \n ANSWER:"
]


#Main code

def main(): #function calls to the banner and welcome text function
    clear_text
    while True:
        banner()
        welcome_text()
        choice=input("Choose one of the options (1/2/3/4):") #tells user to either choose play quiz, info instruction or quit
        choice=cleaned_input(choice)

        if choice == "1":
            clear_text()

        elif choice == "2":
            clear_text()
            show_instructions()
            next = input("Type 'play' to start game or 'menu' to return to the menu: ")
            next = cleaned_input(next)

            if next == "play":
                clear_text()
                show_information()
            else:
                clear_text()
                continue
    

        elif choice == "3":
            clear_text()
            show_information()
            next = input("Type 'play' to start game or 'menu' to return to the menu: ")
            next = cleaned_input(next)

            if next == "play":
                clear_text()
                show_information()
            else:
                clear_text()
                continue

        elif choice == "4":
            clear_text()
            print("Goodbye!")
            break

        else:
            print("Invalid menu option.\n")
            clear_text()


main()

