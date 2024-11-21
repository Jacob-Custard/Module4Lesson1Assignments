# Objective: The aim of this assignment is to enhance your proficiency in using Python
#modules, both standard and custom, with a specific focus on importing with aliases.

# Task 1 Custom Module with Aliases: Create a custom module named `text_utils.py` with
#functions for string manipulation (e.g., reversing a string, capitalizing). In your main
#script, import this module using an alias and utilize its functions.

import text_utils as textils                                                                                                         #importing the module text_utils with an alias

from text_utils import capitalize_all_words as capsall, capitalize_first_word as capsfirst, uppercase as yell                        #importing specific functions from text_utils with their own alias


user_input = input("Enter a sentence and see what happens: ")                                                                        #user input to get a string to be used in the functions

print(f"\n{textils.reverse_string(user_input)}\n")                                                                                   #print statements calling all the functions in the text_utils module
print(f"{textils.lowercase(user_input)}\n")

print(f"{capsall(user_input)}\n")
print(f"{capsfirst(user_input)}\n")
print(f"{yell(user_input)}\n")



