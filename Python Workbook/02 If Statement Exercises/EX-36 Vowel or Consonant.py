"""
In this exercise, you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u, then your program should display a message
indicating that the entered letter is a vowel. If the user enters y, then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise, your program should display a message indicating that the
letter is a consonant.
"""

user_input = input("Enter  a letter of the alphabet: ")

if user_input in ('a', 'e', 'i', 'o', 'u'):
    print("The letter is a Vowel.")
else:
    print("The letter is a consonant.")
