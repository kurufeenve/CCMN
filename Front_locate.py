# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Front_locate.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 15:06:26 by vordynsk          #+#    #+#              #
#    Updated: 2020/03/11 17:36:37 by vordynsk         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tkinter import *
from PIL import ImageTk, Image
from resizeimage import resizeimage

from Locate import *
from Dots import *

class   Front():

    canvas_x = 15
    canvas_y = 170
    dot_size = 10
    user = {}
    ext = ".jpg"
    floors = {}
   
    def __init__(self):
        self.root = Tk() 
        self.root.title("Map")
        self.root.geometry('1800x1100')
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.L = Locate()
        self.L.get_map_images()
        self.floors["1st_Floor"] = ImageTk.PhotoImage(Image.open("maps/1st_Floor"))
        Image.open("maps/2nd_Floor").resize((1750, 900), Image.ANTIALIAS).save("ANTIALIAS" + self.ext)
        self.floors["2nd_Floor"] = ImageTk.PhotoImage(Image.open("ANTIALIAS" + self.ext))
        self.floors["3rd_Floor"] = ImageTk.PhotoImage(Image.open("maps/3rd_Floor"))
        self.but_pres = Button(text="Presence",command=self.presence_window)
        self.but_pres.place(x=120, y=15, width=80, height=30)
        Label(text="Input MAC Address:", font='Helvetica 18 bold').place(x=450,y=15)
        self.e1 = Entry(width=15)
        self.e1.place(x=450,y=50)
        Button(text="Search", command=self.search_MAC).place(x=450, y=80, width=80, height=30)
        Label(text="IP Address:", font='Helvetica 18 bold').place(x=650,y=15)
        Label(text="Floor:", font='Helvetica 18 bold').place(x=850,y=15)
        Label(text="Manufacturer:", font='Helvetica 18 bold').place(x=1050,y=15)
        Label(text="SSID:", font='Helvetica 18 bold').place(x=1250,y=15)
        Button(text="1st Floor",command=self.show_floor_1).place(x=30, y=50, width=80, height=30)
        Button(text="2nd Floor",command=self.show_floor_2).place(x=120, y=50, width=80, height=30)
        Button(text="3rd Floor",command=self.show_floor_3).place(x=210, y=50, width=80, height=30)

    def presence_window(self):
        pres = Tk()
        pres.title("Presence")
        pres.geometry('1800x1100')
        self.but_pres['state'] = 'disabled'

    def run(self):
        self.show_floor_1()
        self.root.mainloop()

    def search_MAC(self):
        self.L.get_clients()
        resp = self.e1.get()
        if len(resp) == 0:
            print (self.L.old_clients)
            print (self.L.new_clients)
        else:
            user = self.L.search(resp)
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
            self.canvas.delete("all")
            try:
                self.canvas.create_image(self.canvas_x, self.canvas_y, anchor=NW, image=self.floors[user['floorName']])
                x = self.canvas_x + user['x']
                y = self.canvas_y + user['y']
                self.canvas.create_oval(x, y, x + self.dot_size, y + self.dot_size, outline="#f11", fill="#1f1", width=2)
            except:
                show_floor_1()

    def get_clients_on_the_floor(self, floor):
        self.L.get_clients()
        users = {}
        for MAC in self.L.old_clients:
            if (self.L.old_clients[MAC]['floorName'] == floor):
                users[MAC] = self.L.old_clients[MAC]
                print (MAC, self.L.old_clients[MAC])
        for MAC in self.L.new_clients:
            if (self.L.new_clients[MAC]['floorName'] == floor):
                users[MAC] = self.L.new_clients[MAC]
                print (MAC, self.L.new_clients[MAC])
        return users

    def show_clients(self, users):
        for MAC in users:
            x = self.canvas_x + users[MAC]['x']
            y = self.canvas_y + users[MAC]['y']
            self.canvas.create_oval(x, y, x + self.dot_size, y + self.dot_size, outline="#f11", fill="#1f1", width=2)

    def show_floor_1(self):
        self.canvas.delete("all")
        self.canvas.create_image(self.canvas_x, self.canvas_y, anchor=NW, image=self.floors["1st_Floor"])
        self.show_clients(self.get_clients_on_the_floor("1st_Floor"))

    def show_floor_2(self):
        self.canvas.delete("all")
        self.canvas.create_image(self.canvas_x, self.canvas_y, anchor=NW, image=self.floors["2nd_Floor"])
        self.show_clients(self.get_clients_on_the_floor("2nd_Floor"))

    def show_floor_3(self):
        self.canvas.delete("all")
        self.canvas.create_image(self.canvas_x, self.canvas_y, anchor=NW, image=self.floors["3rd_Floor"])
        self.show_clients(self.get_clients_on_the_floor("3rd_Floor"))

if __name__ == '__main__':
    F = Front()
    F.run()
