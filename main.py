from genericpath import exists
import sys
import msvcrt
import time

p_num = 1

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
        passwor += x
    return passwor

def user_selection():
    global t_password
    global user
    t_password = "T_auth"
    user = "p"
    remaining_attempts = 5

    while True:
        clear()
        u_input = input("Are you a parent?\n")
        if u_input == "No" or u_input == "no" or u_input == "n" or u_input == "N":
            clear()
            print("Teacher Login")
            while True:
                print("Password:")
                hidden_input()
                if passwor == t_password:
                    user = "t"
                    print("\nAccess Granted")
                    break
                else:
                    remaining_attempts -=1
                    clear()
                    print("Incorrect Password\nYou have", remaining_attempts ,"attempts remaining.")

                if remaining_attempts == 0:
                    print("Password Attempt Limit Exceeded")
                    exit()
            break
        elif u_input == "Yes" or u_input == "yes" or u_input == "y" or u_input == "Y":
            user = "p"
            break
        else:
            print("Please enter Yes or No.")
            time.sleep(0.7)

def p_input():

    global p_num
    global preferences
    global preferenced
    global preferencet

    preferences = 0

    preferenced = ["1", "2"]
    preferencet = ["1", "2"]

    
    if p_num < 24:
        clear()
        print("Crawdale Parents Eveining Booking Portal\n")
        print("Hello! You are Parent " + str(p_num) +  ".\n")
        
        for preferences in range(2):

            if preferences == 0:
                print("Please enter your first booking choice.\n")
            else:
                print("Please enter your second booking choice.\n")


            while True:
                day = str(input("What day would you like your appointment on? Please enter a number from 1-3.\n"))

                if day == "1":
                    break
                elif day == "2":
                    break
                elif day == "3":
                    break
                else:
                    clear()
                    print("Please enter 1, 2 or 3 only.\n")
                
            day = int(day)
            while True:
                print("\nPlease select a time from the following list:")
                print("1 = 17:00\n2 = 17:20\n3 = 17:40\n4 = 18:00\n5 = 18:20\n6 = 18:40\n7 = 19:00\n8 = 19:20\n9 = 19:40")
                time = str(input())
                if time == "1":
                    break
                elif time == "2":
                    break
                elif time == "3":
                    break
                elif time == "4":
                    break
                elif time == "5":
                    break
                elif time == "6":
                    break
                elif time == "7":
                    break
                elif time == "8":
                    break
                elif time == "9":
                    break
                else:
                    clear()
                    print("\nPlease enter a number from 1-9.")
                preferenced[preferences] = day
                preferencet[preferences] = time
                
                preferences += 1
            

        p_num += 1

        p_num_print = (str(p_num)+ "\n")
 
        f = open("bookings.txt", "r")
        p_lines = f.readlines()
        p_lines[0] = p_num_print

        f = open("bookings.txt", "w")
        f.writelines(p_lines)
        f.close()

def booking_verify():
    global p1_line
    global p2_line
    
    b_time = "17:00"
    p1_line = ((int(preferenced[0]) * 10) + int(preferencet[0]))-7
    p2_line = ((int(preferenced[1]) * 10) + int(preferencet[1]))-7

    f = open("bookings.txt", "r")
    
    if f.readline(p1_line)[0] != "P":
        lines = f.readlines()
        lines[(p1_line - 1)] = "P"+p_num+"\n"
        
        f = open("bookings.txt", "w")
        f.writelines(lines)
        f.close()
        if preferencet[0] == 1:
            b_time = "17:00"
        
        print("Preference 1 Booked\nYour booking is on Day", preferenced[0], "at", b_time + ".")




if exists("bookings.txt") == True:
    f = open("bookings.txt", "rt")
    p_num = int(f.readline(1))
    f.close()
else:
    f = open("bookings.txt", "x")
    f = open("bookings.txt", "wt")
    f.write(str(p_num))
    f.write("\n\nDay 1 Bookings\n1\n2\n3\n4\n5\n6\n7\n8\n9\nDay 2 Bookings\n1\n2\n3\n4\n5\n6\n7\n8\n9\nDay 3 Bookings\n1\n2\n3\n4\n5\n6\n7\n8\n9")
    f.close()


clear()
print("Welcome to Crawdale Parents Evening System\n")
time.sleep(1.5)

user_selection()

if user == "p":
    p_input()
    booking_verify()
