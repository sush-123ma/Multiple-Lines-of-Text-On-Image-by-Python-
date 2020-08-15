from PIL import Image, ImageDraw, ImageFont
import textwrap
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color,align="left")
        y_text += line_height


def process():
    '''
    Testing draw_multiple_line_text
    '''
    #image_width
    button.configure(bg='blue')
    l=e1.get()
    try:
         image = Image.open(l+".jpg")
         fontsize = 15# starting font size
         font = ImageFont.truetype("arial.ttf", fontsize)
         font2= ImageFont.truetype("arial.ttf", 13)
         text1 = "Life isn’t about FINDING yourself. Life is about CREATING yourself"
         text2 = "– George Bernard Shaw"
         text_color ="white"
         text_color2="white"
         text_start_height =100
         draw_multiple_line_text(image, text1, font, text_color, text_start_height)
         draw_multiple_line_text(image, text2, font2, text_color2,150)
         k=e2.get()
         image.save(k+'.png')
         #Path of image to be in same local directory of python code
    except:
        messagebox.showinfo("Alert","Fill the Fields Correctly")

if __name__ == "__main__":
    master=tk.Tk()
    master.geometry('400x400')
    imgt=tk.Label(master,text="Enter the Image File Name:" ,font=("calibre",10,'italic'))
    saved=tk.Label(master,text="Image to be Saved as" ,font=("calibre",10,'italic'))
    e1=tk.Entry(master,font=("calibre",10,'italic'))
    e2=tk.Entry(master,font=("calibre",10,'italic'))
    imgt.grid(row=2,column=2)
    saved.grid(row=4,column=2)
    e1.grid(row=2,column=7)
    e2.grid(row=4,column=7)
    button=tk.Button(master,text='SAVE',command=process,bg='green',fg='white',borderwidth='4',relief='groove')
    button.grid(row=100,column=5)
    master.mainloop()

