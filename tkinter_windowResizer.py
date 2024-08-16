from tkinter import *

def submit1(root,w,h):
    if w.get().isdigit() and h.get().isdigit() and int(w.get()) > 500 and int(h.get())>150:
        root.geometry(f"{w.get()}x{h.get()}")
    w.set("")
    h.set("")


root = Tk()
root.title("Window Resizer GUI --From tkinter_practise")
lable = Label(text="Give input to Resize this window Accordingly--> ", anchor="center", bg="lightblue", font=("Arial", 16, "bold") ,height=2 )
lable.grid(row=0,column=0,columnspan=2)

input_width=StringVar()
input_height=StringVar()

i1 = Label(root, text="Width : ", font=('calibre',11, 'bold'))
i2 = Label(root, text="Height : ", font=('calibre',11, 'bold'))

i1_entry = Entry(root, textvariable = input_width,justify=CENTER)
i2_entry = Entry(root, textvariable = input_height,justify=CENTER)

i1.grid(row=1,column=0)
i1_entry.grid(row=1,column=1)
i2.grid(row=2,column=0)
i2_entry.grid(row=2,column=1)

btn=Button(root,text = 'Submit', command = lambda: submit1(root,input_width,input_height),bg="green",padx=10)
btn.grid(row=3, column=1)

root.mainloop()
