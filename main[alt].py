import itertools
import threading
import colorama
import time
import sys
import os

os.system("")
colorama.init()


# border creation with text input
def bordered(text):
    text = str(text)
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


def printin(text, inset):
    text = str(text)
    inset = str(inset)
    lines = text.splitlines()
    inset = "\033[" + inset + "C"
    for line in lines:
        print(inset + line)


def clear():
    # \033[H homes the cursor
    # \033[2J Clears the screen and sets the cursor back to top left
    sys.stdout.write("\033[H\033[2J\033[H")


# here is the animation
def animateStart():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!    ')


def loadingWheel(timetotal):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if timetotal <= 0:
            break
        sys.stdout.write(c + '\033[?25l\033[1D')
        sys.stdout.flush()
        time.sleep(0.1)
        timetotal = timetotal - 0.1
    sys.stdout.write('\033[?25h\033[1D  \033[1D')


def loadingLine(amount):
    line = ""
    line = "-" * amount
    if amount > 99:
        print("WARNING THIS MAY NOT BE ABLE TO PROCEED TO THE PREVOIUS LINE")
    sys.stdout.write(line + " ")
    for c in range(len(line)):                                          # This step back method is much more optimized then
        sys.stdout.write("\033[?25l\033[1D \033[1D")                    # the previous screen by screen method for a large amount
        sys.stdout.flush()
        time.sleep(0.2)
    sys.stdout.write(" \r")


clear()

# print("PLEASE MAKE SURE YOU HAVE AT LEAST 23 LINES OF SPACE AND ALL THE MODULES INSTALLED!")
# print("THE MODULES ARE ITERTOOLS, THREADING, COLORAMA, TIME, SYS AND OS ")
print("Press [Enter] to proceed")
input()
clear()

done = False
# loading wheel
t = threading.Thread(target=animateStart)
t.start()
# code here
time.sleep(1)
done = True
time.sleep(0.7)
clear()
done = False

print(bordered("Hello!"))
hello = True
time.sleep(1)
