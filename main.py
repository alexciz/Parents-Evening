times = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["1", "2", "3", "4", "5", "6", "7", "8", "9"]]

x=1

while x<=24:
    print("Hello! You are Parent", x)
    p_id = x
    day = int(input("What day would you like your appointment on? Please enter a number from 1-3. "))
    day-=1
    x+=1
