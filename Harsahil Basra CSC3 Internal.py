#Harsahil Basra CSC Internal
#Sports program or basketball
from tkinter import*
from PIL import ImageTk, Image
import os

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("700x900")
window.title("DRIVE")

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
    global username1
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
    
    
#function for the main login and signup page
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

#making image button
beg_button = Button(page2, image = beginner_button, command=lambda: show_frame(page3))
beg_button.place(x=60, y=20)

advanced_button = PhotoImage(file='adv1.png')

#making image button
adv_button = Button(page2, image=advanced_button, command=lambda:show_frame(page4))
adv_button.place(x=60, y=360)

profile_img = PhotoImage(file='profile.png')

def profbut():
    display_advanced_stats()
    show_frame(page5)
    

#making image button
profile_button = Button(page2, image=profile_img, command=profbut)
profile_button.place(x=500, y=720)



# ========= Page 3 - Beginner =========
page3_button = Button(page3, text="Go Back", command=lambda:show_frame(page2)).place(x=0, y=0)

Label(page3, text="    ").grid(row=0, column=1)
Label(page3, text="    ").grid(row=1, column=1)
Label(page3, text="    ").grid(row=2, column=1)

Label(page3, text = "Total Points ").grid(row=3, column=0)
totalpoints_entry = Entry(page3)
totalpoints_entry.grid(row=3, column=1, padx=5, pady=3)

Label(page3, text = "Total Rebounds ").grid(row=4, column=0)
totalrebounds_entry = Entry(page3)
totalrebounds_entry.grid(row=4, column=1, padx=5, pady=3)

Label(page3, text = "Total Assists ").grid(row=5, column=0)
totalassists_entry = Entry(page3)
totalassists_entry.grid(row=5, column=1, padx=5, pady=3)

Label(page3, text = "Total Steals ").grid(row=6, column=0)
totalsteals_entry = Entry(page3)
totalsteals_entry.grid(row=6, column=1, padx=5, pady=3)

Label(page3, text = "Total Blocks ").grid(row=7, column=0)
totalblocks_entry = Entry(page3)
totalblocks_entry.grid(row=7, column=1, padx=5, pady=3)

Label(page3, text = "Games Played ").grid(row=8, column=0)
gp_entry = Entry(page3)
gp_entry.grid(row=8, column=1, padx=5, pady=3)

#function for calculation and feedback
def calc():
    pts = int(totalpoints_entry.get())
    rbd = int(totalrebounds_entry.get())
    ast = int(totalassists_entry.get())
    stl = int(totalsteals_entry.get())
    blk = int(totalblocks_entry.get())
    gp = int(gp_entry.get())

    fppg = float(pts/gp)
    ppg = round(fppg, 1)
    frpg = float(rbd/gp)
    rpg = round(frpg, 1)
    fapg = float(ast/gp)
    apg = round(fapg, 1)
    fspg = float(stl/gp)
    spg = round(fspg, 1)
    fbpg = float(blk/gp)
    bpg = round(fbpg, 1)

    
    Label(page3, text="     ").grid(row=10, column=1)
    Label(page3, text="     ").grid(row=11, column=1)
    Label(page3, text=f"Points Per Game: {ppg}").grid(row=12, column=1)
    Label(page3, text=f"Rebounds Per Game: {rpg}").grid(row=13, column=1)
    Label(page3, text=f"Assists Per Game: {apg}").grid(row=14, column=1)
    Label(page3, text=f"Steals Per Game: {spg}").grid(row=15, column=1)
    Label(page3, text=f"Blocks Per Game: {bpg}").grid(row=16, column=1)

calcbtn = Button(page3, text= 'Calculate', command=calc).grid(row=9, column=2)
    




# ========= Page 4 - Advanced =========
page4_button = Button(page4, text="Go Back", command=lambda:show_frame(page2)).place(x=0, y=0)

Label(page4, text="    ").grid(row=0, column=1)
Label(page4, text="    ").grid(row=1, column=1)
Label(page4, text="    ").grid(row=2, column=1)

Label(page4, text = "Total Points ").grid(row=3, column=0)
advtotalpoints_entry = Entry(page4)
advtotalpoints_entry.grid(row=3, column=1, padx=5, pady=3)

Label(page4, text = "Total Rebounds ").grid(row=4, column=0)
advtotalrebounds_entry = Entry(page4)
advtotalrebounds_entry.grid(row=4, column=1, padx=5, pady=3)

Label(page4, text = "Total Assists ").grid(row=5, column=0)
advtotalassists_entry = Entry(page4)
advtotalassists_entry.grid(row=5, column=1, padx=5, pady=3)

Label(page4, text = "Total Steals ").grid(row=6, column=0)
advtotalsteals_entry = Entry(page4)
advtotalsteals_entry.grid(row=6, column=1, padx=5, pady=3)

Label(page4, text = "Total Blocks ").grid(row=7, column=0)
advtotalblocks_entry = Entry(page4)
advtotalblocks_entry.grid(row=7, column=1, padx=5, pady=3)

