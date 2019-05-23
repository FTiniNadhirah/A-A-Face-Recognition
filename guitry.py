import Tkinter
import tkMessageBox


top = Tkinter.Tk()

def create():
   import datasetCreator
   tkMessageBox.showinfo("A&A Face Recognition", "New data has been entered")
B1 = Tkinter.Button(top, text = "Enter new data", command = create)
B1.pack()


def load():
    import trainner
    tkMessageBox.showinfo("A&A Face Recognition", "The dataset has been successfully loaded into the face database")
B2 = Tkinter.Button(top, text = "Load Dataset", command = load)
B2.pack()

def detect():
   import detector
   tkMessageBox.showinfo("A&A Face Recognition", "Actor or actress is successfully recognized")
B3 = Tkinter.Button(top, text = "Recognize actor or actress", command = detect)
B3.pack()

def exitprogram():
   quit()
   tkMessageBox.showinfo("A&A Face Recognition", "EXIT")
B4 = Tkinter.Button(top, text = "Exit", command = exitprogram)
B4.pack()

   
top.mainloop()


