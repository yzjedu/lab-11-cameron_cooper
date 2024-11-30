# Programmers: Cooper Nazar, Cameron Combariza
# Course:  CS151*06
# Due Date: 11/28/2024
# Lab Assignment: Lab 11
# Problem Statement: Create a program to convert encrypted text into plain English
# Data In: Dictionary file, file to translate, translated file name
# Data Out: Translated file

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
    return name

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
# Parameters: filename
# Return: values
def read_file_to_list(filename):
    # Open the file for reading
    file_data = open(filename, 'r')
    # Read all lines from the file and store them as a list of strings
    values = file_data.readlines()
    # Close the file
    file_data.close()
    # Return the list of lines from the file
    return values

# Purpose: Translate the morse code data and write it into a new file
# Parameters: list, dictionary
# Return: translation
def translate_list_with_dictionary(lines, dictionary):
    translation = []
    for line in lines:
        words = line.split(' / ')
        # Split into words (using '/')
        decoded_words = []
        for word in words:
            letters = word.split()
            # Split into individual Morse code letters
            decoded_letters = [dictionary.get(letter, '?') for letter in letters]
            decoded_words.append(''.join(decoded_letters))
            # Join letters into a word
        translation.append(' '.join(decoded_words))
        # Join words into a line
    return translation

# Purpose: Write a list to a file
# Parameters: list, filename
# Return: None
def write_list_to_file(my_list, filename):
    # Open the file for writing
    fd = open(filename, "w")
    # Write each item in the list to the file
    for item in my_list:
        fd.write(str(item))
    # Close the file
    fd.close()

def main():
    continue_choice = 'yes'
    while continue_choice != 'no':
        print("This program's purpose is to translate a file with a given dictionary.")
        print("Please enter which file you want to use as a dictionary.\n")
        dict_file = verify_file()
        dictionary = read_file_to_dict(dict_file)
        print("Now, please enter which file you would like to translate.\n")
        translate_file = verify_file()
        translate_list = read_file_to_list(translate_file)
        translated_list = translate_list_with_dictionary(translate_list, dictionary)
        outfile = input("Please enter which file you would like to write the translation to. ")
        write_list_to_file(translated_list, outfile)
        print("Thank you for using the program.\n")
        continue_choice = input("Would you like to translate another file? Please enter yes or no. ")
        continue_choice = continue_choice.lower().strip()

main()