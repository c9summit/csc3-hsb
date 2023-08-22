#Harsahil Basra CSC Internal
#Sports program or basketball
from tkinter import*
from PIL import ImageTk, Image
import os

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

def deleteloginw():
  loginw.destroy()

def deleteunfwindow():
  unfwindow.destroy()

def deletepnfwindow():
  pnfwindow.destroy()

def logins():
    deleteloginw()
    show_frame(page2)
  
#function for telling user etails are correct and access point to go into next page
def login_sucess():
  global loginw
  loginw = Toplevel()
  loginw.title("Login")
  loginw.geometry("150x100")
  Label(loginw, text = "Login Sucessful").pack()
  Button(loginw, text = "Continue", command =logins).pack()

#Function for when user inputs incorrect password
def password_not_found():
  global pnfwindow
  pnfwindow = Toplevel()
  pnfwindow.title("Incorrect Password")
  pnfwindow.geometry("150x100")
  Label(pnfwindow, text = "Password Error").pack()
  Button(pnfwindow, text = "OK", command =deletepnfwindow).pack()

#function for when user inputs incorrect username
def user_not_found():
  global unfwindow
  unfwindow = Toplevel()
  unfwindow.title("Incorrect Username")
  unfwindow.geometry("150x100")
  Label(unfwindow, text = "User Not Found").pack()
  Button(unfwindow, text = "OK", command =deleteunfwindow).pack()




#function for storing the input of users 
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

#function for verifying login with stored signup info
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete (0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
      file1 = open(username1, "r")
      verify = file1.read().splitlines()
      if password1 in verify:
          login_sucess()
      else:
          password_not_found()
    else:
        user_not_found()


#function for signup
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
    
    

def main_login():
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1


    
    #Create username entrybox
    Label(page1, text = "Username").pack()
    username_entry1 = Entry(page1, textvariable = username_verify)
    username_entry1.pack()
    #Create password entrybox
    Label(page1, text = "Password").pack()
    password_entry1 = Entry(page1, textvariable = password_verify)
    password_entry1.pack()
    #login button
    login_btn = Button(page1, text='LOGIN', font=('Arial', 13, 'bold'), command=login_verify)
    login_btn.pack()
    #signup button
    pg1_button = Button(page1, text='SIGNUP', font=('Arial', 13, 'bold'), command=signup)
    pg1_button.pack()

main_login()

# ========= Page 2 - Dashboard =========

pag2_label = Label(page2, text='DRIVE', font=('Arial', 70, 'bold'))
pag2_label.place(x=170, y=750)
pag2_label1 = Label(page2, text='DASHBOARD', font=('Arial', 35, 'bold'))
pag2_label1.place(x=30, y=700)

beginner_button = PhotoImage(file='p0111.png')

beg_button = Button(page2, image = beginner_button, command=lambda: show_frame(page3))
beg_button.place(x=60, y=20)

advanced_button = PhotoImage(file='adv1.png')

adv_button = Button(page2, image=advanced_button, command=lambda:show_frame(page4))
adv_button.place(x=60, y=360)

profile_img = PhotoImage(file='profile.png')

profile_button = Button(page2, image=profile_img, command=lambda:show_frame(page5))
profile_button.place(x=500, y=720)



# ========= Page 3 - Beginner =========

# ========= Page 4 - Advanced =========


# ========= Page 5 - Profile =========