Label(page4, text = "Total Field Goal Made ").grid(row=8, column=0)
advtotalfgm_entry = Entry(page4)
advtotalfgm_entry.grid(row=8, column=1, padx=5, pady=3)

Label(page4, text = "Total Field Goal Attempted ").grid(row=9, column=0)
advtotalfga_entry = Entry(page4)
advtotalfga_entry.grid(row=9, column=1, padx=5, pady=3)

Label(page4, text = "Total Free Throws Attempted ").grid(row=10, column=0)
advtotalfta_entry = Entry(page4)
advtotalfta_entry.grid(row=10, column=1, padx=5, pady=3)

Label(page4, text = "Total 3 Pointers Made ").grid(row=11, column=0)
advtotalpm_entry = Entry(page4)
advtotalpm_entry.grid(row=11, column=1, padx=5, pady=3)

Label(page4, text = "Games Played ").grid(row=12, column=0)
advgp_entry = Entry(page4)
advgp_entry.grid(row=12, column=1, padx=5, pady=3)

Label(page4, text = "Position ").grid(row=13, column=0)
options = ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]
clicked=StringVar()
drop = OptionMenu(page4, clicked, *options).grid(row=13, column=1, padx=5, pady=3)

def advcalc():
    #Getting user input from entry box and making variable
    advpts = int(advtotalpoints_entry.get())
    advrbd = int(advtotalrebounds_entry.get())
    advast = int(advtotalassists_entry.get())
    advstl = int(advtotalsteals_entry.get())
    advblk = int(advtotalblocks_entry.get())
    advgp = int(advgp_entry.get())
    fgm = int(advtotalfgm_entry.get())
    fga = int(advtotalfga_entry.get())
    fta = int(advtotalfta_entry.get())
    tpm = int(advtotalpm_entry.get())
    global position
    position = clicked.get()
    
    global ppg, rpg, apg, spg, bpg, eFG, TS, FTR
    #Calculations + rounding
    fppg = float(advpts/advgp)
    ppg = round(fppg, 2)
    frpg = float(advrbd/advgp)
    rpg = round(frpg, 2)
    fapg = float(advast/advgp)
    apg = round(fapg, 2)
    fspg = float(advstl/advgp)
    spg = round(fspg, 2)
    fbpg = float(advblk/advgp)
    bpg = round(fppg, 2)
    feFG = float(((fgm+(0.5*tpm))/fga)*100)
    eFG = round(feFG, 2)
    TSA = float(2*(fga+(0.475*fta)))
    fTS = float((advpts/TSA)*100)
    TS = round(fTS, 2)
    fFTR = float((fta/fga)*100)
    FTR = round(fFTR, 2)

    Label(page4, text="       ").grid(row=3, column=2)
    Label(page4, text="       ").grid(row=4, column=2)
    Label(page4, text=f"PPG: {ppg}").grid(row=3, column=4)
    Label(page4, text=f"RPG: {rpg}").grid(row=4, column=4)
    Label(page4, text=f"APG: {apg}").grid(row=5, column=4)
    Label(page4, text=f"SPG: {spg}").grid(row=6, column=4)
    Label(page4, text=f"BPG: {bpg}").grid(row=7, column=4)
    
    Label(page4, text=f"eFG%: {eFG}%").grid(row=8, column=4)
    Label(page4, text=f"TS%: {TS}%").grid(row=9, column=4)
    Label(page4, text=f"FTR: {FTR}%").grid(row=10, column=4)

    if position == 'Point Guard' and ppg<10 and apg<10:
        Label(text="As a point guard you must be able to move the ball around and create offense. Your stats show you are not doing so. To improve scoring do scoring drills,"
              "to improve passing get more ball iq", wraplength=600).place(x=50, y=500)

    if position == 'Point Guard' and ppg>10 and apg>10 and spg>1:
        Label(text="")
    

advcalc_btn = Button(page4, text='Calculate', command = advcalc).grid(row=14, column=1)


def save_stats():
    with open(f"{username1}_advanced_stats.txt", "w") as file:
        file.write("PPG:" )
        file.write(str(ppg )+"\n")
        file.write("RPG:" )
        file.write(str(rpg )+"\n")
        file.write("APG:" )
        file.write(str(apg )+"\n")
        file.write("SPG:" )
        file.write(str(spg )+"\n")
        file.write("BPG:" )
        file.write(str(bpg )+"\n")
        file.write("eFG:" )
        file.write(str(eFG )+"\n")
        file.write("TS:" )
        file.write(str(TS )+"\n")
        file.write("FTR:" )
        file.write(str(FTR )+"\n")
        file.close()

save_btn = Button(page4, text="Save", command = save_stats).grid(row=14, column=2)


# ========= Page 5 - Profile =========
page5_button = Button(page5, text="Go Back", command=lambda:show_frame(page2)).place(x=0, y=0)

def display_advanced_stats():
    with open(f"{username1}_advanced_stats.txt", "r") as file:
        advanced_stats = file.read()
    advanced_stats_label.config(text=advanced_stats)

advanced_stats_label = Label(page5, text="", wraplength=600, justify="center")
advanced_stats_label.pack(pady=20)

