###
#/***************************************************
#File Name    : M4_ChinPeiWern_1191101668.py
#Version/Date : v2 (2020-05-05)
#Programmer/ID: Chin Pei Wern (1191101668)
#Project Name : Random Password Generator
#Teammates    : Teh Su Anne, Leong Xin-Nan, Ooi Kher Ning
#Course/Term  : PSP0201 Mini IT Project (2019/20 T3)
#***************************************************/
###

##Modules of account management and password manager
import account_management

#Modules of password configuration and generation
#import new_password

from tkinter import *
import tkinter.messagebox   ##import messagebox
from tkinter import Text, Tk    ##import textbox
import csv
import os.path
from os import path

fieldnames2 = ["Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn","Google+","Youtube", "Pinterest", "Tumblr", "Reddit", "Quora", "Others"]

window = Tk()
window.title("Random Password Generator")

#Change interface's frames
def raise_frame(frame):
    frame.tkraise()

#menubar 
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Home", command=lambda:first_frame_menubar_home())
filemenu.add_separator()

filemenu.add_command(label="Generate Password", command=lambda:first_frame_menubar_generatepassword())
filemenu.add_command(label="Password Manager", command=lambda:first_frame_menubar_passwordmananger())
filemenu.add_command(label="QR code / Barcode", command=lambda:first_frame_menubar_qrcode_barcode())
filemenu.add_command(label="Log out" , command=lambda:first_frame_menubar_qrcode_logout())
filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Menu", menu=filemenu)

#logoutmenu = Menu(menubar, tearoff=0)

window.config(menu=menubar)
window.configure(bg="#222930")

##frames 
login = Frame(window)
register = Frame(window)
mainMenu = Frame(window)
passwordStructure = Frame(window)
social_media = Frame(window)
confirm = Frame(window)
randomised_password = Frame(window)
deny = Frame(window)
code = Frame(window)
display = Frame(window)
codePassword = Frame(window)
randomPassword = Frame(window)
codeoption = Frame(window)
notes = Frame(window)
password_manager = Frame(window)
socialmedia = Frame(window)
work = Frame(window)
entertainment = Frame(window)
study = Frame(window)
customise = Frame(window)



for frame in (login, register, mainMenu, passwordStructure, social_media, confirm,
              randomised_password, deny, code, codeoption, codePassword, display, notes,
              password_manager, randomPassword, socialmedia, work, entertainment, study, customise) :
    frame.grid(row=0, column=0, sticky="news")
    frame.configure(bg="#222930")

window_height = 500
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
  
### after choosing password structure, confirmation  
def popup_confirm():
    result=tkinter.messagebox.askquestion("CONFIRMATION", "Do you confirm with the option?")
    if result=="yes":
        window.destroy
        raise_frame(randomised_password)
    else:
        window.destroy

### confirmation qr code barcode
def code_popup_confirm():
    result=tkinter.messagebox.askquestion("CONFIRMATION", "Do you confirm with the option?")
    if result=="yes":
        window.destroy
        raise_frame(randomPassword)
    else:
        window.destroy
 
def code_popupOption():
    option = tkinter.messagebox.askquestion("OPTION", "Do you want to regenerate with the same structure?")
    if option=="yes":
        window.destroy
        raise_frame(randomPassword)
    else:
        window.destroy
        raise_frame(codePassword)
        
### after deny the generated password
def popupOption():
    option = tkinter.messagebox.askquestion("OPTION", "Do you want to regenerate with the same structure?")
    if option=="yes":
        window.destroy
        raise_frame(randomised_password)
    else:
        window.destroy
        raise_frame(password)

#### message info for user ###        
def info():
    saved = tkinter.messagebox.showinfo("Data saved", "SAVED")

###after denying the generated password for QRcode / Barcode ###    
def popupConfirm():
    Result = tkinter.messagebox.askquestion("CONFIRMATION", "Do you confirm with the option?")
    if Result == "yes":
        window.destroy
        raise_frame(randomisedPassword)
    else:
        window.destroy
        raise_frame(code)

