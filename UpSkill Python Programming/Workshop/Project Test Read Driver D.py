import sys #Start sys
from tkinter import Tk, simpledialog, messagebox #3rd Import TK interface(TK, smipledialog, messagebox), Detail:shorturl.at/axG67

#Create this Function 1st
def read_from_file(): #Function Read
    with open('D:\Coding\Python\learn_Python\UpSkill Python Programming\Workshop\WorldCapital.txt', 'r') as file: #Open File WorldCapital.txt
        for line in file: #read line
            line = line.rstrip('\n') #split line by \n
            country, capital = line.split('/') #split Country&Capital by /
            country = country.capitalize() #Make Text Country capital like a 'JANPAN'
            capital = capital.capitalize() #Make Text Capital capital Like a 'TOKYO'
            world_capital[country] = capital #Create Data type Dictionary{Key=Country,Value=Capital}

#Create this Function 2nd
def write_to_file(country_name,capital_name): #Function write
    with open('D:\Coding\Python\learn_Python\UpSkill Python Programming\Workshop\WorldCapital.txt', 'a') as file: #Open File WorldCapital.txt
        file.write('\n') #new Line
        file.write(country_name + '/' + capital_name) #write Country_name/Capital_name in new line
        file.close # File Close

#4th Main Function
#Create Main Function before import tkinter
root = Tk() #Call variable TK
root.withdraw() #don't show TK window
world_capital = {} #Create Dictionart{} to use Read #line12 in script

#5th Create Loop
while True: #Use while loop because we don't know loop round
    read_from_file() #Use Function Read
    simpledialog.askstring #Use askstring interface, Ask question User like 'What is your name ?'
    query_country = ''
    query_country = simpledialog.askstring('Country', 'Type the name of country:') #Ask User input Country #'Title', 'Description'
    query_country = query_country.capitalize() #Make Answer of User input to Text Country capital like a 'JANPAN'
    if query_country in world_capital: #if condition to check Country form User input already have in Worldcapital.txt
        result = world_capital[query_country]
        messagebox.showinfo('Answer', 'The capital city of ' + query_country + 'is' + result + '!') #'Title', 'Description'
    else: #incase ask User to input Capital city if can't found Capital City in Worldcapital.txt
        new_capital = simpledialog.askstring('Teach me', 'I don\'t know the answer. Please teacg me. What is the capital city of '+ query_country + '?:') #'Title', 'Description'
        messagebox.showinfo('Thank', 'Thank you for teching me. I will definitely know it next time!') #'Title', 'Description'
        new_capital = new_capital.capitalize()
        write_to_file(query_country, new_capital) #Use Function write to write query_country(line 33) and new_capital(line 40)
#6th Create Do you want to play again
    answer = simpledialog.askstring('Countinue', 'Do you want to try again? Yes/No: ') #'Title', 'Description'
    if answer == 'No':
        messagebox.showinfo('Thank', 'Thank you for plating!') #'Title', 'Description'
        root.destroy()
        sys.exit() #End sys