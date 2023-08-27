#Harsahil Basra CSC Internal
#Sports program or basketball
from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
import os
from tkinter import messagebox

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.geometry("700x900")
window.title("DRIVE")

#Creating frames
page0 = Frame(window) #Entry Page
page1 = Frame(window) #Login+signup
page2 = Frame(window) #Dashboard
page3 = Frame(window) #Beginner
page4 = Frame(window) #Advanced
page5 = Frame(window) #Profile

for frame in (page0, page1, page2, page3, page4, page5):
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

page1.config(background="#8c9197")

pag1_label = Label(page1, text='drive', font=('Planet Kosmos', 70, 'bold'), bg='#8c9197', fg='darkred')
pag1_label.place(x=170, y=750)
pag1_label1 = Label(page1, text='LOGIN/SIGNUP', font=('Arial', 35, 'bold'), bg='#8c9197', fg='darkred')
pag1_label1.place(x=30, y=720)

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
  loginw.geometry("150x70")
  loginw.configure(background='green')
  Label(loginw, text = "Login Sucessful", bg='green', font=('callibri', 15, 'bold')).pack()
  #Label(loginw, text="", bg='green').pack()
  Button(loginw, text = "Continue", command =logins, width=10, height=2).pack()

#Function for when user inputs incorrect password
def password_not_found():
  global pnfwindow
  pnfwindow = Toplevel()
  pnfwindow.title("Incorrect Password")
  pnfwindow.geometry("150x70")
  pnfwindow.configure(background='red')
  Label(pnfwindow, text = "Password Error", bg='red', font=('callibri', 15, 'bold')).pack()
  Button(pnfwindow, text = "OK", command =deletepnfwindow, width=10, height=2).pack()

#function for when user inputs incorrect username
def user_not_found():
  global unfwindow
  unfwindow = Toplevel()
  unfwindow.title("Incorrect Username")
  unfwindow.geometry("150x70")
  unfwindow.configure(background='red')
  Label(unfwindow, text = "User Not Found", bg='red', font=('callibri', 15, 'bold')).pack()
  #Label(unfwindow, text="", bg='red').pack()
  Button(unfwindow, text = "OK", command =deleteunfwindow, height=2, width=10).pack()




#function for storing the input of users 
def signup_user():
    username_data = username.get()
    password_data = password.get()

    if len(password_data) >= 6:
        if username_data.strip():
            file=open(username_data, "w")
            file.write(username_data+"\n")
            file.write(password_data)
            file.close()

            username_entry.delete(0, END)
            password_entry.delete(0, END)
            Label(signuppage, text = "Registration Sucess", fg = "green", font=('callibri', 15, 'bold'), bg='#8c9197').pack()

        else:
            messagebox.showerror("Error", "Please fill in both fields")
    else:
        messagebox.showerror("Error", "Password must be at least 6 characters")

#function for verifying login with stored signup info
def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete (0, END)

    global list_of_files
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
    signuppage.geometry("250x300")
    signuppage.config(background='#8c9197')

    #global username & password so can be used for signup_user function
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(signuppage, text="Enter your details below", bg='#8c9197').pack()
    Label(signuppage, text="", bg='#8c9197').pack()
    
    Label(signuppage, text="Username", bg='#8c9197').pack()
    username_entry = Entry(signuppage, textvariable = username)
    username_entry.pack()

    Label(signuppage, text="", bg='#8c9197').pack()

    Label(signuppage, text="Password", bg='#8c9197').pack()
    password_entry = Entry(signuppage, textvariable = password)
    password_entry.pack()

    Label(signuppage, text="", bg='#8c9197').pack()
    Button(signuppage, text="Register", command = signup_user, height=2).pack()
    Label(signuppage, text="", bg='#8c9197').pack()
    
    
#function for the main login and signup page
def main_login():
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    canvas_1 = tk.Canvas(page1, width=400, height=250)
    canvas_1.place(x=150, y=250)

    # Create a line on the canvas
    rectangle_1 = canvas_1.create_rectangle(0, 0, 410, 260, fill="darkred")
 
    #Create username entrybox
    Label(page1, text = "Username", bg="darkred").place(x=200, y=300)
    username_entry1 = Entry(page1, textvariable = username_verify)
    username_entry1.place(x=275, y=300)
    #Create password entrybox
    Label(page1, text = "Password", bg="darkred").place(x=200, y=340)
    password_entry1 = Entry(page1, textvariable = password_verify)
    password_entry1.config(show='*')
    password_entry1.place(x=275, y=340)
    #login button
    login_btn = Button(page1, text='LOGIN', font=('Arial', 13, 'bold'), command=login_verify, width=19, height = 2)
    login_btn.place(x=275, y=375)
    #signup button
    pg1_button = Button(page1, text='SIGNUP', font=('Arial', 13, 'bold'), command=signup, width=19, height = 2)
    pg1_button.place(x=275, y=420)

    



