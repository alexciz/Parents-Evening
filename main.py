import sys

def clear():
    # \033[H homes the cursor
    # \033[2J Clears the screen and sets the cursor back to top left
    sys.stdout.write("\033[H\033[2J\033[H")


slots = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

x = 1
y = 1
d = 1

while x <= 24:
    clear()
    print("Hello! You are Parent " + str(x) +  "\n")
    p_id = x+10

    while d == 1:
        day = int(input("What day would you like your appointment on? Please enter a number from 1-3.\n"))

        if day == 1:
            d = 0
        elif day == 2:
            d = 0
        elif day == 3:
            d = 0
        else:
            print("Please enter 1, 2 or 3.\n")
    d = 1
    day -= 1
    while y == 1:
        print("\nPlease select a time from the following list:")
        print("17:00, 17:20, 17:40, 18:00, 18:20, 18:40, 19:00, 19:20, 19:40")
        time = str(input())
        y = 0
        if time == "17:00":
            time = 0
        elif time == "17:20":
            time = 1
        elif time == "17:40":
            time = 2
        elif time == "18:00":
            time = 3
        elif time == "18:20":
            time = 4
        elif time == "18:40":
            time = 5
        elif time == "19:00":
            time = 6
        elif time == "19:20":
            time = 7
        elif time == "19:40":
            time = 8
        else:
            print("Please enter a valid time.")
            y = 1
        preference1d = day
        preference1t = time

    y = 1
    x += 1
