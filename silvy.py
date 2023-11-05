# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:35:44 2023

@author: Saleema
"""

#head part-module1-getting name,mail id and phnumber from user and stored in db
import sqlite3
import pandas as pd  
import numpy as np  
print("Please provide your details here")
x= str(input("Please Enter your Name : "))
y=str(input("Enter your mailid "))
z=str(input("Enter your phone number "))
a=np.array([x])
b=np.array([y])
c=np.array([z])
#print("a=",a)
#saranprint("b=",b)
frame={ "Name":a, "Mailid":b,"Phone number":c}
g=pd.DataFrame(frame)
#print(g)
database = "Examp.sqlite"
conn = sqlite3.connect(database)
g.to_sql(name='customer', con=conn,if_exists='append',index=False)
conn.close()

#check validity of mobile number and mail
def is_valid_mobile_number(mobile_number):
    if len(mobile_number) == 10 and mobile_number.isdigit():
        return True
    else:
        return False

def is_valid_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

# Get mobile number and email input from the user
#mobile_number = input("Enter a mobile number: ")
#email = input("Enter an email address: ")

# Validate the mobile number
while not is_valid_mobile_number(z):
    print("Invalid mobile number. Please enter a 10-digit number.")
    mobile_number = input("Enter a mobile number: ")

# Validate the email
while not is_valid_email(y):
    print("Invalid email address. Please enter a valid email.")
    email = input("Enter an email address: ")

#print("Mobile number:", mobile_number)
#print("Email address:", email)


#Body part-using NLP we are creating language translator bot
import time
import nltk
nltk.download('punkt')
#from nltk.tokenize import word_tokenize
from googletrans import Translator
#x= str(input("Please Enter your Name : "))
time_limit = 100 

start_time = time.time()

end_time = start_time + time_limit

print("\n\nHI!!!! {} Myseslf silvy\n Welcome to Language translator BOT\n  " .format(x))
 
while time.time() < end_time:
   
# print("\n\nHI!!!! {} Myseslf silvy\n Welcome to Language translator BOT\n  " .format(x))
 txt= str(input("Please Enter the text to be translated: "))
 print("the text entered :",txt)
 txl= str(input("Please Enter the language in which the text to be translated : "))
 print("The language in which the text to be translated is: ",txl)

 low=txl.lower()
 #print(low)

 if low in  ['spanish','spansh','span','sapaneesh','spaneesh']:
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='es')
    print(trtxt.text)
    
 elif low in ['french','fench']:
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='fr')
    print(trtxt.text)   
    
 elif low in ['german']:
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='de')
    print(trtxt.text)
    
 elif low in ['italian']:
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='it')
    print(trtxt.text)
 elif low in ['portuguese']:
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='pt')
    print(trtxt.text)
 elif low in ['japanese']:
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='ja')
    print(trtxt.text)
 elif low in ['korean']:    
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='ko')
    print(trtxt.text) 
 elif low in ['chinese']:    
    translator = Translator()
    text_to_translate = txt
    trtxt = translator.translate(text_to_translate, src='en', dest='zh')
    print(trtxt.text)
 elif low in ['russian']:    
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='ru')
        print(trtxt.text)
 elif low in ['arabic']:       
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='ar')
        print(trtxt.text)
 elif low in ['hindi']:        
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='hi')
        print(trtxt.text)
 elif low in ['tamil']:       
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='ta')
        print(trtxt.text)
 elif low in ['telugu']:        
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='te')
        print(trtxt.text)
 elif low in ['bengali']:       
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='bn')
        print(trtxt.text)
 elif low in ['urdu']:       
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='ur')
        print(trtxt.text)
 elif low in ['gujarati']:        
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='gu')
        print(trtxt.text)
 elif low in ['marathi']:       
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='mr')
        print(trtxt.text)
 elif low in ['kannada']:       
        translator = Translator()
        text_to_translate = txt
        trtxt = translator.translate(text_to_translate, src='en', dest='kn')
        print(trtxt.text)
 else :
     print("the language is not in the translator list")
     
     
     
 #tail bot      
print("\n\nHi!!!!! i am Silvy, i can translate from english to so many languages,\nsome languages are listed below::\n ")
print("\nSpanish\nFrench\nGerman\nItalian\nPortuguese\nJapanese\nKorean\nChinese\nRussian\nArabic\nHindi\nTamil\nTelugu\nBengali\nUrdu\nGujarati\nMarathi\nKannada\n")
time.sleep(3)
low=txl.lower()
#print(low)

if low in  ['spanish','spansh','span','sapaneesh','spaneesh']:
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='es')
   print(trtxt.text)
   
elif low in ['french','fench','frnch','fnch','frinch']:
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='fr')
   print(trtxt.text)   
   
elif low in ['german','germn',' german','gman','geman']:
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='de')
   print(trtxt.text)
   
elif low in ['italian','italy','italean','etalian','etallean']:
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='it')
   print(trtxt.text)
elif low in ['portuguese','portugeese','portugal']:
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='pt')
   print(trtxt.text)
elif low in ['japanese','japanise','japanis','japaneese','japanlanguage']:
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='ja')
   print(trtxt.text)
elif low in ['korean','korian','corean','corian']:    
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='ko')
   print(trtxt.text) 
elif low in ['chinese','chainese','chinise','china']:    
   translator = Translator()
   text_to_translate = txt
   trtxt = translator.translate(text_to_translate, src='en', dest='zh')
   print(trtxt.text)
elif low in ['russian','russia','rushiya','rassian','russhian']:    
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='ru')
       print(trtxt.text)
elif low in ['arabic','uaelanguage','arabec','arabs']:       
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='ar')
       print(trtxt.text)
elif low in ['hindi','indianorthlang','hende','hendi']:        
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='hi')
       print(trtxt.text)
elif low in ['tamil','thamil','tamilnadu']:       
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='ta')
       print(trtxt.text)
elif low in ['telugu','telungana','thelugu']:        
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='te')
       print(trtxt.text)
elif low in ['bengali','bangali','bhengali']:       
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='bn')
       print(trtxt.text)
elif low in ['urdu','oordu','oordhu']:       
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='ur')
       print(trtxt.text)
elif low in ['gujarati','ghujarati','ghujarathi']:        
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='gu')
       print(trtxt.text)
elif low in ['marathi','marati']:       
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='mr')
       print(trtxt.text)
elif low in ['kannada','kannadam','karnataka']:       
       translator = Translator()
       text_to_translate = txt
       trtxt = translator.translate(text_to_translate, src='en', dest='kn')
       print(trtxt.text)
else :
    print("the language is not in the translator list")     