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

for frame in (page0, page1, page1a, page2, page3, page4, page5, page6):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page0)

# ========= Page 0 - Entry Page =========
entry_btn = PhotoImage(file='oppen45.png')
#Create label for button
img_label = Label(image=entry_btn)

btn0 = Button(page0, image=entry_btn, command=lambda: show_frame(page1), borderwidth=0)
btn0.pack(pady=0)

# ========= Page 1 - Login =========

def signup_user():
    username_data = username.get()
    password_data = password.get()

    file=open(username_data, "w")
    file.write(username_data+"\n")
    file.write(password_data)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(signuppage, text = "Registration Sucess", fg = "green").pack()

def signup():
    global signuppage
    signuppage = Toplevel()
    signuppage.title("Sign Up")
    signuppage.geometry("250x200")

    #global username & password so can be used for signup_user function
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(signuppage, text="Enter your details below").pack()
    Label(signuppage, text="").pack()
    
    Label(signuppage, text="Username").pack()
    username_entry = Entry(signuppage, textvariable = username)
    username_entry.pack()

    Label(signuppage, text="Password").pack()
    password_entry = Entry(signuppage, textvariable = password)
    password_entry.pack()
    Button(signuppage, text="Register", command = signup_user).pack()
    
    



#Create username entrybox
Label(page1, text = "Username").pack()
username_entry1 = Entry(page1)
username_entry1.pack()
#Create password entrybox
Label(page1, text = "Password").pack()
password_entry1 = Entry(page1)
password_entry1.pack()
#login button
login_btn = Button(page1, text='LOGIN', font=('Arial', 13, 'bold'), command=lambda:show_frame(page2), borderwidth=0)
login_btn.pack()
#signup button
pg1_button = Button(page1, text='SIGNUP', font=('Arial', 13, 'bold'), command=signup, borderwidth=0)
pg1_button.pack()



# ========= Page 1a - Signup =========

# ========= Page 2 - Dashboard =========

# ========= Page 3 - Beginner =========

# ========= Page 4 - Advanced =========

# ========= Page 5 - Feedback =========

# ========= Page 6 - Profile =========
