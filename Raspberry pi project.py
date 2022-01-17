# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:51:16 2021

@author: praty
"""

from tkinter import *
from lyrics_extractor import SongLyrics
  
# user defined funtion
def get_lyrics():
    
    extract_lyrics = SongLyrics(
        "AIzaSyDEx1ngZibiwGDqK-A6WvMd7d7V4sZ5990", "4c189202b3c196058")
      
    temp = extract_lyrics.get_lyrics(str(e.get()))
    res = temp['lyrics']
    result.set(res)
  
  

master = Tk()
master.configure(bg='light grey')
  

result = StringVar()
  

Label(master, text="Enter Song name : ",
      bg="light grey").grid(row=0, sticky=W)
  
Label(master, text="Result :",
      bg="light grey").grid(row=3, sticky=W)
  
  

Label(master, text="", textvariable=result,
      bg="light grey").grid(row=3, column=1, sticky=W)
  
e = Entry(master, width=50)
e.grid(row=0, column=1)
  

b = Button(master, text="Show",
           command=get_lyrics, bg="Blue")
  
b.grid(row=0, column=2, columnspan=2,
       rowspan=2, padx=5, pady=5,)
  
mainloop()