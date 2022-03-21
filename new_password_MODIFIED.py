#******************************************************#
#File Name: new_password.py
#Version/Date: FINAL (2020-06-02)
#Programmer/ID: Teh Su Anne (1191101019)
#Project Name: Random Password Generator
#Teammates: Leong Xin-Nan, Chin Pei Wern, Ooi Kher Ning
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#******************************************************#

import csv
import os.path
from os import path

fieldnames2 = ["Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn","Google+","Youtube", "Pinterest", "Tumblr", "Reddit", "Quora", "Others"]

#---------------------------------------- generate password ------------------------------------------#
def generatePassword(pwlength,alphalower,alphaupper,digit,specialchar):
    #use ASCII table to generate password
    import string
    import random
    password = ""
    for i in range (0,pwlength):
        if alphalower == 1 and alphaupper == 0 and digit == 0 and specialchar == 0:
            char = string.ascii_lowercase

        elif alphalower == 0 and alphaupper == 1 and digit == 0 and specialchar == 0:
            char = string.ascii_uppercase
        
        elif alphalower == 0 and alphaupper == 0 and digit == 1 and specialchar == 0:
            char = string.digits
        
        elif alphalower == 0 and alphaupper == 0 and digit == 0 and specialchar == 1:
            char = string.punctuation

        elif alphalower == 1 and alphaupper == 1 and digit == 0 and specialchar == 0:
            char = string.ascii_lowercase + string.ascii_uppercase
        
        elif alphalower == 1 and alphaupper == 0 and digit == 1 and specialchar == 0:
            char = string.ascii_lowercase + string.digits
        
        elif alphalower == 1 and alphaupper == 0 and digit == 0 and specialchar == 1:
            char = string.ascii_lowercase + string.punctuation
        
        elif alphalower == 0 and alphaupper == 1 and digit == 1 and specialchar == 0:
            char = string.ascii_uppercase + string.digits
        
        elif alphalower == 0 and alphaupper == 1 and digit == 0 and specialchar == 1:
            char = string.ascii_uppercase + string.punctuation
        
        elif alphalower == 0 and alphaupper == 0 and digit == 1 and specialchar == 1:
            char = string.digits + string.punctuation

        elif alphalower == 1 and alphaupper == 1 and digit == 1 and specialchar == 0:
            char = string.ascii_lowercase + string.ascii_uppercase + string.digits
        
        elif alphalower == 1 and alphaupper == 1 and digit == 0 and specialchar == 1:
            char = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        
        elif alphalower == 1 and alphaupper == 0 and digit == 1 and specialchar == 1:
            char = string.ascii_lowercase + string.digits + string.punctuation
        
        elif alphalower == 0 and alphaupper == 1 and digit == 1 and specialchar == 1:
            char = string.ascii_uppercase + string.digits + string.punctuation

        elif alphalower == 1 and alphaupper == 1 and digit == 1 and specialchar == 1:
            char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        #randomly generate a combination of password based on the user's choice by using ascii table
        word = random.choice(char)
        password = password + word

    return password

#----------------------------------------- save password into csv ------------------------------------#
def savePassword(user,pw,selectedcat):
    with open('./Passwords/'+user+'.csv','a+',newline='') as passwordfile:
        writer = csv.DictWriter(passwordfile,fieldnames=fieldnames2)
        writer.writerow({selectedcat:pw})