###confirm to change password in password manager
def popupConfirmChanges():
    result = tkinter.messagebox.askquestion("CHANGE PASSWORD", "Do you want to change the password?")
    if result == "yes":
        window.destroy
        raise_frame(password)    
    else:
        window.destroy
### confirm selection
def popupQr():
    result = tkinter.messagebox.askquestion("CONFIRMATION", "Do you confirm with the option?")
    if result == "yes":
        window.destroy
        raise_frame(codeoption)
    else:
        window.destroy
        
def popupBarcode():
    result = tkinter.messagebox.askquestion("CONFIRMATION", "Do you confirm with the option?")
    if result == "yes":
        window.destroy
        raise_frame(codeoption)
    else:
        window.destroy

def generate_Password():
    result = tkinter.messagebox.askquestion("GENERATE PASSWORD", "Do you want to generate password for this category?")
    if result == "yes":
        window.destroy
        raise_frame(codePassword)
    else:
        window.destroy

###confirm to remove password from password manager        
def popUpconfirmRemove():
    result = tkinter.messagebox.askquestion("REMOVE PASSWORD", "Do you want to remove the password?")
    if result == "yes":
        window.destroy
    
    else:
        window.destroy


def confirmData():
    result = tkinter.messagebox.askquestion("SAVE DATA", "Do you want to make any changes?")
    if result == "yes":
        window.destroy
    else:
        window.destroy
        raise_frame(display)

#Error window when invalid username/password
def login_error():
    result = tkinter.messagebox.showerror("ERROR", "Invalid Username/Passsword! Please try again!")

def register_error():
    result = tkinter.messagebox.showerror("ERROR", "Used Username/Password! Please try again!")

#Function that is giving the commands what to do when login details are valid/invalid
def account_verify():
    global login_status
    login_status = account_management.datachecker(login_username,login_password)
    if login_status == True:
        global currentuser
        currentuser = entUsername.get()
        raise_frame(mainMenu)
    else:
        login_error()

    entUsername.delete(0,END)
    entPassword.delete(0,END)

#Function for validating login details for menubar of first frame [Generate Password Button]
def first_frame_menubar_generatepassword():
    if login_status == True:
        raise_frame(passwordStructure)
    else:
        login_error()

#Function for validating login details for menubar of first frame [Passowrd Manger Button]
def first_frame_menubar_passwordmananger():
    if login_status == True:
        raise_frame(password_manager)
    else:
        login_error()

#Function for validating login details for menubar of first frame [QR Code/Bar Code Button]
def first_frame_menubar_qrcode_barcode():
    if login_status == True:
        raise_frame(code)
    else:
        login_error()

#Function for logout button
def first_frame_menubar_qrcode_logout():
    global login_status
    login_status = False
    raise_frame(login)

    
#Function for validating login details for menubar of first frame [Home Button]
def first_frame_menubar_home():
    if login_status == True:
        raise_frame(mainMenu)
    else:
        login_error()

#fuction of regsitering account
def registration():
    status = account_management.registered_account(registerusername,registerpassword)
    if status == True:
        register_error()
    else:
        account_management.adding_account(registerusername,registerpassword)
        result = tkinter.messagebox.showinfo("", "Account created successfully!")
        raise_frame(login)
    
    entusername.delete(0,END)
    entpassword.delete(0,END)

#function of password manager
def  password_manager_display(user):
    with open('./Passwords/'+user+'.csv','r+') as passwordfile:
        reader = csv.DictReader(passwordfile,fieldnames=fieldnames2)
        next(reader)
        global facebookpass,instagrampass,twitterpass,snapchatpass,linkedinpass,googlepluspass,youtubepass,pinterestpass,tumblrpass,redditpass,quorapass,otherspass
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

