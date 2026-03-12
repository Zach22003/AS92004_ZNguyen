#This is a trivia quiz about the sport Formula 1 - players will be able to answer questions about this sport
#Multi-choice and short answer questions and true or false questions

#V1 - put in import modules, constants and welcome banner
#V2 - put in some skeleton functions, put in helper functions(clear text and cleaned input), worked on menu

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

banner()
welcome_text()

def show_instructions(): #function to show the user the instructions for the quiz
    pass

def show_information(): #function to show the user the content/information about formula1 for the quiz
    pass

def play_quiz(): #function to start the quiz
    pass