from time import *
import random as ran


def Typing_speed_checker(paragraph, user_input):
    # Errors will be count here
    Errors = 0
    # Loop through the paragraph
    for i in range(len(paragraph)):
        # Check the para, if there is charcter not matching count them as a error
        try:
            if user_input[i] != paragraph[i]:
                Errors = Errors + 1
        except:
            Errors = Errors + 1
    return Errors


def Time(time_s, time_e, user_input):
    time_delay = time_e - time_s
    Time_Round = round(time_delay, 2)
    Speed = len(user_input) / Time_Round
    return round(Speed)


list_paragraph = ["my name is abdullhah",
                  "i am pursuing my computer science deggree", "i love to learn programming"]

choice = ran.choice(list_paragraph)
print("*********************Typing Speed*********************")
print(choice)
Time_1 = time()
input_charcters = input("Enter: ")
Time_2 = time()
print("Speed: ", Time(Time_1, Time_2, input_charcters), "W/S")
print("Errors: ", Typing_speed_checker(choice, input_charcters))
