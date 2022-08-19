from genericpath import exists
import msvcrt
import time
import os

p_num = 1
slots = 0

if exists("bookings.txt") == True:
    f = open("bookings.txt", "rt")
    p_num = int(f.readline(1))
    f.close()
else:
    f = open("bookings.txt", "x")
    f = open("bookings.txt", "wt")
    f.write(str(p_num))
    f.write("\n\nDay 1 Bookings\n1.  \n2.  \n3.  \n4.  \n5.  \n6.  \n7.  \n8.  \n9.  \nDay 2 Bookings\n1.  \n2.  \n3.  \n4.  \n5.  \n6.  \n7.  \n8.  \n9.  \nDay 3 Bookings\n1.  \n2.  \n3.  \n4.  \n5.  \n6.  \n7.  \n8.  \n9.  ")
    f.close()

f = open("bookings.txt", "rt")
f.seek(0)
slots = f.readlines()
f.close()

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
    reset = f"\033[0m"

    while True:
        clear()
        u_input = input("Are you a parent?\n")
        if u_input == "No" or u_input == "no" or u_input == "n" or u_input == "N" or u_input == "NO":
            clear()
            print("Teacher Login")
            while True:
                print("Password:")
                hidden_input()
                if passwor == t_password:
                    user = "t"
                    print("\033[1;32m \nAccess Granted" + reset)
                    break
                else:
                    remaining_attempts -=1
                    clear()
                    print("Incorrect Password\nYou have", remaining_attempts ,"attempts remaining.")

                if remaining_attempts == 0:
                    print("Password Attempt Limit Exceeded")
                    exit()
            break
        elif u_input == "Yes" or u_input == "yes" or u_input == "y" or u_input == "Y" or u_input == "YES":
            user = "p"
            break
        else:
            print("Please enter Yes or No.")
            time.sleep(0.7)

def print_timetable():
    time.sleep(0.5)
    clear()
    print("Parents Evening Bookings\n")
    print(*slots[3:])
    while True:
        stop = input("\nPlease enter 'stop' to exit teacher mode.\n")
        if stop == "stop":
            break
        
    
def p_menu():
    clear()
    while True:
        p_option = input("Please select what you would like to do by entering the corresponding number.\n1 = Book new appointment\n2 = Cancel an appointment\n")
        if p_option == "1":
            p_option = "new_apt"
            break
        elif p_option == "2":
            p_option = "cancel_apt"
            break
        else:
            clear()
            print("Please enter 1 or 2 only.\n")
    
    return p_option

def cancel_apt():
    name_conf = 1
    reset = f"\033[0m"

    clear()
    while True:
        cancel_day = input("What day is the appointment on that you would like to cancel? Please enter 1, 2 or 3.\n")
        if cancel_day == "1":
            break
        elif cancel_day == "2":
            break
        elif cancel_day == "3":
            break
        else:
            clear()
            print("Please enter 1, 2 or 3 only.\n")
    clear()
    while True:
        
        cancel_time = input("Please select the time of your appoitment from the following list:\n1 = 17:00\n2 = 17:20\n3 = 17:40\n4 = 18:00\n5 = 18:20\n6 = 18:40\n7 = 19:00\n8 = 19:20\n9 = 19:40\n")
        
        if cancel_time == "1":
            break
        elif cancel_time == "2":
            break
        elif cancel_time == "3":
            break
        elif cancel_time == "4":
            break
        elif cancel_time == "5":
            break
        elif cancel_time == "6":
            break
        elif cancel_time == "7":
            break
        elif cancel_time == "8":
            break
        elif cancel_time == "9":
            break
        else:
            clear()
            print("\nPlease enter a number from 1-9.")
    
    cancel_index = ((int(cancel_day)*10)+int(cancel_time))-8
    
    clear()

    while True:
        
        cancel_name = input("Please enter the name on the appointment you would like to cancel:\n")
        if slots[cancel_index][3:] == cancel_name+"\n":
            slots[cancel_index] = cancel_time+".  \n"

            print("\033[1;32mAppointment Cancelled" + reset)
            time.sleep(1.5)
            break
        else:
            name_conf += 1

        if name_conf == 3:
            clear()
            print("Name does not match.\nName Confirmation Attempt Limit Exceeded")
            exit()
        else:
            clear()
            print("Name does not match.\nYou have one more attempt.\n")


