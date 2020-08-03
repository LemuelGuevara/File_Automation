#!/usr/bin/python3
import sys

def test():
    curr_input = input("Create: ")
        
    if curr_input.endswith("py"):
        usr_data = curr_input.split()
        print(usr_data[0])
        
    
    else:
        print("Error")
    
test()
