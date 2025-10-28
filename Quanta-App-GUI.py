# coding=windows-1252
import sys
from PIL import Image
import PIL.Image
import time
import customtkinter
from tkinter import *
class ToolTip(object):
    def __init__(self, widget):
        self.bw = None
        self.bg = None
        self.pady = None
        self.padx = None
        self.fg = None
        self.ft = None
        self.text = None
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
    def showtip(self, text, font, textcolor, padx, pady, background_color, borderline_width):
        self.text = text
        self.ft = font
        self.fg = textcolor
        self.padx = padx
        self.pady = pady
        self.bg = background_color
        self.bw = borderline_width
        if self.tipwindow or not self.text: return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 60
        y = y + cy + self.widget.winfo_rooty() + 7
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = customtkinter.CTkLabel(tw, text=self.text, fg_color=self.bg, padx=self.padx, pady=self.pady, font=self.ft,
                                       text_color=self.fg, corner_radius=4, bg_color="#222222")
        label.pack(ipadx=1)
    def hidetip(self, delay):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            time.sleep((delay / 1000))
            tw.destroy()
def CreateToolTip(widget, text, font, fg, padx, pady, bg, bw, delay):
    toolTip = ToolTip(widget)
    def enter(event): toolTip.showtip(text, font, fg, padx, pady, bg, bw)
    def leave(event): toolTip.hidetip(delay)
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

# Variable Declaration Section
count = 2
filelogging = True
blue = "#0000FF"
gray = "#C8C8C8"
black = "#000000"
white = "#FFFFFF"
dark_gray = "#141414"
light_blue = "#B4DDFF"
darker_gray = "#A5A4A5"
button_font = ("Helvetica", 16)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
customtkinter.set_widget_scaling(0.8)

class Proced_REG(customtkinter.CTk):
    def __init__(self, **kwargs):
        # Initial Variable Declartion
        super().__init__(**kwargs)
        self.imgge = None
        self.graph_img = None
        self.graphical_rep = None
        self.genlistA = None
        self.output = None
        self.t_output = None
        self.dev_explorer = None
        self.interiorTitle = None
        self.interiorText = None
        self.open_explorer = None
        self.filelog = None
        self.reload = None
        self.label = None
        self.labelTitle = None
        self.labelText = None
        self.st = 0
        self.state("zoomed")
        self.title("Quanta")

        # Generates the cosmetics for the main framework
        self.sidebar = customtkinter.CTkFrame(self, width=305, height=1200, corner_radius=5)
        self.random = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=200, border_spacing=10, text="Automated Generation", font=button_font)
        self.basic = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=200, border_spacing=10, text="Basic Generation", font=button_font)
        self.extended = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=200, border_spacing=10, text="Extended Generation", font=button_font)
        self.about = customtkinter.CTkButton(self.sidebar, corner_radius=6, height=50, width=160, border_spacing=10, text="About Us", font=button_font)

        # Reference for the variables for placement of cosmetic items
        self.sidebar.place(x=0, y=120)
        self.random.place(x=53, y=35)
        self.basic.place(x=53, y=110)
        self.extended.place(x=53, y=185)
        self.about.place(x=73, y=260)

        # Main Frame / Title Creation
        self.mainFrame = customtkinter.CTkFrame(self, width=2075, height=1200, corner_radius=5, fg_color="#242424")
        self.mainTitle = customtkinter.CTkFrame(self, width=2075, height=120, corner_radius=5, fg_color="#242424")
        self.line = customtkinter.CTkFrame(self, width=2500, height=3, fg_color="#404040")

        # Main Frame / Title Placement
        self.mainFrame.place(x=305, y=120)
        self.mainTitle.place(x=0, y=0)
        self.line.place(x=0, y=120)

        # Adds the different buttons and itonc (mostly the home button)
        self.home_image = customtkinter.CTkImage(PIL.Image.open(open("Rocket Engine Generator/Assets/reload.png", "rb")))
        self.home_button = customtkinter.CTkButton(self, corner_radius=2, height=20, border_spacing=0, text="", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.home_image)

        # Makes sure the app closes like it is supposed to
        self.make_topmost()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.update()
    def on_exit(self):
        # Exit protocol for app
        self.destroy()
        sys.exit(1)
    def center(self):
        # Centering the tkinter window
        self.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))
    def txt_gen(self, array):
        y_coor = 0
        self.labelTitle = customtkinter.CTkLabel(self.interiorTitle, text=str(f"""  {array[0]}"""), font=("Segoe UI", 32))
        self.labelTitle.place(x=14, y=10)
        for i in range(1, len(self.output)):
            self.labelText = customtkinter.CTkLabel(self.interiorText, text=str(f"   {array[i]}\n"), font=("Segoe UI", 20))
            self.labelText.place(x=15, y=y_coor + 30)
            y_coor = y_coor + 30
    def make_topmost(self):
        # No idea anymore lol
        self.lift()
        self.attributes("-topmost", 1)
        self.attributes("-topmost", 0)
    def basic(self):
        # Destroying any widgets already displayed
        for widgets in self.mainFrame.winfo_children(): widgets.destroy()
        for widgets in self.mainTitle.winfo_children(): widgets.destroy()

        # Display main window title
        self.label = customtkinter.CTkLabel(self.mainTitle, text="Basic Generation", font=("Sans-Serif", 65, "bold"))
        self.label.grid(padx=20, pady=(20, 100)); self.label.place(x=325, y=98, anchor="s")

    def adv(self):
        # Destroying any widgets already displayed
        for widgets in self.mainFrame.winfo_children(): widgets.destroy()
        for widgets in self.mainTitle.winfo_children(): widgets.destroy()

        # Display main window title
        self.label = customtkinter.CTkLabel(self.mainTitle, text="Extended Generation", font=("Sans-Serif", 65, "bold"))
        self.label.grid(padx=20, pady=(20, 100)); self.label.place(x=385, y=98, anchor="s")

    def about(self):
        # Destroying any widgets already displayed
        for widgets in self.mainFrame.winfo_children(): widgets.destroy()
        for widgets in self.mainTitle.winfo_children(): widgets.destroy()

        # Display main window title
        self.label = customtkinter.CTkLabel(self.mainTitle, text="About Us", font=("Sans-Serif", 65, "bold"))
        self.label.grid(padx=20, pady=(20, 100)); self.label.place(x=205, y=98, anchor="s")

if __name__ == "__main__":
    # Ensures that the superclass "Proced_REG" is only executed when the script is run directly
    app = Proced_REG()
    app.mainloop()
