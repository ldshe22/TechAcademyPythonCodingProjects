#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.7.2
#

from tkinter import *
import tkinter as tk

# Be sure to import our other modules 
# so we can have access to them
import drillstep121




def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """
    
    self.btn_add = tk.Button(self.master,width=30,height=4,text='Browse...')
    self.btn_add.grid(row=1,column=0,rowspan=1,columnspan=1, padx=(20,0),pady=(100,00),sticky=N+W)
    self.btn_2add = tk.Button(self.master,width=30,height=4,text='Browse...')
    self.btn_2add.grid(row=2,column=0,rowspan=1,columnspan=1, padx=(20,0),pady=(10,00),sticky=N+W)
    self.btn_ck = tk.Button(self.master,width=30,height=6,text='Check for files...')
    self.btn_ck.grid(row=5,column=0,rowspan=1,columnspan=1, padx=(20,0),pady=(20,00),sticky=N+W)
    self.btn_cls = tk.Button(self.master,width=30,height=6,text='Close Program')
    self.btn_cls.grid(row=5,column=7,rowspan=1,columnspan=1, padx=(400,0),pady=(20,00),sticky=N+W)

   """
I have tried both of these below to make text boxes for drill 121 they are closebut just not right.
I am confused and have been trying to figure this out the past 2 days.
I have tried all different ways and came down to one of these two.
Please help.
  """


   # self.txt_add = tk.Entry(self.master,text='')
   # self.txt_add.grid(row=1,column=2,rowspan=4,columnspan=10,padx=(30,0),pady=(100,0),sticky=N+W)

   # self.lstList1 = Listbox(self.master)
   # self.lstList1.grid(row=1,column=1,rowspan=1,columnspan=12,padx=(30,00),pady=(100,00),sticky=N+E+S+W)



if __name__ == "__main__":
    pass
