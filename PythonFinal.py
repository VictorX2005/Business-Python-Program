# import modules
from select import select
from tkinter import *
from turtle import width
from webbrowser import BackgroundBrowser
from tkcalendar import *
from userdata import *

# superclass of userInfo
class Person:
    def __init__(self, name):
        self.name = name

# subclass of Person to specify user info
class userInfo(Person):
    def __init__(self, name, number, package, cost, date):
        super().__init__(name)
        self.number = number
        self.package = package
        self.date = ""
        self.cost = ""

# asks the user for their info and validates info
name = input("Input your name: ")
name = verifyName(name)
number = input("\nInput your contact number: ")
number = verifyNumber(number)
package = int(input("\nChoose a package for detailing(1-3):\n1: Basic 1($50 - Wash, Tire Shine)\n2: Silver ($75 - Wash, Tire Shine, Interior Cleaning)\n3: Gold ($100 - Wash, Tire Shine, Interior Cleaning, Wax Coat)\n"))
package = verifyPackage(package)
cost = addBill(package)

# creates a person function with user data
person = userInfo(name, number, package, cost, "")

# create the widget to display the calendar
root = Tk()
root.title("Choose date for detailing")
root.geometry("600x400")

# creates a calendar to choose appointment date
cal = Calendar(root, showweeknumbers=False,firstweekday='sunday',background = "black" , disabledbackground = "black" , borderbackground = "black" , headersbackground = "black" , normalbackground = "black", selectmode="day", cursor = "hand2", year = 2022, month = 7, day = 28)
cal.pack(pady = 30)

# displays the results from the user input
def openResults():
    global date 
    date = cal.selection_get()
    window = Tk()
    window.title("APPOINTMENT DETAILS")
    window.geometry("600x400")
    
    # name labels
    nameLabel = Label(window, text = "Name:", font=("calibre", 20, "bold"))
    nameInput = Label(window, text = name, font = ("calibre", 16, "normal") )

    #number labels
    numberLabel = Label(window, text = "Number:", font=("calibre", 20, "bold"))
    numberInput = Label(window, text = number, font=("calibre", 16, "normal"))

    # package labels
    packageLabel = Label(window, text = "Package:", font=("calibre", 20, "bold"))
    packageInput = Label(window, text = package, font=("calibre", 16, "normal"))

    # cost labels
    costLabel = Label(window, text = "Cost:", font=("calibre", 20, "bold"))
    costInput = Label(window, text = cost, font=("calibre", 16, "normal"))

    # date labels
    dateLabel = Label(window, text = "Date:", font = ("calibre", 20, "bold"))
    dateInput = Label(window, text = date, font=("calibre", 16, "normal"))

    # formats the user info into a grid
    nameLabel.grid(row=0,column=0)
    nameInput.grid(row=0, column=1)
    numberLabel.grid(row=1,column=0)
    numberInput.grid(row=1,column=1)
    packageLabel.grid(row=2,column=0)
    packageInput.grid(row=2,column=1)
    costLabel.grid(row=3,column=0)
    costInput.grid(row=3,column=1)
    dateLabel.grid(row=4,column=0)
    dateInput.grid(row=4,column=1)
    window.mainloop() 

# function that closes the calendar window and displays results
def setDate():
    root.destroy()
    openResults()

# button to take date
selectDay = Button(root, text = "Select Date", command = setDate)
selectDay.pack()
root.mainloop()

# opens text file to write appointment details
f = open("appointmentdetails.txt", "w")

# writes all user info into text file
f.write("Name: " + name)
f.write("\nNumber: " + str(number))
f.write("\nPackage: " + str(package))
f.write("\nCost: " + cost)
f.write("\nDate: "+ str(date))
f.close()

# opens appointment details file to print
f = open("appointmentdetails.txt")
print(f.read())