main_login()

# ========= Page 2 - Dashboard =========
page2.config(background='#8c9197')

pag2_label = Label(page2, text='drive', font=('Planet Kosmos', 70, 'bold'), bg='#8c9197', fg='darkred')
pag2_label.place(x=170, y=750)
pag2_label1 = Label(page2, text='DASHBOARD', font=('Arial', 35, 'bold'), bg='#8c9197', fg='darkred')
pag2_label1.place(x=30, y=720)

beginner_button = PhotoImage(file='p0111.png')

#making image button
beg_button = Button(page2, image = beginner_button, command=lambda: show_frame(page3))
beg_button.place(x=60, y=20)
beg_lbl = Label(page2, text='Beginner', font=('Arial', 19, 'bold'), bg='#010101', fg='#ffa392').place(x=536, y=260)
advanced_button = PhotoImage(file='adv1.png')

#making image button
adv_button = Button(page2, image=advanced_button, command=lambda:show_frame(page4))
adv_button.place(x=60, y=360)
adv_label=Label(page2, text='Advanced', font=('Arial', 19, 'bold'), bg='#d6d6d6', fg='black').place(x=280, y=650)
profile_img = PhotoImage(file='profileimg.png')

#profile button function
def profbut():
    if (f"{username1}_advanced_stats.txt") in list_of_files:
        display_advanced_stats()
        show_frame(page5)

    else:
        messagebox.showerror("Error", "Profile Page can only be seen once stats saved from advanced page. If you have saved for the first time the profile page will be available on your next visit")
        
    

#making image button
profile_button = Button(page2, image=profile_img, command=profbut, borderwidth=0)
profile_button.place(x=500, y=720)


# ========= Page 3 - Beginner =========
page3.config(background='darkred')

begbg = PhotoImage(file='begbg101.png')
begbg_lbl = Label(page3, image=begbg).place(x=0,y=0)

pag3_label = Label(page3, text='drive', font=('Planet Kosmos', 70, 'bold'), bg='darkred', fg='#8c9197')
pag3_label.place(x=170, y=750)
pag3_label1 = Label(page3, text='BEGINNER', font=('Arial', 35, 'bold'), bg='darkred', fg='#8c9197')
pag3_label1.place(x=30, y=720)


page3_button = Button(page3, text="Go Back", command=lambda:show_frame(page2), height=2, width=10).place(x=0, y=0)

Label(page3, text="    ", bg='darkred').grid(row=0, column=1)
Label(page3, text="    ", bg='darkred').grid(row=1, column=1)
Label(page3, text="    ", bg='darkred').grid(row=2, column=1)

Label(page3, text = "Total Points ", bg='darkred').grid(row=3, column=0)
totalpoints_entry = Entry(page3)
totalpoints_entry.grid(row=3, column=1, padx=5, pady=3)

Label(page3, text = "Total Rebounds ", bg='darkred').grid(row=4, column=0)
totalrebounds_entry = Entry(page3)
totalrebounds_entry.grid(row=4, column=1, padx=5, pady=3)

Label(page3, text = "Total Assists ", bg='darkred').grid(row=5, column=0)
totalassists_entry = Entry(page3)
totalassists_entry.grid(row=5, column=1, padx=5, pady=3)

Label(page3, text = "Total Steals ", bg='darkred').grid(row=6, column=0)
totalsteals_entry = Entry(page3)
totalsteals_entry.grid(row=6, column=1, padx=5, pady=3)

Label(page3, text = "Total Blocks ", bg='darkred').grid(row=7, column=0)
totalblocks_entry = Entry(page3)
totalblocks_entry.grid(row=7, column=1, padx=5, pady=3)

Label(page3, text = "Games Played ", bg='darkred').grid(row=8, column=0)
gp_entry = Entry(page3)
gp_entry.grid(row=8, column=1, padx=5, pady=3)

#function for handling variety of input by user
def robust(entry):
    if entry.isdigit() and 0<=int(entry)<=100000:
        return True
    return False


