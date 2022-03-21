###
#/***************************************************
#File Name: account_management.py
#Version/Date: FINAL (2020-06-02)
#Programmer/ID: Leong Xin-Nan (1191101536)
#Project Name: Password Generator
#Teammates: Teh Su Anne, Ooi Kher Ning and Chin Pei Wern
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###

import csv

import os.path

from os import path

#header for password data csv file
fieldnames2 = ["Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn","Google+","Youtube", "Pinterest", "Tumblr", "Reddit", "Quora", "Others"]
#header for account's password csv file
fieldnames = ['password']

#Function that check whether the login details is valid or not
def datachecker(a,b):
    username = a.get()
    password = b.get()

    if os.path.exists('./User/'+username+'.csv'):
        with open('./User/'+username+'.csv',"r+") as usernamelist:
            reader = csv.DictReader(usernamelist)
            for line in reader:
                if password == line['password']:
                    return True
    elif len(username.strip())== 0 or len(password.strip())==0:
        return False
    else:
        return False

#function of creating password,user,qrcode and barcode file for storing data                
def datafilecreator():
        if not os.path.exists('User'):
            os.mkdir('User')
        if not os.path.exists('Passwords'):
            os.mkdir('Passwords')
        if not os.path.exists('QRcode'):
            os.mkdir('QRcode')
        if not os.path.exists('BARcode'):
            os.mkdir('BARcode')

#function of validating the username the user inputted is being used or not
def registered_account(x,y):
    username = x.get()
    password = y.get()
    if os.path.exists('./User/'+username+'.csv'):
        return True
    elif len(username.strip()) == 0 or len(password.strip()) == 0:
        return True
    elif " " in username or " " in password:
        return True
    else:
        return False

#function of adding created account's data
def adding_account(x,y):
    username = x.get()
    password = y.get()
    with open('./User/'+username+'.csv',"w+") as account_data2:
        writingdata = csv.DictWriter(account_data2, fieldnames=fieldnames)
        writingdata.writeheader()
        writingdata.writerow({'password':password})
    with open('./Passwords/'+username+'.csv','w+') as a:
        b = csv.DictWriter(a,fieldnames=fieldnames2)
        b.writeheader()
        
#function of password manager
def  password_manager(user):
    with open('./Passwords/'+user+'.csv','r+') as passwordfile:
        reader = csv.DictReader(passwordfile,fieldnames=fieldnames2)
        facebookpass=[]
        instagrampass=[]
        twitterpass=[]
        snapchatpass=[]
        linkedinpass=[]
        googlepluspass=[]
        youtubepass=[]
        pinterestpass=[]
        tumblrpass=[]
        redditpass=[]
        quorapass=[]
        otherspass=[]
        for line in reader:
            facebookpass.append(line["Facebook"])
            instagrampass.append(line["Instagram"])
            twitterpass.append(line["Twitter"])
            snapchatpass.append(line["Snapchat"])
            linkedinpass.append(line["LinkedIn"])
            googlepluspass.append(line["Google+"])
            youtubepass.append(line["Youtube"])
            pinterestpass.append(line["Pinterest"])
            tumblrpass.append(line["Tumblr"])
            redditpass.append(line["Reddit"])
            quorapass.append(line["Quora"])
            otherspass.append(line["Others"])

#function of deleting a password
def deletePassword(user,pw,selectedcat):
    with open('./Passwords/'+user+'.csv')as passwordfile:
        reader = list(csv.DictReader(passwordfile))
        with open('./Passwords/'+user+'.csv','w') as passwordfile:
            writer = csv.DictWriter(passwordfile,fieldnames=fieldnames2)
            writer.writeheader()
            for row in reader:
                if pw != row[selectedcat]:
                    writer.writerow(row)