#function of removing password in password manager
#def removing_password():


        
#Function from account_management.py; purpose is to create account_data.csv
account_management.datafilecreator()

##frame 1

lblUsername = Label(login, text="USERNAME: ", font="courier 13 bold", fg="#E9E9E9", bg="#222930",  height= 1)
lblUsername.grid(row=1, column= 0, padx=200, pady=20, sticky=E)


lblPassword = Label(login, text="PASSWORD: ", font="courier 13 bold", fg="#E9E9E9", bg="#222930", height=1)
lblPassword.grid(row=2, column = 0, padx=200, pady=20, sticky=E)

login_username = StringVar()
entUsername = Entry(login, width=20, textvariable=login_username)
entUsername.grid(row=1, column=1, sticky=W)

login_password = StringVar()
bullet = "\u2022"   ##bullet character###
entPassword = Entry(login, width=20, textvariable=login_password, show=bullet)
entPassword.grid(row=2, column=1, sticky=W)

btnLogin = Button(login, bg="#4EB1BA", width= 10, text="LOG IN",font="system 10 bold",
                   fg="#E9E9E9", command=lambda:account_verify())

btnLogin.grid(row=3, column=0,sticky=E, padx=20, pady=20)

lblLogin = Label(login, text="Don't have an account?", font="verdana 8 italic",  fg="#E9E9E9", bg="#222930")
lblLogin.grid(row=7, column=0, padx=20, pady=50, sticky=E)

btnSignup = Button(login, bg="#4EB1BA",width=10, fg="#E9E9E9", 
                    text="SIGN UP", command=lambda:raise_frame(register))
btnSignup.grid(row=7, column=1,pady=50, sticky=W)


##frame 2 Register for new users
lblRegister = Label(register, text="REGISTER YOUR ACCOUNT", fg="#E9E9E9", bg="#222930", font="fixedsys 17 bold")
lblRegister.grid(row=0, column=0, columnspan=2, padx=300, pady=20)

lblusername = Label(register, text="USERNAME: ", fg="#E9E9E9", bg="#222930", font="system 12 bold")
lblusername.grid(row=1, column=0, padx=10, pady=10, sticky=E)

lblMasterPassword = Label(register, text="MASTER PASSWORD: ", fg="#E9E9E9", bg="#222930", font="system 12 bold")
lblMasterPassword.grid(row=2, column=0, padx= 10, pady= 10, sticky=E)

registerusername = StringVar()
entusername= Entry(register, width=20, bg="light grey", textvariable= registerusername)
entusername.grid(row=1, column=1, sticky=W)

registerpassword = StringVar()
bullet = "\u2022"
entpassword = Entry(register, width=20, bg="light grey", textvariable= registerpassword, show=bullet)
entpassword.grid(row=2, column=1, sticky=W)

btnRegister = Button(register, text="SIGN UP", font="system 10 bold", fg="#E9E9E9", bg="#4EB1BA", command=lambda:registration())
btnRegister.grid(row=4, column=0,columnspan=2, padx=200, pady=20)


##frame 3 main menu
lblmenu = Label(mainMenu, text="MAIN MENU", fg="#E9E9E9", bg="#222930", font="fixedsys 15 bold")
lblmenu.grid(row=1, column=0, columnspan=2, padx=50, pady=20, sticky="news")

btnNewPassword = Button(mainMenu, text="Generate New Password", fg="#E9E9E9", bg="#4EB1BA",
                    font="system 13", command=lambda:raise_frame(passwordStructure))
btnNewPassword.grid(row=2, column=0,columnspan=2, padx=50, pady=15)

btnManager = Button(mainMenu, text="Password Manager", 
                    font="system 13", bg="#4EB1BA", fg="#E9E9E9", command=lambda:raise_frame(password_manager))
btnManager.grid(row=3, column=0, columnspan=2, padx=50, pady=15)

