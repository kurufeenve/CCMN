from tkinter import *
from PIL import ImageTk, Image

pres = Tk()
pres.title("Presence")
pres.geometry('1450x750')

l1 = Label(text="Total Visitors: ")
l1.configure(font=("Times New Roman", 22, "bold"))
visitors = ["Unique Visitors: ", "Total Visitors: ", "Total Connected: ", "Percentage: "]
visitors_listbox = Listbox(height=4, bg="#87CEFA")
 
for vis in visitors:
    visitors_listbox.insert(END, vis)

l2 = Label(text="Average Dwell Time: ")
l2.configure(font=("Times New Roman", 22, "bold"))
dwelltime = ["5-30 mins: " + " visitors", "30-60 mins: " + " visitors", "1-5 hours: " + " visitors", "5-8 hours: " + " visitors", "8+ hours: " + " visitors"]
dwelltime_listbox = Listbox(height=5, bg="#9370DB")
 
for dw in dwelltime:
    dwelltime_listbox.insert(END, dw)

l3 = Label(text="Peak Hour: ")
l3.configure(font=("Times New Roman", 22, "bold"))
peakhour = ["Visitors in peak hour: ", "Visitors in peak day: "]
peakhour_listbox = Listbox(height=2, bg="#DDA0DD")
 
for ph in peakhour:
    peakhour_listbox.insert(END, ph)

l4 = Label(text="Conversion Rate: ")
l4.configure(font=("Times New Roman", 22, "bold"))
conver = ["Total visitors: ", "Total passerby: "]
conver_listbox = Listbox(height=2, bg="#FFDAB9")
 
for con in conver:
    conver_listbox.insert(END, con)

lstart = Label(text="Start Date")
estart = Entry(width=15)
lend = Label(text="End Date")
eend = Entry(width=15)
change = Button(text="Change")

b1 = Button(text="Repeat Visitors")
b2 = Button(text="Dwell Time")
b3 = Button(text="Proximity")

im1 = Image.open("plot.png")
image1 = ImageTk.PhotoImage(im1)
imagesprite=Label(image=image1)
imagesprite.place(x = 200,y = 350)

im2 = Image.open("diagram.png")
image2 = ImageTk.PhotoImage(im2)
imagesprite2=Label(image=image2)
imagesprite2.place(x = 750,y = 350)

l1.place(x=120, y=50)
visitors_listbox.place(x=120, y=90)
l2.place(x=420, y=50)
dwelltime_listbox.place(x=420, y=90)
l3.place(x=720, y=50)
peakhour_listbox.place(x=720, y=90)
l4.place(x=1020, y=50)
conver_listbox.place(x=1020, y=90)
lstart.place(x=1100, y=240)
estart.place(x=1170, y=240)
lend.place(x=1100, y=270)
eend.place(x=1170, y=270)
change.place(x=1170, y=300)
b1.place(x=420, y=250)
b2.place(x=620, y=250)
b3.place(x=820, y=250)

pres.mainloop()