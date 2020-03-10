from tkinter import Tk, Canvas, Frame, BOTH

class Dots(Frame):

    def __init__(self, root):
        super().__init__()
        self.canvas = Canvas(root)
        canvas.pack(fill=BOTH, expand=1)

    def place_dot(self):

        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)

        canvas.create_oval(10, 10, 300, 300, outline="#f11", fill="#1f1", width=2)
        canvas.pack(fill=BOTH, expand=1)