btnQR = Button(mainMenu, text="QR code / Barcode", font="system 13", bg="#4EB1BA", fg="#E9E9E9", 
        command=lambda:raise_frame(code))
btnQR.grid(row=4, column=0, columnspan=2, padx=50, pady=15)


###frame 4 generate new password
lblStructure = Label(passwordStructure, text="PASSWORD STRUCTURE", bg="#222930", fg="#E9E9E9", font="fixedsys 17 bold underline")
lblStructure.grid(row=0, column=0, columnspan=2, padx=300, pady=15, sticky="news")
 
lblLength = Label(passwordStructure, text="Password Length: (6-40)", bg="#222930", fg="#E9E9E9", font="verdana 10")
lblLength.grid(row= 1, column = 0, columnspan=2, padx= 300, pady= 10, sticky=W)

scale_widget = Scale(passwordStructure, from_=6, to=40, orient= HORIZONTAL, bg="#4EB1BA",  fg="#E9E9E9")
scale_widget.set(6)
scale_widget.grid(row=2,column=0, columnspan=2, padx=300, pady=10)


var1 = IntVar()
Checkbutton(passwordStructure, variable=var1, bg="#222930").grid(row=4, column=1, sticky="news")
lblalpha = Label(passwordStructure, text="Alphabets lowercase(a-z)", bg="#222930", fg="#E9E9E9", font="verdana 10")
lblalpha.grid(row=4, column=0, columnspan=2, padx=200, pady=10, sticky=W)

var2 = IntVar()
Checkbutton(passwordStructure, variable=var2, bg="#222930").grid(row=5, column=1, sticky="news")
lblAlpha = Label(passwordStructure, text="Alphabets uppercase(a-z)", bg="#222930", fg="#E9E9E9", font="verdana 10")
lblAlpha.grid(row=5, column=0, columnspan=2, padx=200, pady=10, sticky=W)

var3 = IntVar()
Checkbutton(passwordStructure, variable=var3, bg="#222930").grid(row=6, column=1, sticky="news")
lblDigits = Label(passwordStructure, text="Digits", font="verdana 10", bg="#222930", fg="#E9E9E9")
lblDigits.grid(row=6, column=0, columnspan=2, padx=200, pady=10, sticky=W)

var4 = IntVar()
Checkbutton(passwordStructure, variable=var4, bg="#222930").grid(row=7, column=1, sticky="news")
lblSpch = Label(passwordStructure, text="Special Characters", font="verdana 10", bg="#222930", fg="#E9E9E9")
lblSpch.grid(row=7, column=0, columnspan=2, padx=200, pady= 10, sticky=W)

btnGenerate = Button(passwordStructure, text="GENERATE",font="courier 10", bg="#4EB1BA", fg="#E9E9E9", command=popup_confirm)
btnGenerate.grid(row=8, column=1, padx=20, pady=10, sticky=E)



###if confirm, password generated
lblPasswordGenerator = Label(randomised_password, text="PASSWORD GENERATOR", font="fixedsys 17 bold", fg="#E9E9E9", bg="#222930")
lblPasswordGenerator.grid(row=0,columnspan=2, padx=300, pady=20, sticky="news")

lblRandomisedPassword = Label(randomised_password, text="PASSWORD: ", font="system 10", bg="#222930", fg="#E9E9E9")
lblRandomisedPassword.grid(row=1, column=0, columnspan=2, padx=200, pady=0, sticky=W)

entRandomisedPassword = Entry(randomised_password, width=55, state="readonly")
entRandomisedPassword.grid(row=2, column=0,columnspan=2, padx=200, pady=20, sticky=W)

btnAccept = Button(randomised_password, text="ACCEPT", font="courier 10", bg="#4EB1BA", fg="#E9E9E9", 
            command=lambda:raise_frame(social_media))
btnAccept.grid(row=3, column=0, padx=100, pady=20)

