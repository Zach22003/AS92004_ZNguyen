#This is a trivia quiz about the sport Formula 1 - players will be able to answer questions about this sport
#Multi-choice and short answer questions and true or false questions

#V1 - put in import modules, constants and welcome banner

#Import modules
import os #this module will clear the terminal
import string #This module will allow me to use cleaned to remove punctuation etc
import random #This module will allow me to make the computer choose a random question
import webbrowser

#Constants
MIN_AGE = 11 #Constant sets the minimum age a user can be to do the quiz
MAX_AGE = 18 #Constant sets the maximum age a user can be to do the quiz


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
