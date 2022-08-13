from genericpath import exists
import msvcrt
import time
import linecache
import os
from tracemalloc import start


p_num = 1

def clear():
    os.system('cls||clear')

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
    global limit_exceeded
    global p_name

    preferences = 0

    p_name = " "

    preferenced = ["1", "2"]
    preferencet = ["1", "2"]

    limit_exceeded = 0

    
    if p_num <= 24:
        clear()
        print("Crawdale Parents Eveining Booking Portal\n")
        print("Hello! You are Parent " + str(p_num) +  ".\n")
        
        p_name = input("Please enter your full name.\n")
        for preferences in range(2):

            if preferences == 0:
                print("\nPlease enter your first booking choice.\n")
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
            preferenced[preferences] = int(day)
            preferencet[preferences] = int(time)
            
            preferences += 1
            

        p_num += 1

        p_num_print = (str(p_num)+ "\n")
 
        f = open("bookings.txt", "r")
        p_lines = f.readlines()
        p_lines[0] = p_num_print

        f = open("bookings.txt", "w")
        f.writelines(p_lines)
        f.close()
    else:
        clear()
        print("All parents have booked.")
        limit_exceeded = 1
        exit()

def booking_verify():
    global p1_line
    global p2_line
    
    next = False
    b_pref =  0
    b_day = 0
    b_time = 0
    p1_line = ((preferenced[0] * 10) + preferencet[0])-7
    p2_line = ((preferenced[1] * 10) + preferencet[1])-7

    f = open("bookings.txt", "rt")

    if linecache.getline("bookings.txt", p1_line)[3] == " ":
        f.seek(0)
        lines = f.readlines()
        lines[(p1_line - 1)] = str(preferencet[0])+". " + p_name + "\n"

        f = open("bookings.txt", "wt")
        f.writelines(lines)
        f.close()
        b_pref = "1"
        b_day = preferenced[0]

        if preferencet[0] == 1:
            b_time = "17:00"
        elif preferencet[0] == 2:
            b_time = "17:20"
        elif preferencet[0] == 3:
            b_time = "17:40"
        elif preferencet[0] == 4:
            b_time = "18:00"
        elif preferencet[0] == 5:
            b_time = "18:20"
        elif preferencet[0] == 6:
            b_time = "18:40"
        elif preferencet[0] == 7:
            b_time = "19:00"
        elif preferencet[0] == 8:
            b_time = "19:20"
        elif preferencet[0] == 9:
            b_time = "19:40"
       
    elif linecache.getline("bookings.txt", p2_line)[3] == " ":
        f.seek(0)
        lines = f.readlines()
        lines[(p2_line - 1)] = str(preferencet[1]) + ". " + p_name + "\n"

        f = open("bookings.txt", "wt")
        f.writelines(lines)
        f.close()

        b_pref = "2"
        b_day = preferenced[1]

        if preferencet[1] == 1:
            b_time = "17:00"
        elif preferencet[1] == 2:
            b_time = "17:20"
        elif preferencet[1] == 3:
            b_time = "17:40"
        elif preferencet[1] == 4:
            b_time = "18:00"
        elif preferencet[1] == 5:
            b_time = "18:20"
        elif preferencet[1] == 6:
            b_time = "18:40"
        elif preferencet[1] == 7:
            b_time = "19:00"
        elif preferencet[1] == 8:
            b_time = "19:20"
        elif preferencet[1] == 9:
            b_time = "19:40"

    else:
        clear()
        print("Both Preferences Taken\n")
        while True:
            while True:
                b_prefd = input("What day would you like your booking on? Please enter 1, 2 or 3.\n")
                if b_prefd == "1" or b_prefd == "2" or b_prefd == "3":
                    break
                else:
                    clear()
                    print("Please enter 1, 2 or 3 only.")

            start_line = (int(b_prefd)*10)-8
            end_line = start_line + 10
            
            f = open("bookings.txt", "rt")

            print_lines = f.readlines()[start_line:end_line]
            f.close()
            while True:
                clear()
                print("Please select an available slot from the following list for the selected day.\nSlots without a name are available.\n")
                time.sleep(1.5)
                print(*print_lines)
                b_preft = input("Please select an available slot by entering its number.\nIf none of the slots suit you are none are available please enter 'next'.\n")
                
                bb_line = ((int(b_prefd)*10)+int(b_preft))-7

                f = open("bookings.txt", "rt")
                

                if str(b_preft) != "1" or b_preft != "2" or b_preft != "3" or b_preft != "4" or b_preft != "5" or b_preft != "6" or b_preft != "7" or b_preft != "8" or b_preft != "9" or b_preft != "next":
                    print("Please enter a number from 1-9 or 'next only.\n")
                    time.sleep(1.5)
                    f.close()
                elif b_preft == "next":
                    next = True
                    break
                    f.close()
                elif linecache.getline("bookings.txt", bb_line)[3] == " ":
                    b_pref = 3
                    f.seek(0)
                    lines = f.readlines()
                    lines[(bb_line - 1)] = str(b_preft) + ". " + p_name + "\n"

                    f = open("bookings.txt", "wt")
                    f.writelines(lines)
                    f.close()
                    b_day = b_prefd

                    if b_preft == "1":
                        b_time = "17:00"
                    elif b_preft == "2":
                        b_time = "17:20"
                    elif b_preft == "3":
                        b_time = "17:40"
                    elif b_preft == "4":
                        b_time = "18:00"
                    elif b_preft == "5":
                        b_time = "18:20"
                    elif b_preft == "6":
                        b_time = "18:40"
                    elif b_preft == "7":
                        b_time = "19:00"
                    elif b_preft == "8":
                        b_time = "19:20"
                    elif b_preft == "9":
                        b_time = "19:40"
                    
                    break
            
            if next != False:
                break


    print("Preference " + b_pref + " Booked")
    print("Your booking is on Day " + str(b_day) + " at " + str(b_time) + ".")
    
        
if exists("bookings.txt") == True:
    f = open("bookings.txt", "rt")
    p_num = int(f.readline(2))
    f.close()
else:
    f = open("bookings.txt", "x")
    f = open("bookings.txt", "wt")
    f.write(str(p_num))
    f.write("\n\nDay 1 Bookings\n1.  \n2.  \n3.  \n4.  \n5.  \n6.  \n7.  \n8.  \n9.  \nDay 2 Bookings\n1.  \n2.  \n3.  \n4.  \n5.  \n6.  \n7.  \n8.  \n9.  \nDay 3 Bookings\n1.  \n2.  \n3.  \n4.  \n5.  \n6.  \n7.  \n8.  \n9.  ")
    f.close()


clear()
print("Welcome to Crawdale Parents Evening System\n")
time.sleep(1.5)

user_selection()

if user == "p":
    p_input()
    if limit_exceeded == 0:
        booking_verify()
