# Python Ver: 3.7.2
#
from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access to them
import drillstep121_gui


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        
        self.master.minsize(1110,430) #(height,width)
       
        self.master.maxsize(1110,430)
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")
        

        # load in the GUI widgets from a seperate module,
        # keeping your code compartmentalized and clutter free
        drillstep121_gui.load_gui(self)

        # Instantiate the Tkinter menu dropdown object
        # This is the menu that will appear at the top of our window
        
     
        

"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""
        
        




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
