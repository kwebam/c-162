from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650,650)
root.maxsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text = "File Name")
label_file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely = 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80)
my_text.place(relx = 0.5, rely = 0.55, anchor = CENTER)

name = ""

def openfile():
    # means defing openfile() funtion
    global name
    # means variable could be used in the funtion or out of the funtion. but it does not mean by this funtion because there could be more than one funtion to. 
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title = " open text file", filetypes = (("text files", "*.txt"), ))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END, formated_name)
    root.title(formated_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    my_text.insert(END, paragraph)
    text_file.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    messagebox.showinfo("Update", "Success")
    
def closeWindow():
    root.destroy()
    

open_file = Button(root, image = open_img,  text = "open file", command = openfile)
open_file.place(relx = 0.03, rely = 0.05, anchor = CENTER)

save_file = Button(root, image = save_img, text = "Save file", command = save)
save_file.place(relx = 0.11, rely = 0.05, anchor = CENTER)

exit_file = Button(root, image = exit_img, text = "exit file", command = closeWindow)
exit_file.place(relx = 0.17, rely = 0.05, anchor = CENTER)