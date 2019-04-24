
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import time

# filename = filedialog.askopenfilename()
# filename = filedialog.asksaveasfilename()
# dirname = filedialog.askdirectory()

import drillstep123
import drillstep123_gui
        


def onbuttonclicksource(self):
        direc = filedialog.askdirectory()
        self.txt_add.insert('0', direc)
        self.sourceDir = direc
        

def onbuttonclickdestination(self):
        direc = filedialog.askdirectory()
        self.txt_add2.insert('1', direc)
        self.destDir = direc


def onbuttonclickcheckfiles(self, modtimesinceepoc=None):
        for file in os.listdir(self.sourceDir):
            if file.endswith(".txt"):
                        print(file)
                        drillstep123 = os.path.join(self.sourceDir, file)
                        print(drillstep123)
                        modificationtime = os.path.getmtime(file)
                        modificationtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modtimesinceepoc))
                        print("Last Modified Time: ", modificationtime)
        









if __name__ == "__main__":
    pass


"""
conn = sqlite3.connect(drillstep123_db.db)
c = conn.cursor()
cur.execute("Create Table if not exists tbl_drillstep123( \ID INTEGER PRIMARY KEY AUTOINCREMENT);")
conn.commit()
conn.close()

"""
