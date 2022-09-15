from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import os
from project import attendance as ap
import tkinter.messagebox as tmsg


# click utility for submit button
def click():
    name = str(entryname.get()).capitalize()
    course = str(entrycourse.get())+" "+str(entryyear.get())+" "+"year"
    roll = str(entryroll.get())

    if name in ap:

        total_working_days = ap[name][1]
        total_present_days = ap[name][0]
        attendance_precentage = ap[name][2]

        labelname.delete(0, END)
        labelcourse.delete(0, END)
        labelroll.delete(0, END)
        labelwork.delete(0, END)
        labelpresent.delete(0, END)
        labelpercent.delete(0, END)

        labelname.insert(0, name)
        labelroll.insert(0, roll)
        labelcourse.insert(0, course)
        labelwork.insert(0, total_working_days)
        labelpresent.insert(0, total_present_days)
        labelpercent.insert(0, attendance_precentage)

    elif name != "":
      labelname.delete(0, END)
      labelcourse.delete(0, END)
      labelroll.delete(0, END)
      labelwork.delete(0, END)
      labelpresent.delete(0, END)
      labelpercent.delete(0, END)

      labelname.insert(0, "Entry Not found")
      labelroll.insert(0, "**********")
      labelcourse.insert(0, "**********")
      labelwork.insert(0, "**********")
      labelpresent.insert(0, "**********")
      labelpercent.insert(0, "**********")


# erase utility for erase button
def erase():
    entryname.delete(0, END)
    entrycourse.delete(0, END)
    entryroll.delete(0, END)
    entryyear.delete(0, END)

    labelname.delete(0, END)
    labelcourse.delete(0, END)
    labelroll.delete(0, END)
    labelwork.delete(0, END)
    labelpresent.delete(0, END)
    labelpercent.delete(0, END)


# function to generate report
def report():
    
    # we can also mention the directory in which we want to store our file
    # os.chdir(r'C:\Users\Naman Shah\Desktop')
    dict = ap
    df_report = pd.DataFrame(dict)
    nw = df_report.T
    nw.to_csv("Report.csv")
    tmsg.showinfo("done","downloaded successfully")


# main function()
root = Tk()

root.geometry("600x400")
root.title("Tkinter python project")

# HEADING PART
# 1.creating the heading bar for our gui
heading = Frame(root, bg="grey", relief="sunken", border=2)
heading.pack(side="top", fill="x")


# 1.1 putting label in frame(heading)
sidelabel = Label(heading, text="Attendance record",
                  font="Elianto 25 bold", border=12, padx=50, bg="darkgrey", fg="white")
sidelabel.pack(side="left")

# INPUT DETAILS PART

# 2.1 configuing column and dividing in the ratio of 1 : 3
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# 2.2 creating Frame to for user input name

# ==========================================================================================================

nameframe = Frame(root, bg="turquoise", border=5,
                  relief="sunken", width=50, padx=20, pady=50)
nameframe.pack(side="left", anchor="sw", fill="y")

nameframe.columnconfigure(0, weight=1)
nameframe.columnconfigure(1, weight=3)

# 2.3 create label for name
name = Label(nameframe, text="Student Name", font="sans 15 bold",
             border=3, bg="turquoise", fg="black")
name.grid(column=0, row=0, sticky=W, padx=14, pady=35)

# take user input using entry option
entryname = Entry(nameframe, border=3, relief="sunken",
                  width=30, font="Tahoma 15", fg="red")
entryname.grid(column=1, row=0, sticky=E, padx=14, pady=35)


#2.4 create label for Roll No
rollname = Label(nameframe, text=" Student Roll no",
                 font="sans 14 bold", border=3, bg="turquoise", fg="black")
rollname.grid(column=0, row=1, sticky=W, padx=14, pady=35)

# take user input for Roll No
entryroll = Entry(nameframe, border=3, relief="sunken",
                  width=30, font="Tahoma 15", fg="green")
entryroll.grid(column=1, row=1, sticky=E, padx=14, pady=35)

#2.5 create label for Course Name
course = Label(nameframe, text=" Course Name",
               font="sans 15 bold", border=3, bg="turquoise", fg="black")
course.grid(column=0, row=2, sticky=W, padx=14, pady=35)

# take user input for course Name
entrycourse = Entry(nameframe, border=3, relief="sunken",
                    width=30, font="Tahoma 15", fg="green")
entrycourse.grid(column=1, row=2, sticky=E, padx=14, pady=35)

#2.6 create label for year
year = Label(nameframe, text="Current Year", font="sans 15 bold",
             border=3, bg="turquoise", fg="black")
year.grid(column=0, row=3, sticky=W, padx=14, pady=35)

