# Programmers: Cooper Nazar, Cameron Combariza
# Course:  CS151*06
# Due Date: 11/28/2024
# Lab Assignment: Lab 11
# Problem Statement:
# Data In:
# Data Out:

import os

# Purpose: Check the file input name for error
# Parameters: None
# Return: None
def verify_file():
    # Prompt user for the filename to read
    name = input("What file do you want to read? ")
    # Check if the file exists, and if not, loop until a valid file is entered
    while not os.path.isfile(name):
        print("That file does not exist. Please try again.")
        name = input("What file do you want to read? ")

# Purpose: Read the morse code file into a dictionary
# Parameters: filename
# Return: morse_dict
def read_file_to_dict(filename):
    morse_dict = {}
    morse_data = open(filename, 'r')
    for line in morse_data:
        items = line.strip().split()
        key = items[1]
        value = items[0]
        morse_dict[key] = value
    morse_data.close()
    return morse_dict

# Purpose: Read morse code data from a file
# Parameters:
# Return:
def