def p_input():

    global p_num
    global preferences
    global preferenced
    global preferencet
    global p_name

    preferences = 0

    p_name = " "

    preferenced = ["1", "2"]
    preferencet = ["1", "2"]

    
    if p_num <= 24:
        clear()
        print("Crawdale Parents Eveining Booking Portal\n")
        print("Hello! You are Parent " + str(p_num) +  ".\n")
        
        p_name = input("Please enter your full name.\n")
        for preferences in range(2):

            if preferences == 0:
                print("\nPlease enter your first booking choice.\n")
            else:
                clear()
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
                time = input()
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

        p_num_print = str(p_num)+ "\n"

        slots[0] = p_num_print

    else:
        clear()
        print("All parents have booked.")
        exit()

def booking_verify():
    global p1_line
    global p2_line

    b_pref =  0
    b_day = 0
    b_time = 0
    p1_index = ((preferenced[0] * 10) + preferencet[0])-8
    p2_index = ((preferenced[1] * 10) + preferencet[1])-8
    next_day = 0
    booked = False

    if slots[p1_index][3] == " ":
        slots[p1_index] = str(preferencet[0])+". " + p_name + "\n"

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
       
    elif slots[p2_index][3] == " ":
        slots[p2_index] = str(preferencet[1]) + ". " + p_name + "\n"

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
            

            while True:
                clear()
                print("Please select an available slot from the following list for the selected day.\nSlots without a name are available.\n")
                print(*slots[start_line:end_line])
                b_preft = input("Please select an available slot by entering its number.\nIf none of the slots suit you are none are available please enter 'next'.\n")
                
                if b_preft.isnumeric() == True: 
                    bb_index = ((int(b_prefd)*10)+int(b_preft))-8

                if b_preft == "next":
                    clear()
                    next_day = 1
                    break
                elif b_preft.isnumeric() == False:
                    print("\nPlease enter a number from 1-9 or 'next' only.")
                    time.sleep(1.7)
                elif int(b_preft) not in range(1,10):
                    print("\nPlease enter a number from 1-9 or 'next' only.")
                    time.sleep(1.7)
                elif slots[bb_index][3] == " ":
                    b_pref = "3"
                    slots[bb_index] = str(b_preft) + ". " + p_name + "\n"

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
                    
                    next_day = 0
                    
                    break
                else:
                    clear()
                    print("The seleced slot is not available.")
                    time.sleep(1)
            
            if next_day == 0:
                break


    print("Preference " + b_pref + " Booked")
    print("Your booking is on Day " + str(b_day) + " at " + b_time + ".")
    time.sleep(2)
    
def stop():
    clear()
    while True:
        stop = input("Would you like to stop the program? Please enter yes or no.\n")
        if stop == "Yes" or stop == "yes" or stop == "Y" or stop == "YES" or stop == "y":
            clear()

            f = open("bookings.txt", "wt")
            f.writelines(slots)
            f.close()

            print("Goodbye!\n")
            time.sleep(0.5)
            print("██████╗░██╗░░░██╗███████╗\n██╔══██╗╚██╗░██╔╝██╔════╝\n██████╦╝░╚████╔╝░█████╗░░\n██╔══██╗░░╚██╔╝░░██╔══╝░░\n██████╦╝░░░██║░░░███████╗\n╚═════╝░░░░╚═╝░░░╚══════╝")
            exit()
        elif stop == "No" or stop == "no" or stop == "n" or stop == "NO" or stop == "N":
            break
        else:
            clear()
            print("Please enter yes or no only.\n")

while True:
    clear()
    print("Welcome to Crawdale Parents Evening System\n")
    time.sleep(1.5)

    user_selection()

    if user == "p":
        if p_menu() == "new_apt":
            p_input()
            booking_verify()
        else:
            cancel_apt()
    else:
        print_timetable()
    stop()