# take user input for year
entryyear = Entry(nameframe, border=3, relief="sunken",
                  width=30, font="Tahoma 15", fg="green")
entryyear.grid(column=1, row=3, sticky=E, padx=14, pady=35)

#2.7 clear button
clear_button = Button(nameframe, text="Clear", font="serif 12 bold",
                      border=5, relief="raised", width=10, command=erase)
clear_button.grid(column=0, row=6, sticky=W, padx=14, pady=5)

#2.8 login button
login_button = Button(nameframe, text="Submit", font="serif 12 bold",
                      border=5, relief="raised", width=10, command=click)
login_button.grid(column=1, row=6, sticky=E, padx=14, pady=5)

# ===============================================================================================================
# 3 DISPLAY FRAME

# 3.1 creating frame
photoframe = Frame(root, bg="grey", relief="ridge", width=50)
photoframe.pack(side="top", anchor="ne", padx=10, pady=10, fill="x")

# 3.2 inserting image
img = Image.open("pics.png")
photo = ImageTk.PhotoImage(img)
labepng = Label(photoframe, image=photo)
labepng.pack(side="right", anchor="ne")

# 3.3  heading for display columns

subheading = Label(photoframe, text="Student Details", padx=50,
                   pady=50, font="couriernew 30 bold", bg="grey", fg="white",)
subheading.pack(side="left", anchor="nw")


deatilsframe = Frame(root, bg="pink", relief="sunken",
                     border=5, borderwidth=10)
deatilsframe.pack(side="left", anchor="ne", fill="both")

deatilsframe.columnconfigure(0, weight=1)
deatilsframe.columnconfigure(1, weight=4)

#3.3.1 Creating label to display names
namelabel = Label(deatilsframe, text="Name of the student ",
                  font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
namelabel.grid(column=0, row=0, sticky=W, padx=14, pady=20)

labelname = Entry(deatilsframe, border=3, relief="sunken",
                  width=56, font="Tahoma 15", fg="red")
labelname.grid(column=3, row=0, sticky=E, padx=16, pady=10)


# 3.3.2 Creating label to display course
courselabel = Label(deatilsframe, text="Course Undertaken ",
                    font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
courselabel.grid(column=0, row=1, sticky=W, padx=14, pady=20)

labelcourse = Entry(deatilsframe, border=3, relief="sunken",
                    width=56, font="Tahoma 15", fg="red")
labelcourse.grid(column=3, row=1, sticky=E, padx=16, pady=10)

# 3.3.3 Creating label to display roll number
Rolllabel = Label(deatilsframe, text=" Roll Number     ",
                  font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
Rolllabel.grid(column=0, row=2, sticky=W, padx=14, pady=20)

labelroll = Entry(deatilsframe, border=3, relief="sunken",
                  width=56, font="Tahoma 15", fg="red")
labelroll.grid(column=3, row=2, sticky=E, padx=16, pady=10)

# 3.3.4 Creating label to display working days
totworking = Label(deatilsframe, text="Total Working Days",
                   font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
totworking.grid(column=0, row=3, sticky=W, padx=14, pady=20)

labelwork = Entry(deatilsframe, border=3, relief="sunken",
                  width=56, font="Tahoma 15", fg="red")
labelwork.grid(column=3, row=3, sticky=E, padx=16, pady=10)

# 3.3.5 Creating label to display days present
totpresent = Label(deatilsframe, text="Total Days Present",
                   font="Tahoma 15 bold", border=3, padx=10, pady=5, relief="raised")
totpresent.grid(column=0, row=4, sticky=W, padx=14, pady=20)

labelpresent = Entry(deatilsframe, border=3, relief="sunken",
                     width=56, font="Tahoma 15", fg="red")
labelpresent.grid(column=3, row=4, sticky=E, padx=16, pady=10)

# 3.3.6 Creating label for Attendance percentage
totattendance = Label(deatilsframe, text="Attendance Percentage ",
                      font="Tahoma 14 bold", border=3, padx=10, pady=5, relief="raised")
totattendance.grid(column=0, row=5, sticky=W, padx=14, pady=20)

labelpercent = Entry(deatilsframe, border=3, relief="sunken",
                     width=56, font="Tahoma 15", fg="red")
labelpercent.grid(column=3, row=5, sticky=E, padx=16, pady=10)

# =========================================================================================================

# submit button for downloading attendance
final_submit = Button(nameframe, text="Download Report", font="serif 12 bold",
                      border=5, relief="raised", width=18, command=report)
final_submit.grid(column=1, row=6, sticky=W, padx=14, pady=5)

# logout button
logout = Button(heading, text="Logout", font="serif 15 bold", pady=6, border=5,
                width=10, relief="raised", command=exit)
logout.pack(side="right", anchor="ne", pady=8)


# program ends here

root.mainloop()
