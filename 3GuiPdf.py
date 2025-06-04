from PyPDF2 import PdfReader
from tkinter import *
import random
import datetime
import os

def already_shown_today():
    today = datetime.date.today().isoformat()
    if os.path.exists("last_shown.txt"):
        with open("last_shown.txt", "r") as f:
            last_date = f.read().strip()
        if last_date == today:
            return True
    with open("last_shown.txt", "w") as f:
        f.write(today)
    return False

if already_shown_today():
    exit()  # Exit if already shown today

path=r'F:\2MyProjects\Python\GuiQuote\count.txt'
infile=open(path,'r')
str1=infile.read()
key,value=str1.split('=')
i=int(value)
infile.seek(0)


root=Tk()

root.geometry("1244x534")
# root.minsize("200,200")
reader= PdfReader(r"F:\1MyBooks\SelfHelp\The Daily Stoic_ 366 Meditations on Wisdom, Perseverance, and the Art of Living.pdf")
number_of_pages=len(reader.pages)
# print(number_of_pages)

page=reader.pages[i]
text1=page.extract_text()
# print(type(text))
# print("text1[21:165]")

# assert "potentials" in text

text1=Label(text=text1)
text1.pack()

i+=1
outfile=open(path,'w')
outfile.write("i="+str(i))

close_button = Button(root, text="Close", command=root.destroy)
close_button.pack(pady=10)
root.mainloop()



