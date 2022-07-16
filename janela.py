import tkinter

def monitor():
    xwindow = tkinter.Tk()
    text_box = tkinter.Text(xwindow)
    text_box.pack()

    def verify():
        text_box.delete('1.0',tkinter.END)
        recover = open('log.txt','r')
        text_box.insert('1.0', recover.read())
        text_box.see('end')
        recover.close()
        xwindow.after(200,verify)

    verify()
    xwindow.mainloop()

monitor()