btnDeny = Button(randomised_password, text="DENY", font="courier 10", bg="#4EB1BA", fg="#E9E9E9", command=popupOption)
btnDeny.grid(row=3, column=1, padx=100, pady= 20)

###frame 5 choose which social media to save into
lblSocialMedia = Label(social_media, text="Choose from the following social media: ", bg="#222930", fg="#E9E9E9", font="arial 13")
lblSocialMedia.grid(row=1, column=0, columnspan=2, padx=300, pady=20)

listbox = Listbox(social_media, height=15, 
                  width=30, 
                  font="fixedsys 10", 
                  fg="black")

index = 1
for i in ("Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn","Google+", 
"Youtube", "Pinterest", "Tumblr", "Reddit", "Quora", "Others"):
    listbox.insert(index, i)
    index +=1

listbox.grid(row=3, column=0, columnspan=2, padx=150, pady=0)

btnProceed = Button(social_media, text="PROCEED",font="courier 10", bg="#4EB1BA", fg="#E9E9E9", command=info)
btnProceed.grid(row=4, column=1, padx= 50, pady=20)


###frame6 barcode / qrcode mainpage
lblChoose = Label(code, text="CHOOSE AN OPTION:", font="fixedsys 17 bold", bg="#222930", fg="#E9E9E9")
lblChoose.grid(row=1,column=0, columnspan=2, padx= 300, pady=20, sticky="news")

btnQr = Button(code, text="QR CODE", font="system 10 bold", bg="#4EB1BA", fg="#E9E9E9", command= popupQr)
btnQr.grid(row=3, column=0, padx=175, pady=20, sticky=W)
btnBarcode = Button(code, text="BARCODE", font="system 10 bold", bg="#4EB1BA", fg="#E9E9E9",
            command= popupBarcode)
btnBarcode.grid(row=3, column=1, padx=175, pady=20, sticky=W)

###frame7 enter data  into which category (qrcode)
lblCategory = Label(codeoption, text="CHOOSE CATEGORY: ", font="fixedsys 20 bold", bg="#222930", fg="#E9E9E9")
lblCategory.grid(row=1,column=0, columnspan=2, padx= 350, pady=20, sticky="news")

listboxCategory = Listbox(codeoption, height=17, width=27, font="fixedsys 13", fg="black")

index = 1
for i in ("Social Media", "Entertainment", "Work", "Study", "Customise"):
    listboxCategory.insert(index, i)
    index += 1
listboxCategory.grid(row=3, column=0, columnspan=2, padx=100, pady=0)

lblSm = Label(socialmedia, text= "SOCIAL MEDIA", font="fixedsys 20 bold", bg="#222930", fg="#E9E9E9")
lblSm.grid(row=1,column=0, columnspan=2, padx= 350, pady=20, sticky="news")

listboxSocialMedia = Listbox(socialmedia, height=17, width=30, font="fixedsys 13", fg="black")

for i in ('Facebook', 'Instagram', 'WeChat', 'Line', 'Snapchat', 'Google', 'Telegram', 'LinkedIn'):
    listboxSocialMedia.insert( index, i)
    index += 1
listboxSocialMedia.grid(row=3, column=0, columnspan=2, padx=100, pady=0)

##Entertainment
lblEnt = Label(entertainment, text = "ENTERTAINMENT", font="fixedsys 20 bold", bg="#222930", fg="#E9E9E9")
lblEnt.grid(row=1,column=0, columnspan=2, padx= 350, pady=20, sticky="news")

listboxEnt = Listbox(entertainment,height=17, width=30, font="fixedsys 13", fg="black")
for i in ('Netflix', 'iFlix', 'YouTube', 'iQiyi', 'TikTok'):
    listboxEnt.insert(index, i)
    index += 1
listboxEnt.grid(row=3, column=0, columnspan=2, padx=100, pady=0)