#function for calculation and feedback
def calc():
    if robust(totalpoints_entry.get()) and robust(totalrebounds_entry.get()) and \
       robust(totalassists_entry.get()) and robust(totalsteals_entry.get()) and \
       robust(totalblocks_entry.get()) and robust(gp_entry.get()):

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

        Label(page3, text=f"Points Per Game: {ppg}", bg='darkred').grid(row=3, column=2)
        Label(page3, text=f"Rebounds Per Game: {rpg}", bg='darkred').grid(row=4, column=2)
        Label(page3, text=f"Assists Per Game: {apg}", bg='darkred').grid(row=5, column=2)
        Label(page3, text=f"Steals Per Game: {spg}", bg='darkred').grid(row=6, column=2)
        Label(page3, text=f"Blocks Per Game: {bpg}", bg='darkred').grid(row=7, column=2)
        Label(page3, text="                                                        ", bg='darkred').grid(row= 17, column=1)

    else:
        Label(page3, text="Invalid input, enter only numbers between 0 and 100000.", bg='darkred', wraplength=200, font=("Arial", 11)).grid(row=17, column=1)

calcbtn = Button(page3, text= 'Calculate', command=calc, height=2, width=10).grid(row=9, column=1)
    




# ========= Page 4 - Advanced =========
page4.config(background='darkred')
page4_button = Button(page4, text="Go Back", command=lambda:show_frame(page2), height=2, width=10).place(x=0, y=0)

pag4_label = Label(page4, text='drive', font=('Planet Kosmos', 70, 'bold'), bg='darkred', fg='#8c9197')
pag4_label.place(x=170, y=750)
pag4_label1 = Label(page4, text='ADVANCED', font=('Arial', 35, 'bold'), bg='darkred', fg='#8c9197')
pag4_label1.place(x=30, y=720)

def pg_feedback(ppg, apg, TS):
    feedback = ""
    
    
    if ppg<10 or apg<7 and TS<40:
        feedback="As a point guard you must be able to move the ball around and create offense. Your stats show you are not doing so. The point guard is the control centre of offense so it is crucial to have good offensive skill. "
    else:
        feedback="Offensively you are playing well but improvement should still be sought for. Continously practicing shooting drills can help improve contested shots and increase your ceiling as a point guard. This helps your team win. "

    return feedback

def sg_feedback(ppg, TS, tpm):
    feedback = ""

    
    if ppg<10 or TS<40 and tpm<3:
        feedback="As a shooting guard you must be able to create offense and score at will which you currently aren't doing. The shooting guard is often one who can score at will which can help your team bounce back from tough situations. "
        
    else:
        feedback="Offensively you are playing well but improvement should still be sought for. Continue to practice shooting and one on one techniques to polish your skills ensuring no defender can stop you during game. "

    return feedback

def sf_feedback(ppg, spg, fta):
    feedback = ""
  
    if ppg<8 or spg<2 and fta<5:
        feedback="As a small forward you need to be able to be a threat offensive which you are currently not doing. You need to practice. Small forwards should be good at both offence and defence and be stable powerhouses within their teams. "   
    else:
        feedback="Offensively you are playing well but improvement should still be sought for. Continue to practice defense through getting game experience and improve offence by training everyday to ensure you are someone your team can rely on. " 
    return feedback


def pf_feedback(ppg, bpg, FTR):
    feedback = ""
    
    if ppg<6 or bpg<2 and FTR<40:
        feedback="As a power foward you should be able to be threat offensively by being able to score and find good passes for your team. You are not doing this. Power forward is similar to small forward beside from size so the roles are similar. "   
    else:
        feedback="Offensively you are playing well but improvement should still be sought for. Continue to do offensive drills during training and improving defence by doing defensive drills and using them in game to get into your muscle memory.  "
    return feedback


def c_feedback(ppg, rpg, bpg):
    feedback = ""
    
    if ppg<5 or rpg<7 and bpg<2:
        feedback+="As a center you should be able to score when opportunity provided and be able to facilitate the ball. You are not doing this. Rebounds are a crucial part of the game and the center is responsible for securing them for his team. "

    else:
        feedback+="Offensively you are playing well but improvement should still be sought for. Continue to practice rebounding and scoring in the paint as well as defending in the paint against other bigs. This will allow for you to prosper and win. "
    return feedback

