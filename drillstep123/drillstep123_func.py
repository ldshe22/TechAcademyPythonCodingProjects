
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import time
import shutil
import sqlite3
from os import path


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

# chicken = filename
def onbuttonclickcheckfiles(self):
        for chicken in os.listdir(self.sourceDir):
            dest = self.destDir
            if chicken.endswith(".txt"):
                print(chicken)
                drillstep123 = os.path.join(self.sourceDir, chicken)
                print(drillstep123)
                modificationtime = time.ctime(os.path.getmtime(drillstep123))
                print("Last Modified Time: ", modificationtime)
                conn = sqlite3.connect('drillstep123.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute('CREATE TABLE IF NOT EXISTS tbl_drillstep123(\
                            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                            col_txt TEXT, \
                            col_movedtimestamp TEXT )')
                conn.commit()
                conn.close()

                conn = sqlite3.connect('drillstep123.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute('INSERT INTO tbl_drillstep123(col_txt, col_movedtimestamp) VALUES (?,?)', \
                                (chicken, modificationtime))

                conn.commit()
                conn.close()
                shutil.move(drillstep123, dest)

        """
        # get the path to the file in the current directory
        src = os.listdir("C:\ldshe\OneDrive\Documents\GitHub\TechAcademyPythonCodingProjects\drillstep123")
        dest = "C:\ldshe\OneDrive\Documents\GitHub\TechAcademyPythonCodingProjects\drillstep123\__pycache__"
        for files in src:
            if files.endswith(".txt"):
                shutil.move(files,dest)
        """





        """
        c = conn.cursor()
        c.execute("")
        conn.commit()
        conn.close()
        """




if __name__ == "__main__":
    pass