##work
lblWork = Label(work, text = "WORK", font="fixedsys 20 bold", bg="#222930", fg="#E9E9E9")
lblWork.grid(row=1,column=0, columnspan=2, padx= 400, pady=20, sticky="news")

listboxWork = Listbox(work,height=17, width=30, font="fixedsys 13", fg="black")
for i in ('Bank', 'Office', 'Email', 'Contact'):
    listboxWork.insert(index, i)
    index += 1
listboxWork.grid(row=3, column=0, columnspan=2, padx=100, pady=0)
##study
lblStudy = Label(study, text = "STUDY", font="fixedsys 20 bold", bg="#222930", fg="#E9E9E9")
lblStudy.grid(row=1,column=0, columnspan=2, padx= 250, pady=20, sticky="news")
listboxStudy = Listbox(study,height=17, width=30, font="fixedsys 13", fg="black")
for i in ('College', 'Coursera', 'High School', 'Tuition', 'Udemy', 'Duolingo', 'Memrise', 'Mathway'):
    listboxStudy.insert(index, i)
    index += 1
listboxStudy.grid(row=3, column=0, columnspan=2, padx=100, pady=0)   

##customise
lblCust = Label(customise, text = "WORK", font="fixedsys 20 bold", bg="#222930", fg="#E9E9E9")
lblCust.grid(row=1,column=0, columnspan=2, padx= 350, pady=20, sticky="news")

listboxCust = Listbox(customise,height=17, width=30, font="fixedsys 13", fg="black")
listboxCust.grid(row=3, column=0, columnspan=2, padx=100, pady=0)

def option_onselect(option):
    w = option.widget
    index = (w.curselection()[0])
    if index == 0:
        raise_frame(socialmedia)
    if index == 1:
        raise_frame(entertainment)
    if index == 2:
        raise_frame(work)
    if index == 3:
        raise_frame(study)
    if index == 4:
        raise_frame(customise)

def onselect(sm):
    w = sm.widget
    index = (w.curselection()[0])
    generate_Password()

listboxCategory.bind('<<ListboxSelect>>', option_onselect)   
listboxSocialMedia.bind('<<ListboxSelect>>', onselect)
listboxEnt.bind('<<ListboxSelect>>', onselect)
listboxWork.bind('<<ListboxSelect>>', onselect)
listboxStudy.bind('<<ListboxSelect>>', onselect)
listboxCust.bind('<<ListboxSelect>>', onselect)

##if want to generate password
lblStructure = Label(codePassword, text="PASSWORD STRUCTURE", bg="#222930", fg="#E9E9E9", font="fixedsys 17 bold underline")
lblStructure.grid(row=0, column=0, columnspan=2, padx=300, pady=15, sticky="news")
 
lblLength = Label(codePassword, text="Password Length: (6-40)", bg="#222930", fg="#E9E9E9", font="verdana 10")
lblLength.grid(row= 1, column = 0, columnspan=2, padx= 300, pady= 10, sticky=W)

scale_widget = Scale(codePassword, from_=6, to=40, orient= HORIZONTAL, bg="#4EB1BA",  fg="#E9E9E9")
scale_widget.set(6)
scale_widget.grid(row=2,column=0, columnspan=2, padx=300, pady=10)


var1 = IntVar()
Checkbutton(codePassword, variable=var1, bg="#222930").grid(row=4, column=1, sticky="news")
lblalpha = Label(codePassword, text="Alphabets lowercase(a-z)", bg="#222930", fg="#E9E9E9", font="verdana 10")
lblalpha.grid(row=4, column=0, columnspan=2, padx=200, pady=10, sticky=W)

var2 = IntVar()
Checkbutton(codePassword, variable=var2, bg="#222930").grid(row=5, column=1, sticky="news")
lblAlpha = Label(codePassword, text="Alphabets uppercase(a-z)", bg="#222930", fg="#E9E9E9", font="verdana 10")
lblAlpha.grid(row=5, column=0, columnspan=2, padx=200, pady=10, sticky=W)