def display_fb():
    global feedbacktxt
    feedbacktxt=""

    if position == 'Point Guard':
        feedbacktxt = pg_feedback(ppg, apg, TS)

    elif position == 'Shooting Guard':
        feedbacktxt = sg_feedback(ppg, TS, tpm)

    elif position == 'Small Forward':
        feedbacktxt = sf_feedback(ppg,  spg, fta)

    elif position == 'Power Forward':
        feedbacktxt = pf_feedback(ppg, bpg, FTR)

    elif position == 'Center':
        feedbacktxt = c_feedback(ppg, rpg, bpg)
    
    

Label(page4, text="    ", bg='darkred').grid(row=0, column=1)
Label(page4, text="    ", bg='darkred').grid(row=1, column=1)
Label(page4, text="    ", bg='darkred').grid(row=2, column=1)

Label(page4, text = "Total Points ", bg='darkred').grid(row=3, column=0)
advtotalpoints_entry = Entry(page4)
advtotalpoints_entry.grid(row=3, column=1, padx=5, pady=3)

Label(page4, text = "Total Rebounds ", bg='darkred').grid(row=4, column=0)
advtotalrebounds_entry = Entry(page4)
advtotalrebounds_entry.grid(row=4, column=1, padx=5, pady=3)

Label(page4, text = "Total Assists ", bg='darkred').grid(row=5, column=0)
advtotalassists_entry = Entry(page4)
advtotalassists_entry.grid(row=5, column=1, padx=5, pady=3)

Label(page4, text = "Total Steals ", bg='darkred').grid(row=6, column=0)
advtotalsteals_entry = Entry(page4)
advtotalsteals_entry.grid(row=6, column=1, padx=5, pady=3)

Label(page4, text = "Total Blocks ", bg='darkred').grid(row=7, column=0)
advtotalblocks_entry = Entry(page4)
advtotalblocks_entry.grid(row=7, column=1, padx=5, pady=3)

Label(page4, text = "Total Field Goal Made ", bg='darkred').grid(row=8, column=0)
advtotalfgm_entry = Entry(page4)
advtotalfgm_entry.grid(row=8, column=1, padx=5, pady=3)

Label(page4, text = "Total Field Goal Attempted ", bg='darkred').grid(row=9, column=0)
advtotalfga_entry = Entry(page4)
advtotalfga_entry.grid(row=9, column=1, padx=5, pady=3)

Label(page4, text = "Total Free Throws Attempted ", bg='darkred').grid(row=10, column=0)
advtotalfta_entry = Entry(page4)
advtotalfta_entry.grid(row=10, column=1, padx=5, pady=3)

Label(page4, text = "Total 3 Pointers Made ", bg='darkred').grid(row=11, column=0)
advtotalpm_entry = Entry(page4)
advtotalpm_entry.grid(row=11, column=1, padx=5, pady=3)

Label(page4, text = "Games Played ", bg='darkred').grid(row=12, column=0)
advgp_entry = Entry(page4)
advgp_entry.grid(row=12, column=1, padx=5, pady=3)

Label(page4, text = "Position ", bg='darkred').grid(row=13, column=0)
options = ['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center']
global clicked
clicked=tk.StringVar()
drop = tk.OptionMenu(page4, clicked, *options).grid(row=13, column=1, padx=5, pady=3)

