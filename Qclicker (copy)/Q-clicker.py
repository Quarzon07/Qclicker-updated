from tkinter import *
from playsound import playsound



# setting background music

playsound('backgroundmusic.mp3', False)

#setting up window

win = Tk()

win.title("Q-clicker")

win.geometry("240x350")

win.configure(bg = 'blue')


#setting background


img004 = PhotoImage(file="BackGround.png")
label004 = Label(win, image = img004)
label004.place(x=0, y=0)


#displaying balance

label2 = Label(text = "Balance :", bg = 'blue', fg = 'white')
label2.pack()

UC = 0

label1 = Label(text = UC, bg = 'blue', fg = 'white')
label1.pack()




#setting button clicker 

addedC = 1


def clicked():
    global addedC
    global UC
    UC += addedC
    label1.config(text = UC)

photclickB = PhotoImage(file = "Buttonclicker.png")

button1 = Button(win, text = "Click", command = clicked, image = photclickB, bg = 'blue', fg = 'white')
button1.pack()

label02 = Label(win, text = "your click add count is : ", bg = 'blue', fg = 'white')
label3 = Label(win, text = addedC, bg = 'blue', fg = 'white')

label02.pack()
label3.pack()


#set and display add count

addcost = 10
addvalue = 1

def updateclickC():
    global addedC
    global UC
    global addcost
    global addvalue
    
    if UC > addcost - 1:
        addedC = addedC + addvalue
        UC -= addcost
        label1.config(text = UC)
        label3.config(text = addedC)
        label001.config(text = addcost)
        addcost += 10
        addvalue = addvalue + 1


photclick3B = PhotoImage(file = "addtoclick.png")

button2 = Button(win, text = "increase click count", command = updateclickC, image = photclick3B, bg = 'blue', fg = 'white')
label00 = Label(win, text = "cost is : ", bg = 'blue', fg = 'white')
label001 = Label(win, text = addcost, bg = 'blue', fg = 'white')

button2.pack()
label00.pack()
label001.pack()



#setting multiplayng adding count button and displaying it

multiplycost = 10000
multiplyedvalue = 10

def multiplycount():
    global UC
    global addedC
    global multiplycost
    global multiplyedvalue
    
    if UC > multiplycost - 1:
        UC -= multiplycost
        addedC = addedC * multiplyedvalue
        label1.config(text = UC)
        label3.config(text = addedC)
        label03.config(text = multiplycost)
        multiplycost = multiplycost * 5
        multiplyedvalue += 1
        

photclick2B = PhotoImage(file = "Multiplyadd.png")


button3 = Button(win, text = "multiply click count x10", command = multiplycount, image = photclick2B, bg = 'blue', fg = 'white')
label12 = Label(win, text = "cost is : ", bg = 'blue', fg = 'white')
label03 = Label(win, text = multiplycost, bg = 'blue', fg = 'white')

button3.pack()
label12.pack()
label03.pack()

win.mainloop()
