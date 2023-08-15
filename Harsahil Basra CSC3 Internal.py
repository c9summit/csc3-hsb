#Harsahil Basra CSC Internal
#Sports program or basketball
from tkinter import*
from PIL import ImageTk, Image

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("700x900")

#Creating frames
page0 = Frame(window) #Entry Page
page1 = Frame(window) #Login+signup
page1a = Frame(window) #Login
page1b = Frame(window) #Signup
page2 = Frame(window) #Dashboard
page3 = Frame(window) #Beginner
page4 = Frame(window) #Advanced
page5 = Frame(window) #Feedback
page6 = Frame(window) #Profile

for frame in (page0, page1, page1a, page1b, page2, page3, page4, page5, page6):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page0)

# ========= Page 0 =========
entry_btn = PhotoImage(file='oppen45.png')
#Create label for button
img_label = Label(image=entry_btn)

btn0 = Button(page0, image=entry_btn, command=lambda: show_frame(page1), borderwidth=0)
btn0.pack(pady=0)

# ========= Page 1 =========

# ========= Page 1a =========

# ========= Page 1b =========

# ========= Page 2 =========

# ========= Page 3 =========

# ========= Page 4 =========

# ========= Page 5 =========

# ========= Page 6 =========
