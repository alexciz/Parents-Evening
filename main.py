from genericpath import exists
import sys
import msvcrt
import time

slots = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]


def clear():
    # \033[H homes the cursor
    # \033[2J Clears the screen and sets the cursor back to top left
    sys.stdout.write("\033[H\033[2J\033[H")

def hidden_input():
    global passwor
    passwor = ''
    while True:
        x = msvcrt.getch().decode("utf-8")
        if x == '\r' or x == '\n':
            break
        print('*', end='', flush=True)
        passwor +=x
    return passwor

def user_selection():
    global t_password
    global user
    t_password = "T_auth"
    user = "p"
    us_loop = 1
    p_attempts = 0
    
    while us_loop == 1:
        clear()
        u_input = input("Are you a parent?\n")
        if u_input == "No" or u_input == "no" or u_input == "n" or u_input == "N":
            us_loop = 0
            clear()
            print("Teacher Login")
            while True:
                print("Password:")
                hidden_input()
                if passwor == str(t_password):
                    user = "t"
                    print("\nCorrect")
                    break
                else:
                    p_attempts += 1
                    remaining_attempts = 5-int(p_attempts)
                    clear()
                    print("Incorrect Password\nYou have", remaining_attempts ,"attempts remaining.")

                if remaining_attempts == 0:
                    print("Password Attempt Limit Exceeded")
                    exit()
        
        elif u_input == "Yes" or u_input == "yes" or u_input == "y" or u_input == "Y":
            user = "p"
            us_loop = 0
        else:
            print("Please enter Yes or No.")
            time.sleep(0.7)

def p_input():

    global x
    global y
    global d
    global preferences
    global preferenced
    global preferencet
    #global slots

    x = 1
    y = 1
    d = 1
    preferences = 0

    #slots = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]
    preferenced = ["1", "2"]
    preferencet = ["1", "2"]

    
    if x < 24:
        clear()
        print("Crawdale Parents Eveining Booking Portal\n")
        print("Hello! You are Parent " + str(x) +  ".\n")
        
        for preferences in range(2):

            if preferences == 0:
                print("Please enter your first booking choice.\n")
            else:
                print("Please enter your second booking choice.\n")


            while d == 1:
                day = str(input("What day would you like your appointment on? Please enter a number from 1-3.\n"))

                if day == "1":
                    d = 0
                elif day == "2":
                    d = 0
                elif day == "3":
                    d = 0
                else:
                    clear()
                    print("Please enter 1, 2 or 3 only.\n")
                
            d = 1
            day = int(day)
            day -= 1
            while y == 1:
                print("\nPlease select a time from the following list:")
                print("1 = 17:00\n2 = 17:20\n3 = 17:40\n4 = 18:00\n5 = 18:20\n6 = 18:40\n7 = 19:00\n8 = 19:20\n9 = 19:40")
                time = str(input())
                y = 0
                if time == "1":
                    time = 0
                elif time == "2":
                    time = 1
                elif time == "3":
                    time = 2
                elif time == "4":
                    time = 3
                elif time == "5":
                    time = 4
                elif time == "6":
                    time = 5
                elif time == "7":
                    time = 6
                elif time == "8":
                    time = 7
                elif time == "9":
                    time = 8
                else:
                    print("Please enter a valid time.")
                    y = 1
                preferenced[preferences] = day
                preferencet[preferences] = time
                print("\n")
                #print(preferenced[0])
                #print(preferenced[1])
                #print(preferencet[0])
                #print(preferencet[1])
                
                preferences += 1
            

            y = 1

        #y = 1
        x += 1

        f = open("bookings.txt", "wt")
        f.write(str(x))
        f.close()



if exists("bookings.txt") == True:
    f = open("bookings.txt", "rt")
    x = int(f.read())
    f.close()

else:
    f = open("bookings.txt", "x")
    f = open("bookings.txt", "wt")
    f.write(str(x))
    f.close()

user_selection()
if user == "p":
    p_input()
