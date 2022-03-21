#*****************************************************#
#File Name: M3_OoiKherNing_1191100876_MODIFIED.py
#Version/Date:  FINAL (2020-06-02)
#Programmer/ID: Ooi Kher Ning 1191100876
#Project Name: Random Password Generator
#Teammates: Teh Su Anne, Chin Pei Wern, Leong Xin-Nan
#Course/Term: PSP0201 Mini IT Project (2019/20 T3)
#*****************************************************#
import pip_install
import pyqrcode
import barcode
from barcode.writer import ImageWriter
import os

choicelist = ['q', 'b']
confirmlist = ['y', 'n']

#function of checking whether the name of the png file used or not
def duplicatePNG_checker(pngname):
    filename = []
    file_path = os.path.dirname(__file__)
    for root, dirs, files in os.walk (file_path):
        for file in files:
            if file.endswith('.png'):
                filename.append(file)
    if pngname in filename:
        return True
    elif len(pngname.strip())<1:
        return True 
    else:
        return False

#-------------------------------------------- qrcode ------------------------------------------------#
def qrcode(choose_category,qrcode_option2,data,qname):
    if choose_category == 'social media':
        choose_category = "Social Media"
        data = 'Category : ' + choose_category + '\n' + 'Subject : ' + qrcode_option2 + '\n' + 'Notes : ' + data
        q = pyqrcode.create(data)
        q.png('./QRcode/'+qname, scale=7)
     
    elif choose_category == 'entertainment':
        choose_category = "Entertainment"
        data = 'Category : ' + choose_category + '\n' + 'Subject : ' + qrcode_option2 + '\n' + 'Notes : ' + data
        q = pyqrcode.create(data)
        q.png('./QRcode/'+qname, scale=7)
            
    elif choose_category == 'work':
        choose_category = "Work"
        data = 'Category :' + choose_category + '\n' + 'Subject : ' + qrcode_option2 + '\n' + 'Notes : ' + data
        q = pyqrcode.create(data)
        q.png('./QRcode/'+qname, scale=7)
        
    elif choose_category == 'study':
        choose_category = "Study"
        data = 'Category : ' + choose_category + '\n' + 'Subject : ' + qrcode_option2 + '\n' + 'Notes : ' + data
        q = pyqrcode.create(data)
        q.png('./QRcode/'+qname, scale=7)
                    
    else:
        data = 'Category : ' + choose_category + '\n' + 'Subject : ' + str(qrcode_option2) + '\n' + 'Notes : ' + data
        q = pyqrcode.create(data)
        q.png('./QRcode/'+qname, scale=7)
                            
#----------------------------------------------------barcode--------------------------------------------------#
#barcode writer
writer = barcode.get_barcode_class('code128')
writer.default_writer_options['write_text'] = False

def barcode(data,bname):
    data ='Notes : ' + data
    b = writer(data, writer=ImageWriter())
    c = b.save('./BARcode/'+bname)