import Tkinter
import tkMessageBox


top = Tkinter.Tk()


def detect():
   import detector
   tkMessageBox.showinfo("A&A Face Recognition", "Actor or actress is successfully recognized")
B1 = Tkinter.Button(top, text = "Recognize actor or actress", command = detect)
B1.pack()

def exitprogram():
   quit()
   tkMessageBox.showinfo("A&A Face Recognition", "EXIT")
B4 = Tkinter.Button(top, text = "Exit", command = exitprogram)
B4.pack()

   
top.mainloop()


