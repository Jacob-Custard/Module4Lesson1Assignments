# Objective: The aim of this assignment is to assess your understanding and ability to
#implement Python modules, both built-in and custom, and to apply data handling techniques
#using Python's data structures and error handling.

# Task 1: Your Mood Today - Problem Statement: Create a Python program using a custom module 
#that asks the user how they are feeling today and responds with a custom message based on the
#mood entered. 

import mood_response                                                                                                              #importing the custom module

mood = input("What mood are you in right now? ")                                                                                  #input getting the user's mood to be used in a function
print(mood_response.reply(mood))                                                                                                  #print statement providing the user with a reply
