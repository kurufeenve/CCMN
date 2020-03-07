# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    front_tkiter.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/07 17:29:17 by vordynsk          #+#    #+#              #
#    Updated: 2020/03/07 18:49:12 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage

from Locate import *

root = Tk()

root.title("Map")
root.geometry('1800x1100')

def presence_window():
    pres = Tk()
    pres.title("Presence")
    pres.geometry('1800x1100')
    but_pres['state'] = 'disabled'


but_pres = Button(text="Presence",command=presence_window)

def search_MAC():
    L = Locate()
    L.get_clients()
    print (L.new_clients)
    print (e1)

l1 = Label(text="Input MAC Address:")
e1 = Entry(width=15)
b1 = Button(text="Search", command=search_MAC)
l2 = Label(text="IP Address:")
e2 = Entry(width=15)
l3 = Label(text="Floor:")
e3 = Entry(width=15)
l4 = Label(text="Manufacturer:")
e4 = Entry(width=15)

def change_pic1():
    imagesprite.configure(image=image1)
def change_pic2():
    imagesprite.configure(image=image2)
def change_pic3():
    imagesprite.configure(image=image3)

ext = ".jpg"

im1 = Image.open("maps/1st_Floor")
image1 = ImageTk.PhotoImage(im1)
tmp = Image.open("maps/2nd_Floor")
tmp2 = tmp.resize((1750, 900), Image.ANTIALIAS)
tmp2.save("ANTIALIAS" + ext)
im2 = Image.open("ANTIALIAS" + ext)
image2 = ImageTk.PhotoImage(im2)
im3 = Image.open("maps/3rd_Floor")
image3 = ImageTk.PhotoImage(im3)
imagesprite=Label(image=image1)
imagesprite.place(x = 30,y = 110, width=1750, height=1000)

but1 = Button(text="1st Floor",command=change_pic1)
but2 = Button(text="2nd Floor",command=change_pic2)
but3 = Button(text="3rd Floor",command=change_pic3)

but_pres.place(x=120, y=15, width=80, height=30)
but1.place(x=30, y=50, width=80, height=30)
but2.place(x=120, y=50, width=80, height=30)
but3.place(x=210, y=50, width=80, height=30)
l1.place(x=450,y=15)
e1.place(x=450,y=50)
b1.place(x=485, y=80, width=80, height=30)
l2.place(x=650,y=15)
e2.place(x=650,y=50)
l3.place(x=850,y=15)
e3.place(x=850,y=50)
l4.place(x=1050,y=15)
e4.place(x=1050,y=50)

#########################################################################


root.mainloop()