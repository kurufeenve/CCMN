# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    front_tkiter.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/07 17:29:17 by vordynsk          #+#    #+#              #
#    Updated: 2020/03/10 20:57:22 by vordynsk         ###   ########.fr        #
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
canvas = Canvas(root)
root.title("Map")
root.geometry('1800x1100')
canvas.pack(fill=BOTH, expand=1)

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

floors = {"1st_Floor":image1, "2nd_Floor":image2, "3rd_Floor":image3}

canvas_x = 15
canvas_y = 170

dot_size = 10

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
        try:
            e2 = Label(text=user['ipAddress'][0])
        except:
            e2 = Label(text="N/A")
        e2.place(x=650,y=50)
        try:
            e2 = Label(text=user['floorName'])
        except:
            e2 = Label(text="N/A")
        e2.place(x=850,y=50)
        try:
            e2 = Label(text=user['manufacturer'])
        except:
            e2 = Label(text="N/A")
        e2.place(x=1050,y=50)
        try:
            e2 = Label(text=user['ssId'])
        except:
            e2 = Label(text="N/A")
        e2.place(x=1250,y=50)
        canvas.delete("all")
        try:
            canvas.create_image(canvas_x, canvas_y, anchor=NW, image=floors[user['floorName']])
            x = canvas_x + user['x']
            y = canvas_y + user['y']
            canvas.create_oval(x, y, x + dot_size, y + dot_size, outline="#f11", fill="#1f1", width=2)
        except:
            change_pic1()
        

l1 = Label(text="Input MAC Address:", font='Helvetica 18 bold')
e1 = Entry(width=15)
b1 = Button(text="Search", command=search_MAC)
l2 = Label(text="IP Address:", font='Helvetica 18 bold')
l3 = Label(text="Floor:", font='Helvetica 18 bold')
l4 = Label(text="Manufacturer:", font='Helvetica 18 bold')
l5 = Label(text="SSID:", font='Helvetica 18 bold')

def change_pic1():
    canvas.delete("all")
    canvas.create_image(canvas_x, canvas_y, anchor=NW, image=floors["1st_Floor"])
def change_pic2():
    canvas.delete("all")
    canvas.create_image(canvas_x, canvas_y, anchor=NW, image=floors["2nd_Floor"])
def change_pic3():
    canvas.delete("all")
    canvas.create_image(canvas_x, canvas_y, anchor=NW, image=floors["3rd_Floor"])

canvas.create_image(canvas_x, canvas_y, anchor=NW, image=floors["1st_Floor"])

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
