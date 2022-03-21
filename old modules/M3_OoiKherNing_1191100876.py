#*****************************************************#
#File Name: M3_OoiKherNing_1191100876.py
#Version/Date:  v3 (2020-05-13)
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


def duplicatePNG_checker(pngname):
    filename = []
    file_path = os.path.dirname(__file__)
    for root, dirs, files in os.walk (file_path):
        for file in files:
            if file.endswith('.png'):
                file = file.rstrip('.png')
                filename.append(file)
    if pngname in filename:
        return True
    elif '' in pngname:
        print('True')
        return True 
    else:
        return False


#-------------------------------------------- qrcode ------------------------------------------------#
def qrcode(choose_category,qrcode_option2,data,qname):
    # if userC == 'q':
    #     print (categorylist)
        # choose_category = input('Choose category: ').lower()
        # while choose_category not in categorylist:
        #     print ('Invalid!')
        #     choose_category = input('Choose category: ').lower()
        
        # confirmChoice = input('Do you confirm with your choice: ').lower()
        # while confirmChoice not in confirmlist:
        #     print ('Invalid!')
        #     confirmChoice = input('Do you confirm with your choice: ').lower() 

        # while confirmChoice == 'n':
        #     choose_category = input('Choose category: ').lower()
        #     while choose_category not in categorylist:
        #         print ('Invalid!')
        #         choose_category = input('Choose category: ').lower()
        #     confirmChoice = input('Do you confirm with your choice: ').lower() 
        #     while confirmChoice not in confirmlist:
        #         print ('Invalid!')
        #         confirmChoice = input('Do you confirm with your choice: ').lower() 

        #     if confirmChoice == 'y':
        #         continue

        if choose_category == 'social media':
            # smList = ['Facebook', 'Instagram', 'WeChat', 'Line', 'Snapchat', 'Google', 'Telegram', 'LinkedIn']
            # print (smList)
            # chooseSM = input('Choose social media : ')
            # while chooseSM not in smList:
            #     print ('Invalid!')
            #     chooseSM = input('Choose social media : ')
            
            # confirmChoice = input('Do you confirm with your choice: ').lower()
            # while confirmChoice not in confirmlist:
            #     print ('Invalid!')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
            
            # while confirmChoice == 'n':
            #     chooseSM = input('Choose social media: ')
            #     while chooseSM not in smList:
            #         print ('Invalid!')
            #         chooseSM = input('Choose social media: ')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
            #     while confirmChoice not in confirmlist:
            #         print ('Invalid!')
            #         confirmChoice = input('Do you confirm with your choice: ').lower()
                     
            # if confirmChoice == 'y':
            #     data = input('Enter data: ')
            #     dataC = input('Do you confirm with your input?: ').lower()  
            #     while dataC not in confirmlist:
            #         print ('Invalid')
            #         dataC = input('Do you confirm with your input?: ').lower()  
        
                # while dataC == 'n':
                #     data = input('Enter data: ')
                #     dataC = input('Do you confirm with your input?: ').lower()
                #     while dataC not in confirmlist: 
                #         print ('Invalid')
                #         dataC = input('Do you confirm with your input?: ').lower()  
                # if dataC == 'y':
            # filename = []
            # file_path = os.path.dirname(__file__)
            # for root, dirs, files in os.walk (file_path):
            #     for file in files:
            #         if file.endswith('.png'):
            #             print(file)
            #             file = file.rstrip('.png')
            #             print(file)
            #             filename.append(file)
                            
            # nameC = 'n'
            # while nameC == 'n':
                # qname = input('Enter qr code name: ')
            # while qname in filename:
            #     print('Already exists!')

                    # qname = input('Enter qr code name: ')

                # nameC = input('Do you confirm with the name?: ').lower()
                # while nameC not in confirmlist:
                #     print ('Invalid')
                #     nameC = input('Do you confirm with the name?: ').lower()
                    
                # if nameC == 'y':
            data = 'Category :' + choose_category + '\n' + 'Subject:' + qrcode_option2 + '\n' + 'Notes:' + data
            q = pyqrcode.create(data)
            q.png('./QRcode/'+qname+'.png', scale=7)
            #print ('QR code generated..')
     
        elif choose_category == 'entertainment':
            # entList = ['Netflix', 'iFlix', 'YouTube', 'iQiyi', 'TikTok']
            # print (entList)
            # chooseEnt = input('Choose entertainment : ')
            # while chooseEnt not in entList:
            #     print ('Invalid!')
            #     chooseEnt = input('Choose entertainment : ')
                
            # confirmChoice = input('Do you confirm with your choice: ').lower()
            # while confirmChoice not in confirmlist:
            #     print ('Invalid!')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
             
            # while confirmChoice == 'n':
            #     chooseEnt = input('Choose entertainment: ')
            #     while chooseEnt not in entList:
            #         print ('Invalid!')
            #         chooseEnt = input('Choose entertainment: ')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
            #     while confirmChoice not in confirmlist:
            #         print ('Invalid!')
            #         confirmChoice = input('Do you confirm with your choice: ').lower()
            # if confirmChoice == 'y':
            #     data = input('Enter data: ')
            #     dataC = input('Do you confirm with your input?: ').lower()  
            #     while dataC not in confirmlist:
            #         print ('Invalid')
            #         dataC = input('Do you confirm with your input?: ').lower()  
        
            #     while dataC == 'n':
            #         data = input('Enter data: ')
            #         dataC = input('Do you confirm with your input?: ').lower()
            #         while dataC not in confirmlist: 
            #             print ('Invalid')
            #             dataC = input('Do you confirm with your input?: ').lower()  
            #     if dataC == 'y':
                                    
                    # nameC = 'n'
                    # while nameC == 'n':
                    #     qname = input('Enter qr code name: ')
                    # while qname in filename:
                    #     print('Already exists!')
                    #         qname = input('Enter qr code name: ')

                # nameC = input('Do you confirm with the name?: '),lower()
                # while nameC not in confirmlist:
                #     print ('Invalid')
                #     nameC = input('Do you confirm with the name?: ').lower()
                    
                # if nameC == 'y':
            data = 'Category :' + choose_category + '\n' + 'Subject:' + qrcode_option2 + '\n' + 'Notes:' + data
            q = pyqrcode.create(data)
            q.png('./QRcode/'+qname+'.png', scale=7)
            #print ('QR code generated..')

            
        elif choose_category == 'work':
            # workList = ['Bank', 'Office', 'Email', 'Contact']
            # print (workList)
            # chooseWork = input('Choose work : ')
            # while chooseWork not in workList:
            #     print ('Invalid!')
            #     chooseWork = input('Choose work : ')
                
            # confirmChoice = input('Do you confirm with your choice: ').lower()
            # while confirmChoice not in confirmlist:
            #     print ('Invalid!')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
             
            # while confirmChoice == 'n':
            #     chooseWork = input('Choose work: ')
            #     while chooseWork not in workList:
            #         print ('Invalid!')
            #         chooseWork = input('Choose work: ')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
            #     while confirmChoice not in confirmlist:
            #         print ('Invalid!')
            #         confirmChoice = input('Do you confirm with your choice: ').lower()
            # if confirmChoice == 'y':
            #     data = input('Enter data: ')
            #     dataC = input('Do you confirm with your input?: ').lower()  
            #     while dataC not in confirmlist:
            #         print ('Invalid')
            #         dataC = input('Do you confirm with your input?: ').lower()  
        
            #     while dataC == 'n':
            #         data = input('Enter data: ')
            #         dataC = input('Do you confirm with your input?: ').lower()
            #         while dataC not in confirmlist: 
            #             print ('Invalid')
            #             dataC = input('Do you confirm with your input?: ').lower()  
            #     if dataC == 'y':
            #         filename = []
            #         file_path = os.path.dirname(os.path.abspath(__file__))
            #         for root, dirs, files in os.walk (file_path):
            #             for file in files:
            #                 if file.endswith('.png'):
            #                     file = file.rstrip('.png')
            #                     filename.append(file)
                                    
                    # nameC = 'n'
                    # while nameC == 'n':
                    #     qname = input('Enter qr code name: ')
                    #     while qname in filename:
                    #         print('Already exists!')
                    #         qname = input('Enter qr code name: ')

                    #     if qname not in filename:
                    #         nameC = input('Do you confirm with the name?: ').lower()
                    #         while nameC not in confirmlist:
                    #             print ('Invalid')
                    #             nameC = input('Do you confirm with the name?: ').lower()
                                
                            # if nameC == 'y':
            data = 'Category :' + choose_category + '\n' + 'Subject:' + qrcode_option2 + '\n' + 'Notes:' + data
            q = pyqrcode.create(data)
            q.png('./QRcode/'+qname+'.png', scale=7)
            #print ('QR code generated..')
        
        elif choose_category == 'study':
            # studyList = ['College', 'Coursera', 'High School', 'Tuition', 'Udemy', 'Duolingo', 'Memrise', 'Mathway']
            # print (studyList)
            # chooseStudy = input('Choose study : ')
            # while chooseStudy not in studyList:
            #     print ('Invalid!')
            #     chooseStudy = input('Choose study : ')
                
            # confirmChoice = input('Do you confirm with your choice: ').lower()
            # while confirmChoice not in confirmlist:
            #     print ('Invalid!')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
             
            # while confirmChoice == 'n':
            #     chooseStudy = input('Choose study: ')
            #     while chooseStudy not in studyList:
            #         print ('Invalid!')
            #         chooseStudy = input('Choose study: ')
            #     confirmChoice = input('Do you confirm with your choice: ').lower()
            #     while confirmChoice not in confirmlist:
            #         print ('Invalid!')
            #         confirmChoice = input('Do you confirm with your choice: ').lower()
            # if confirmChoice == 'y':
            #     data = input('Enter data: ')
            #     dataC = input('Do you confirm with your input?: ').lower()  
            #     while dataC not in confirmlist:
            #         print ('Invalid')
            #         dataC = input('Do you confirm with your input?: ').lower()  
        
            #     while dataC == 'n':
            #         data = input('Enter data: ')
            #         dataC = input('Do you confirm with your input?: ').lower()
            #         while dataC not in confirmlist: 
            #             print ('Invalid')
            #             dataC = input('Do you confirm with your input?: ').lower()  
            #     if dataC == 'y':
            #         filename = []
            #         file_path = os.path.dirname(os.path.abspath(__file__))
            #         for root, dirs, files in os.walk (file_path):
            #             for file in files:
            #                 if file.endswith('.png'):
            #                     file = file.rstrip('.png')
            #                     filename.append(file)
                                    
            #         nameC = 'n'
            #         while nameC == 'n':
            #             qname = input('Enter qr code name: ')
            #             while qname in filename:
            #                 print('Already exists!')
            #                 qname = input('Enter qr code name: ')

            #             if qname not in filename:
            #                 nameC = input('Do you confirm with the name?: ').lowr()
            #                 while nameC not in confirmlist:
            #                     print ('Invalid')
            #                     nameC = input('Do you confirm with the name?: ').lower()
                                
            #                 if nameC == 'y':

            data = 'Category :' + choose_category + '\n' + 'Subject:' + qrcode_option2 + '\n' + 'Notes:' + data
            q = pyqrcode.create(data)
            q.png('./QRcode/'+qname+'.png', scale=7)
            #print ('QR code generated..')
                    
        elif choose_category == 'customise':
            # enterCat = input ('Enter your own customise category: ')
            # confirmChoice = input('Do you confirm with the category: ').lower()
            # while confirmChoice not in confirmlist:
            #     print ('Invalid!')
            #     confirmChoice = input('Do you confirm with the category: ').lower()
            
            # while confirmChoice == 'n':
            #     enterCat = input('Enter your own customise category: ')
            #     confirmChoice = input('Do you confirm with the category: ').lower()
            #     while confirmChoice not in confirmlist:
            #         print ('Invalid!')
            #         confirmChoice = input('Do you confirm with the category: ').lower()
            
            # if confirmChoice == 'y':
            #     subject = input('Enter subject: ')
            #     confirmSub = input('Do you confirm with your subject?: ').lower()
            #     while confirmSub not in confirmlist:
            #         print ('Invalid!')
            #         confirmSub = input('Do you confirm with your subject?: ').lower()
                    
            #     while confirmSub == 'n':
            #         subject = input('Enter subject: ')
            #         confirmSub = input('Do you confirm with your subject?: ').lower()
            #         while confirmSub not in confirmlist:
            #             print ('Invalid!')
            #             confirmSub = input('Do you confirm with your subject?: ').lower()
                    
            #     if confirmSub == 'y':
            #         data = input('Enter data: ')
            #         dataC = input('Do you confirm with your input?: ').lower()  
            #         while dataC not in confirmlist:
            #             print ('Invalid')
            #             dataC = input('Do you confirm with your input?: ').lower()  
        
            #         while dataC == 'n':
            #             data = input('Enter data: ')
            #             dataC = input('Do you confirm with your input?: ').lower()
            #             while dataC not in confirmlist: 
            #                 print ('Invalid')
            #                 dataC = input('Do you confirm with your input?: ').lower()  
            #         if dataC == 'y':
            #             filename = []
            #             file_path = os.path.dirname(os.path.abspath(__file__))
            #             for root, dirs, files in os.walk (file_path):
            #                 for file in files:
            #                     if file.endswith('.png'):
            #                         file = file.rstrip('.png')
            #                         filename.append(file)
                                    
            #         nameC = 'n'
            #         while nameC == 'n':
            #             qname = input('Enter qr code name: ')
            #             while qname in filename:
            #                 print('Already exists!')
            #                 qname = input('Enter qr code name: ')

            #             if qname not in filename:
            #                 nameC = input('Do you confirm with the name?: ').lower()
            #                 while nameC not in confirmlist:
            #                     print ('Invalid')
            #                     nameC = input('Do you confirm with the name?: ').lower()
                                
            #                 if nameC == 'y':
            data = 'Category :' + choose_category + '\n' + 'Subject:' + qrcode_option2 + '\n' + 'Notes:' + data
            q = pyqrcode.create(data)
            q.png('./QRcode/'+qname+'.png', scale=7)
            #print ('QR code generated..')
                            
