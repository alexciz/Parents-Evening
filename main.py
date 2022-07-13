slots = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

x=1
y=1

while x<=24:
    print("Hello! You are Parent", x)
    p_id = x+10
    day = int(input("What day would you like your appointment on? Please enter a number from 1-3. "))
    day-=1
    while y == 1:
        print("Please select a time from the following list:")
        print("17:00, 17:20, 17:40, 18:00, 18:20, 18:40, 19:00, 19:20, 19:40")
        time = str(input())

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
            time =6
    x+=1
