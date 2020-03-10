# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    front_tkiter.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/07 17:29:17 by vordynsk          #+#    #+#              #
#    Updated: 2020/03/10 18:18:45 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage

from Locate import *
from Dots import * 

root = Tk()
L = Locate()
user = {}
dot = Dots()

root.title("Map")
root.geometry('1800x1100')

def presence_window():
    pres = Tk()
    pres.title("Presence")
    pres.geometry('1800x1100')
    but_pres['state'] = 'disabled'


but_pres = Button(text="Presence",command=presence_window)

def search_MAC():
    L.get_clients()
    resp = e1.get()
    if len(resp) == 0:
        print (L.old_clients)
        print (L.new_clients)
    else:
        user = L.search(resp)
        e2 = Label(text=user['ipAddress'][0])
        e2.place(x=650,y=50)
        e2 = Label(text=user['floorName'])
        e2.place(x=850,y=50)
        e2 = Label(text=user['manufacturer'])
        e2.place(x=1050,y=50)
        e2 = Label(text=user['ssId'])
        e2.place(x=1250,y=50)
        dot.place_dot()

l1 = Label(text="Input MAC Address:", font='Helvetica 18 bold')
e1 = Entry(width=15)
b1 = Button(text="Search", command=search_MAC)
l2 = Label(text="IP Address:", font='Helvetica 18 bold')
l3 = Label(text="Floor:", font='Helvetica 18 bold')
l4 = Label(text="Manufacturer:", font='Helvetica 18 bold')
l5 = Label(text="SSID:", font='Helvetica 18 bold')

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
b1.place(x=450, y=80, width=80, height=30)
l2.place(x=650,y=15)
l3.place(x=850,y=15)
l4.place(x=1050,y=15)
l5.place(x=1250,y=15)

#########################################################################


root.mainloop()