#----------------------------------------------------barcode--------------------------------------------------#
def barcode(choose_category,barcode_option2,data,bname):
    # print (categorylist)
    # choose_category = input('Choose category: ').lower()
    # while choose_category not in categorylist:
    #     print ('Invalid!')
    #     choose_category = input('Choose category: ').lower()
    
    # confirmChoice = input('Do you confirm with your choice: ').lower()
    # while confirmChoice not in confirmlist:
    #     print ('Invalid!')
    #     confirmChoice = input('Do you confirm with your choice: ').lower() 

    # while confirmChoice == 'n':
    #     choose_category = input('Choose category: ').lower()
    #     while choose_category not in categorylist:
    #         print ('Invalid!')
    #         choose_category = input('Choose category: ').lower()
    #     confirmChoice = input('Do you confirm with your choice: ').lower() 
    #     while confirmChoice not in confirmlist:
    #         print ('Invalid!')
    #         confirmChoice = input('Do you confirm with your choice: ').lower() 

    #     if confirmChoice == 'y':
    #         continue

    if choose_category == 'social media':
        # smList = ['Facebook', 'Instagram', 'WeChat', 'Line', 'Snapchat', 'Google', 'Telegram', 'LinkedIn']
        # print (smList)
        # chooseSM = input('Choose social media : ')
        # while chooseSM not in smList:
        #     print ('Invalid!')
        #     chooseSM = input('Choose social media : ')
        
        # confirmChoice = input('Do you confirm with your choice: ').lower()
        # while confirmChoice not in confirmlist:
        #     print ('Invalid!')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
        
        # while confirmChoice == 'n':
        #     chooseSM = input('Choose social media: ')
        #     while chooseSM not in smList:
        #         print ('Invalid!')
        #         chooseSM = input('Choose social media: ')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
        #     while confirmChoice not in confirmlist:
        #         print ('Invalid!')
        #         confirmChoice = input('Do you confirm with your choice: ').lower()
                 
        # if confirmChoice == 'y':
        #     data = input('Enter data: ')
        #     data1 = str(data)
        #     dataC = input('Do you confirm with your input?: ').lower()  
        #     while dataC not in confirmlist:
        #         print ('Invalid')
        #         dataC = input('Do you confirm with your input?: ').lower()  
    
        #     while dataC == 'n':
        #         data = input('Enter data: ')
        #         data1 = str(data)
        #         dataC = input('Do you confirm with your input?: ').lower()
        #         while dataC not in confirmlist: 
        #             print ('Invalid')
        #             dataC = input('Do you confirm with your input?: ').lower()  
        #     if dataC == 'y':
        #         filename = []
        #         file_path = os.path.dirname(os.path.abspath(__file__))
        #         for root, dirs, files in os.walk (file_path):
        #             for file in files:
        #                 if file.endswith('.png'):
        #                     file = file.rstrip('.png')
        #                     filename.append(file)
                                
        #         nameC = 'n'
        #         while nameC == 'n':
        #             bname = input('Enter barcode name: ')
        #             while bname in filename:
        #                 print('Invalid')
        #                 bname = input('Enter barcode name: ')

        #             if bname not in filename:
        #                 nameC = input('Do you confirm with the name?: ')
        #                 while nameC not in confirmlist:
        #                     print ('Invalid')
        #                     nameC = input('Do you confirm with your input?: ').lower()
                            
        #                 if nameC == 'y':
        data = choose_category + '\n' + barcode_option2 + '\n' + data
        a = barcode.get_barcode_class('code128')
        a.default_writer_options['write_text'] = False
        b = a(data, writer=ImageWriter())
        c = b.save('./QRcode/'+bname)
        print ('Barcode generated...')

    elif choose_category == 'entertainment':
        # entList = ['Netflix', 'iFlix', 'YouTube', 'iQiyi', 'TikTok']
        # print (entList)
        # chooseEnt = input('Choose entertainment : ')
        # while chooseEnt not in entList:
        #     print ('Invalid!')
        #     chooseEnt = input('Choose entertainment : ')
            
        # confirmChoice = input('Do you confirm with your choice: ').lower()
        # while confirmChoice not in confirmlist:
        #     print ('Invalid!')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
         
        # while confirmChoice == 'n':
        #     chooseEnt = input('Choose entertainment: ')
        #     while chooseEnt not in entList:
        #         print ('Invalid!')
        #         chooseEnt = input('Choose entertainment: ')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
        #     while confirmChoice not in confirmlist:
        #         print ('Invalid!')
        #         confirmChoice = input('Do you confirm with your choice: ').lower()
        # if confirmChoice == 'y':
        #     data = input('Enter data: ')
        #     data1 = str(data)
        #     dataC = input('Do you confirm with your input?: ').lower()  
        #     while dataC not in confirmlist:
        #         print ('Invalid')
        #         dataC = input('Do you confirm with your input?: ').lower()  
    
        #     while dataC == 'n':
        #         data = input('Enter data: ')
        #         data1 = str(data)
        #         dataC = input('Do you confirm with your input?: ').lower()
        #         while dataC not in confirmlist: 
        #             print ('Invalid')
        #             dataC = input('Do you confirm with your input?: ').lower()  
        #     if dataC == 'y':
        #         filename = []
        #         file_path = os.path.dirname(os.path.abspath(__file__))
        #         for root, dirs, files in os.walk (file_path):
        #             for file in files:
        #                 if file.endswith('.png'):
        #                     file = file.rstrip('.png')
        #                     filename.append(file)
                                
        #         nameC = 'n'
        #         while nameC == 'n':
        #             bname = input('Enter barcode name: ')
        #             while bname in filename:
        #                 print('Already exists!')
        #                 bname = input('Enter barcode name: ')

        #             if bname not in filename:
        #                 nameC = input('Do you confirm with the name?: ')
        #                 while nameC not in confirmlist:
        #                     print ('Invalid')
        #                     nameC = input('Do you confirm with your input?: ').lower()
                            
        #                 if nameC == 'y':
        data = choose_category + '\n' + qrcode_option2 + '\n' + data
        a = barcode.get_barcode_class('code128')
        a.default_writer_options['write_text'] = False
        b = a(data, writer=ImageWriter())
        c = b.save('./QRcode/'+bname)
        print ('Barcode generated...')

    elif choose_category == 'work':
        # workList = ['Bank', 'Office', 'Email', 'Contact']
        # print (workList)
        # chooseWork = input('Choose work : ')
        # while chooseWork not in workList:
        #     print ('Invalid!')
        #     chooseWork = input('Choose work : ')
            
        # confirmChoice = input('Do you confirm with your choice: ').lower()
        # while confirmChoice not in confirmlist:
        #     print ('Invalid!')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
         
        # while confirmChoice == 'n':
        #     chooseWork = input('Choose work: ')
        #     while chooseWork not in workList:
        #         print ('Invalid!')
        #         chooseWork = input('Choose work: ')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
        #     while confirmChoice not in confirmlist:
        #         print ('Invalid!')
        #         confirmChoice = input('Do you confirm with your choice: ').lower()
        # if confirmChoice == 'y':
        #     data = input('Enter data: ')
        #     data1 = str(data)
        #     dataC = input('Do you confirm with your input?: ').lower()  
        #     while dataC not in confirmlist:
        #         print ('Invalid')
        #         dataC = input('Do you confirm with your input?: ').lower()  
    
        #     while dataC == 'n':
        #         data = input('Enter data: ')
        #         data1 = str(data)
        #         dataC = input('Do you confirm with your input?: ').lower()
        #         while dataC not in confirmlist: 
        #             print ('Invalid')
        #             dataC = input('Do you confirm with your input?: ').lower()  
        #     if dataC == 'y':
        #         filename = []
        #         file_path = os.path.dirname(os.path.abspath(__file__))
        #         for root, dirs, files in os.walk (file_path):
        #             for file in files:
        #                 if file.endswith('.png'):
        #                     file = file.rstrip('.png')
        #                     filename.append(file)
                                
        #         nameC = 'n'
        #         while nameC == 'n':
        #             bname = input('Enter barcode name: ')
        #             while bname in filename:
        #                 print('Already exists!')
        #                 bname = input('Enter barcode name: ')

        #             if bname not in filename:
        #                 nameC = input('Do you confirm with the name?: ')
        #                 while nameC not in confirmlist:
        #                     print ('Invalid')
        #                     nameC = input('Do you confirm with your input?: ').lower()
                            
        #                 if nameC == 'y':
        data = choose_category + '\n' + qrcode_option2 + '\n' + data
        a = barcode.get_barcode_class('code128')
        a.default_writer_options['write_text'] = False
        b = a(data, writer=ImageWriter())
        c = b.save('./QRcode/'+bname)
        print ('Barcode generated...')
    
    elif choose_category == 'study':
        # studyList = ['College', 'Coursera', 'High School', 'Tuition', 'Udemy', 'Duolingo', 'Memrise', 'Mathway']
        # print (studyList)
        # chooseStudy = input('Choose study : ')
        # while chooseStudy not in studyList:
        #     print ('Invalid!')
        #     chooseStudy = input('Choose study : ')
            
        # confirmChoice = input('Do you confirm with your choice: ').lower()
        # while confirmChoice not in confirmlist:
        #     print ('Invalid!')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
         
        # while confirmChoice == 'n':
        #     chooseStudy = input('Choose study: ')
        #     while chooseStudy not in studyList:
        #         print ('Invalid!')
        #         chooseStudy = input('Choose study: ')
        #     confirmChoice = input('Do you confirm with your choice: ').lower()
        #     while confirmChoice not in confirmlist:
        #         print ('Invalid!')
        #         confirmChoice = input('Do you confirm with your choice: ').lower()
        # if confirmChoice == 'y':
        #     data = input('Enter data: ')
        #     data1 = str(data)
        #     dataC = input('Do you confirm with your input?: ').lower()  
        #     while dataC not in confirmlist:
        #         print ('Invalid')
        #         dataC = input('Do you confirm with your input?: ').lower()  
    
        #     while dataC == 'n':
        #         data = input('Enter data: ')
        #         data1 = str(data)
        #         dataC = input('Do you confirm with your input?: ').lower()
        #         while dataC not in confirmlist: 
        #             print ('Invalid')
        #             dataC = input('Do you confirm with your input?: ').lower()  
        #     if dataC == 'y':
        #         filename = []
        #         file_path = os.path.dirname(os.path.abspath(__file__))
        #         for root, dirs, files in os.walk (file_path):
        #             for file in files:
        #                 if file.endswith('.png'):
        #                     file = file.rstrip('.png')
        #                     filename.append(file)
                        
        #         nameC = 'n'
        #         while nameC == 'n':
        #             bname = input('Enter barcode name: ')
        #             while bname in filename:
        #                 print('Already exists!')
        #                 bname = input('Enter barcode name: ')

        #             if bname not in filename:
        #                 nameC = input('Do you confirm with the name?: ')
        #                 while nameC not in confirmlist:
        #                     print ('Invalid')
        #                     nameC = input('Do you confirm with your input?: ').lower()
                            
        #                 if nameC == 'y':
        data = choose_category + '\n' + barcode_option2 + '\n' + data
        a = barcode.get_barcode_class('code128')
        a.default_writer_options['write_text'] = False
        b = a(data, writer=ImageWriter())
        c = b.save('./QRcode/'+bname)
        print ('Barcode generated...')
                
    elif choose_category == 'customise':
        # enterCat = input ('Enter your own customise category: ')
        # confirmChoice = input('Do you confirm with the category: ').lower()
        # while confirmChoice not in confirmlist:
        #     print ('Invalid!')
        #     confirmChoice = input('Do you confirm with the category: ').lower()
        
        # while confirmChoice == 'n':
        #     enterCat = input('Enter your own customise category: ')
        #     confirmChoice = input('Do you confirm with the category: ').lower()
        #     while confirmChoice not in confirmlist:
        #         print ('Invalid!')
        #         confirmChoice = input('Do you confirm with the category: ').lower()

        # if confirmChoice == 'y':
        #     subject = input('Enter subject: ')
        #     confirmSub = input('Do you confirm with your subject?: ').lower()
        #     while confirmSub not in confirmlist:
        #         print ('Invalid!')
        #         confirmSub = input('Do you confirm with your subject?: ').lower()
                
        #     while confirmSub == 'n':
        #         subject = input('Enter subject: ')
        #         confirmSub = input('Do you confirm with your subject?: ').lower()
        #         while confirmSub not in confirmlist:
        #             print ('Invalid!')
        #             confirmSub = input('Do you confirm with your subject?: ').lower()
                
        #     if confirmSub == 'y':
        #         data = input('Enter data: ')
        #         data1 = str(data)
        #         dataC = input('Do you confirm with your input?: ').lower()  
        #         while dataC not in confirmlist:
        #             print ('Invalid')
        #             dataC = input('Do you confirm with your input?: ').lower()  
    
        #         while dataC == 'n':
        #             data = input('Enter data: ')
        #             data1 = str(data)
        #             dataC = input('Do you confirm with your input?: ').lower()
        #             while dataC not in confirmlist: 
        #                 print ('Invalid')
        #                 dataC = input('Do you confirm with your input?: ').lower()  
        #         if dataC == 'y':
        #             filename = []
        #             file_path = os.path.dirname(os.path.abspath(__file__))
        #             for root, dirs, files in os.walk (file_path):
        #                 for file in files:
        #                     if file.endswith('.png'):
        #                         file = file.rstrip('.png')
        #                         filename.append(file)
                                
        #         nameC = 'n'
        #         while nameC == 'n':
        #             bname = input('Enter barcode name: ')
        #             while bname in filename:
        #                 print('Already exists!')
        #                 bname = input('Enter barcode name: ')

        #             if bname not in filename:
        #                 nameC = input('Do you confirm with the name?: ')
        #                 while nameC not in confirmlist:
        #                     print ('Invalid')
        #                     nameC = input('Do you confirm with your input?: ').lower()
                            
                        # if nameC == 'y':
        data = enterCat + '\n' + barcode_option2 + '\n' + data
        a = barcode.get_barcode_class('code128')
        a.default_writer_options['write_text'] = False
        b = a(data, writer=ImageWriter())
        c = b.save('./QRcode/'+bname)
        print ('Barcode generated...')