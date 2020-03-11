# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Front_locate.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vordynsk <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 15:06:26 by vordynsk          #+#    #+#              #
#    Updated: 2020/03/11 15:15:35 by vordynsk         ###   ########.fr        #
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
   
    def __init__(self):
        self.root = Tk() 
        self.root.title("Map")
        self.root.geometry('1800x1100')
        self.canvas = Canvas(root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.L = Locate()
        self.L.get_map_images()
