from msilib.schema import ListBox
from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        ListBox.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    ListBox.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('TO-DO List')
ws.config(bg='#E0EEEE')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

ListBox = Listbox(frame,width=25,height=8,font=('Bold', 18),bd=0,fg='#464646',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none")
ListBox.pack(side=LEFT, fill=BOTH)



my_entry = Entry(ws,font=('times new roman', 20))

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(button_frame,text='Add Task',font=("Arial",14),bg='#76EE00',padx=20,pady=10,command=newTask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame, text='Delete Task',font=("Arial",14), bg='#DC143C',padx=20,pady=10,command=deleteTask)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()