def advcalc():
    if robust(advtotalpoints_entry.get()) and robust(advtotalrebounds_entry.get()) and \
       robust(advtotalassists_entry.get()) and robust(advtotalsteals_entry.get()) and \
       robust(advtotalblocks_entry.get()) and robust(advgp_entry.get()) and \
       robust(advtotalfgm_entry.get()) and robust(advtotalfga_entry.get()) and \
       robust(advtotalfta_entry.get()) and robust(advtotalpm_entry.get()):

        #clear existing area
        Label(page4, text="", bg='darkred').grid(row=3, column=4)
        Label(page4, text="", bg='darkred').grid(row=4, column=4)
        Label(page4, text="", bg='darkred').grid(row=5, column=4)
        Label(page4, text="", bg='darkred').grid(row=6, column=4)
        Label(page4, text="", bg='darkred').grid(row=7, column=4)
        Label(page4, text="", bg='darkred').grid(row=8, column=4)
        Label(page4, text="", bg='darkred').grid(row=9, column=4)
        Label(page4, text="", bg='darkred').grid(row=10, column=4)
        Label(page4, text="", bg='darkred').grid(row=17, column=1)
        

        #Getting user input from entry box and making variable
        global advpts, advrbd, advast, advstl, advblk, advgp, fgm, fga, fta, tpm, position
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

        Label(page4, text="       ", bg='darkred').grid(row=3, column=2)
        Label(page4, text="       ", bg='darkred').grid(row=4, column=2)
        Label(page4, text=f"PPG: {ppg}", bg='darkred').grid(row=3, column=4)
        Label(page4, text=f"RPG: {rpg}", bg='darkred').grid(row=4, column=4)
        Label(page4, text=f"APG: {apg}", bg='darkred').grid(row=5, column=4)
        Label(page4, text=f"SPG: {spg}", bg='darkred').grid(row=6, column=4)
        Label(page4, text=f"BPG: {bpg}", bg='darkred').grid(row=7, column=4)
        Label(page4, text=f"eFG%: {eFG}%", bg='darkred').grid(row=8, column=4)
        Label(page4, text=f"TS%: {TS}%", bg='darkred').grid(row=9, column=4)
        Label(page4, text=f"FTR: {FTR}%", bg='darkred').grid(row=10, column=4)

        #Feedback for each specifc response
        if TS<=100 and FTR<=100 and eFG<=100:
            Label(page3, text="                                                                                                                                                                                                                                                                                                                                                                                                                                      ", bg='darkred').grid(row= 17, column=1)
            display_fb()
            feedback_lbl = tk.Label(page4, text="", wraplength=200, bg='darkred')
            feedback_lbl.config(text=feedbacktxt)
            feedback_lbl.grid(row=17, column=1)
            
    
            
        else:
            messagebox.showerror("Error", "To get feedback check your input again, your current stats is not possible in a basketball game")
            
    #If user input is invalid
    else:
        messagebox.showerror("Error", "Invalid input, enter only numbers between 0 and 100 000 and ensure all fields are filled in.")

    

advcalc_btn = Button(page4, text='Calculate', command = advcalc, height=2, width=10).grid(row=14, column=1)

def save_stats():
    if (advtotalpoints_entry.get()).strip() and (advtotalrebounds_entry.get()).strip() and (advtotalassists_entry.get()).strip() and (advtotalsteals_entry.get()).strip() and (advtotalblocks_entry.get()).strip() and (advgp_entry.get()).strip() and (advtotalfgm_entry.get()).strip() and (advtotalfga_entry.get()).strip() and (advtotalfta_entry.get()).strip() and (advtotalpm_entry.get()).strip():

        with open(f"{username1}_advanced_stats.txt", "w") as file:
            file.write("Points Per Game: " )
            file.write(str(ppg )+"\n")
            file.write("\n")
            file.write("Rebounds Per Game: " )
            file.write(str(rpg )+"\n")
            file.write("\n")
            file.write("Assists Per Game: " )
            file.write(str(apg )+"\n")
            file.write("\n")
            file.write("Steals Per Game: " )
            file.write(str(spg )+"\n")
            file.write("\n")
            file.write("Blocks Per Game: " )
            file.write(str(bpg )+"\n")
            file.write("\n")
            file.write("Effective Field Goal Percentage: " )
            file.write(str(eFG )+"%"+"\n")
            file.write("\n")
            file.write("True Shooting Percentage: " )
            file.write(str(TS )+"%"+"\n")
            file.write("\n")
            file.write("Free Throw Rate: " )
            file.write(str(FTR )+"%"+"\n")
            file.write("\n")
            file.close()

        messagebox.showinfo("Success", "Your stats have been saved")

    else:
        messagebox.showerror("Error", "Before saving ensure all fields have been filled in and calculated")




save_btn = Button(page4, text="Save", command = save_stats, height=2, width=10).grid(row=14, column=4)




# ========= Page 5 - Profile =========
page5.config(background='#8c9197')

bg = PhotoImage(file='profile_bg101.png')

labelbgprf = Label(page5, image=bg).place(x=0, y=0)


pag5_label = Label(page5, text='drive', font=('Planet Kosmos', 70, 'bold'), bg='#8c9197', fg='darkred')
pag5_label.place(x=170, y=750)
pag5_label1 = Label(page5, text='PROFILE', font=('Arial', 35, 'bold'), bg='#8c9197', fg='darkred')
pag5_label1.place(x=30, y=720)


page5_button = Button(page5, text="Go Back", command=lambda:show_frame(page2), width=10, height=2).place(x=0, y=0)

def display_advanced_stats():
    with open(f"{username1}_advanced_stats.txt", "r") as file:
        advanced_stats = file.read()
    advanced_stats_label.config(text=advanced_stats, bg='#8c9197', borderwidth=5, anchor="w", justify="left")

advanced_stats_label = Label(page5, text="", wraplength=600, font=("Callibri", 15))
advanced_stats_label.place(x=50, y=250)