var3 = IntVar()
Checkbutton(codePassword, variable=var3, bg="#222930").grid(row=6, column=1, sticky="news")
lblDigits = Label(codePassword, text="Digits", font="verdana 10", bg="#222930", fg="#E9E9E9")
lblDigits.grid(row=6, column=0, columnspan=2, padx=200, pady=10, sticky=W)

var4 = IntVar()
Checkbutton(codePassword, variable=var4, bg="#222930").grid(row=7, column=1, sticky="news")
lblSpch = Label(codePassword, text="Special Characters", font="verdana 10", bg="#222930", fg="#E9E9E9")
lblSpch.grid(row=7, column=0, columnspan=2, padx=200, pady= 10, sticky=W)

btnGenerate = Button(codePassword, text="GENERATE",font="courier 10", bg="#4EB1BA", fg="#E9E9E9", command=code_popup_confirm)
btnGenerate.grid(row=8, column=1, padx=20, pady=10, sticky=E)

###if confirm, password generated
lblPasswordGenerator = Label(randomPassword, text="PASSWORD GENERATOR", font="fixedsys 17 bold", fg="#E9E9E9", bg="#222930")
lblPasswordGenerator.grid(row=0,columnspan=2, padx=300, pady=20, sticky="news")

lblRandomisedPassword = Label(randomPassword, text="PASSWORD: ", font="system 10", bg="#222930", fg="#E9E9E9")
lblRandomisedPassword.grid(row=1, column=0, columnspan=2, padx=200, pady=0, sticky=W)

entRandomisedPassword = Entry(randomPassword, width=55, state="readonly")
entRandomisedPassword.grid(row=2, column=0,columnspan=2, padx=200, pady=20, sticky=W)

btnAccept = Button(randomPassword, text="ACCEPT", font="courier 10", bg="#4EB1BA", fg="#E9E9E9", 
            command=lambda:raise_frame(notes))
btnAccept.grid(row=3, column=0, padx=100, pady=20)

btnDeny = Button(randomPassword, text="DENY", font="courier 10", bg="#4EB1BA", fg="#E9E9E9", command=code_popupOption)
btnDeny.grid(row=3, column=1, padx=100, pady= 20)


##interface for the user to type in important notes
lbldata = Label(notes, text="IMPORTANT DATA", font="fixedsys 17 bold underline", bg="#222930", fg="#E9E9E9")
lbldata.grid(row=1, column=0, columnspan=2, padx=320, pady=20, sticky="news")

textbox = Text(notes, height=20, width=40)
textbox.grid(row=2, columnspan=2, padx=200, pady=0)

btnNotes = Button(notes, text="PROCEED",font="courier 10", bg="#4EB1BA", fg="#E9E9E9", command= confirmData)
btnNotes.grid(row= 9, column=2, padx=0, pady=0, sticky="news")


#####QR code display
lblcode = Label(display, text="QR CODE / BARCODE", font="fixedsys 17 bold", bg="#222930", fg="#E9E9E9")
lblcode.grid(row=0, column=0, columnspan=2, padx=310, pady=20, sticky="news")

lblCode = Label(display, text="Please scan the QR code / Barcode below:", font="system", bg="#222930", fg="#E9E9E9")
lblCode.grid(row=1, column=0, columnspan=2, padx=250, pady=0)

btnCode = Button(display, text="Download the QR Code / Barcode for sharing purposes", font="courier 10", bg="#4EB1BA", fg="#E9E9E9")
btnCode.grid(row=5, column=0, columnspan=2, padx=250, pady=40)


### frame7 manage password
lblManagePassword = Label(password_manager, text="LIST OF SAVED PASSWORDS", font="fixedsys 17 bold underline", bg="#222930", fg="#E9E9E9")
lblManagePassword.grid(row=1, column=0, columnspan=4, padx=300, pady=20, sticky="news")

