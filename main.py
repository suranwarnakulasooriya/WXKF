import sys
import time
from init import *
from commands import *


while True:
    raw = str(input("> "))
    if raw != '': # if enter was hit, just give the prompt again
        st = raw.split() # split input into words
        cm = st[0] # command name
        c = 0 # commmand to be used, starts as 0
        for cmd in C: # find the command
            if cm == cmd.name:
                c = cmd
        if c == 0: # if it wasn't found, give error
            print(f"ERROR: '{cm}' is not a command.")
        else: # if the command was valid
            st.pop(0) # remove command from words, st is now a list of arguments
            # check for the right number of arguments
            if len(st) < c.xargs:
                print("ERROR: Too few arguments.")
            elif len(st) > c.xargs:
                print("ERROR: Too many arguments.")
            else: # if there was a correct number of arguments, invoke the command
                if c.xargs == 0:
                    c.func()
                elif c.xargs == 1:
                    c.func(st[0])
                elif c.xargs == 2:
                    c.func(st[0],st[1])
                elif c.xargs == 3:
                    c.func(st[0],st[1],st[2])
