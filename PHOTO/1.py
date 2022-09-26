from tkinter import *

win = Tk()

win.geometry("700x600")

# Create title label
title_label = Label(win, text="Enter the File Name")
title_label.pack(anchor='n')

# Create title entry
title_entry = Entry(win, width=35)
title_entry.pack(anchor='nw')

# Create save button and function
def save():
   # Get contents of title entry and text entry
   # Create a file to write these contents in to it
   file_title = title_entry.get()
   file_contents = text_entry.get(0.0, END)
   with open(file_title + ".txt", "w") as file:
      file.write(file_contents)
      print("File successfully created")
      file.close()
   pass
#Create a save button to save the content of the file
save_button = Button(win, text="Save The File", command=save)
save_button.pack()

# Create text entry
text_entry = Text(win, width=40, height=30, border=4, relief=RAISED)
text_entry.pack()

win.mainloop()