btnChange = Button(password_manager, text="CHANGE",font="courier 10", bg="#4EB1BA", fg="#E9E9E9", command=popupConfirmChanges)
btnChange.grid(row=3, column=1, padx=0, pady=0, sticky=NE)

lblOption = Label(password_manager, text="/", bg="#222930", fg="#E9E9E9").grid(row=3,column=2, padx=10,pady=0, sticky=NW)

btnRemove = Button(password_manager, text="REMOVE",font="courier 10", fg="#E9E9E9", bg="#4EB1BA", command=popUpconfirmRemove)
btnRemove.grid(row=3, column=2, padx=0, pady=0, sticky=NE)

lblCat = Label(password_manager, text= "CATEGORIES", font= "system", bg="#222930", fg="#E9E9E9")
lblCat.grid(row=2,column=0, padx=100, pady=0, sticky=W)

lblpassword = Label(password_manager, text="PASSWORDS", font="system", bg="#222930", fg="#E9E9E9")
lblpassword.grid(row=2, column=1, padx=100, pady=0, sticky= W)

listboxCat = Listbox(password_manager, height=15, width=15, font="fixedsys 10", fg="black")
listboxCat.grid(row=3, column=0, padx=100, pady=0, sticky=W)

index_cat = 1
for i in ("Facebook", "Instagram", "Twitter", "Snapchat", "LinkedIn","Google+", 
"Youtube", "Pinterest", "Tumblr", "Reddit", "Quora", "Others"):
    listboxCat.insert(index, i)
    index_cat +=1

password = Listbox(password_manager,height= 15, width=15, font="fixedsys 10", fg="black")
password.grid( row=3, column=1, padx=100, pady=0, sticky=W)


def cat_onselect(pwd):q
    w = pwd.widget
    index = (w.curselection()[0])
    password_manager_display(currentuser)
    if index == 0:
        password.delete(0,'end')
        index_password = 1
        for i in facebookpass:
            password.insert(index_password, i)
            index_password +=1
    if index == 1:
        password.delete(0,'end')
        index_password = 1
        for i in instagrampass:
            password.insert(index_password, i)
            index_password +=1
    if index == 2:
        password.delete(0,'end')
        index_password = 1
        for i in twitterpass:
            password.insert(index_password, i)
            index_password +=1
    if index == 3:
        password.delete(0,'end')
        index_password = 1
        for i in snapchatpass:
            password.insert(index_password, i)
            index_password +=1
    if index == 4:
        password.delete(0,'end')
        index_password = 1
        for i in linkedinpass:
            password.insert(index_password, i)
            index_password +=1
    if index == 5:
        password.delete(0,'end')
        index_password = 1
        for i in googlepluspass:
            password.insert(index_password, i)
            index_password +=1
    if index == 6:
        password.delete(0,'end')
        index_password = 1
        for i in youtubepass:
            password.insert(index_password, i)
            index_password +=1
    if index == 7:
        password.delete(0,'end')
        index_password = 1
        for i in pinterestpass:
            password.insert(index_password, i)
            index_password +=1
    if index == 8:
        password.delete(0,'end')
        index_password = 1
        for i in tumblrpass:
            password.insert(index_password, i)
            index_password +=1
    if index == 9:
        password.delete(0,'end')
        index_password = 1
        for i in redditpass:
            password.insert(index_password, i)
            index_password +=1
    if index == 10:
        password.delete(0,'end')
        index_password = 1
        for i in quorapass:
            password.insert(index_password, i)
            index_password +=1
    if index == 11:
        password.delete(0,'end')
        index_password = 1
        for i in otherspass:
            password.insert(index_password, i)
            index_password +=1


listboxCat.bind('<<ListboxSelect>>', cat_onselect)

#select = listboxCat.curselection()
#password_text.set(select)


raise_frame(login)
window.mainloop()
