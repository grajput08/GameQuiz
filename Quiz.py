import json
from tkinter import *
from tkinter import messagebox as mb

with open('Easy.json') as f:
    data1 = json.load(f)
with open('Medium.json') as f:
    data2 = json.load(f)
with open('hard.json') as f:
    data3 = json.load(f)
question1 = [v for v in data1[0].values()]
options1 = [v for v in data1[1].values()]
question2 = [v for v in data2[0].values()]
options2 = [v for v in data2[1].values()]
question3 = [v for v in data3[0].values()]
options3 = [v for v in data3[1].values()]
answer1 = [1,2,3,2,3]
answer2 = [1,1,4,2,1]
answer3 = [2,2,2,1,1]

class Easy:

    def __init__(self):
        self.q_no=0
        self.display_question()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question1)
        self.correct=0


    def display_result(self):
        score = self.correct
        if(score == 1):
            mb.showinfo("Result", "Poor")
        elif(score == 2):
            mb.showinfo("Result", "Bad")
        elif(score ==3):
            mb.showinfo("Result", "Good")
        elif(score== 4):
            mb.showinfo("Result", "Strong")
        elif(score==5):
            mb.showinfo("Result", " Very Strong")
        else:
            mb.showinfo("Result", "General Knowlege")




    def check_ans(self, q_no):
        if self.opt_selected.get() == answer1[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no==self.data_size:
            self.display_result()
            top.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(top, text="Next",command=self.next_btn,
                             width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
        quit_button = Button(top, text="Quit", command=top.destroy,
                             width=5,bg="black", fg="white",font=("ariel",16," bold"))
        quit_button.place(x=700,y=50)


    def display_options(self):
        val=0
        self.opt_selected.set(0)
        for option in options1[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
        q_no = Label(top, text=question1[self.q_no], width=60,
                     font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)


    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(top,text=" ",variable=self.opt_selected,
                                    value = len(q_list)+1,font = ("ariel",14))
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
        return q_list

class Medium:

    def __init__(self):
        self.q_no=0
        self.display_question()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question2)
        self.correct=0


    def display_result(self):
        score = self.correct
        if(score == 1):
            mb.showinfo("Result", "Poor")
        elif(score == 2):
            mb.showinfo("Result", "Bad")
        elif(score ==3):
            mb.showinfo("Result", "Good")
        elif(score== 4):
            mb.showinfo("Result", "Strong")
        elif(score==5):
            mb.showinfo("Result", " Very Strong")
        else:
            mb.showinfo("Result", "General Knowlege")




    def check_ans(self, q_no):
        if self.opt_selected.get() == answer2[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no==self.data_size:
            self.display_result()
            top.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(top, text="Next",command=self.next_btn,
                             width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
        quit_button = Button(top, text="Quit", command=top.destroy,
                             width=5,bg="black", fg="white",font=("ariel",16," bold"))
        quit_button.place(x=700,y=50)


    def display_options(self):
        val=0
        self.opt_selected.set(0)
        for option in options2[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
        q_no = Label(top, text=question2[self.q_no], width=60,
                     font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)


    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(top,text=" ",variable=self.opt_selected,
                                    value = len(q_list)+1,font = ("ariel",14))
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
        return q_list


class Hard:

    def __init__(self):
        self.q_no=0
        self.display_question()
        self.opt_selected=IntVar()
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question3)
        self.correct=0


    def display_result(self):
        score = self.correct
        if(score == 1):
            mb.showinfo("Result", "Poor")
        elif(score == 2):
            mb.showinfo("Result", "Bad")
        elif(score ==3):
            mb.showinfo("Result", "Good")
        elif(score== 4):
            mb.showinfo("Result", "Strong")
        elif(score==5):
            mb.showinfo("Result", " Very Strong")
        else:
            mb.showinfo("Result", "General Knowlege")




    def check_ans(self, q_no):
        if self.opt_selected.get() == answer3[q_no]:
            return True

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
        if self.q_no==self.data_size:
            self.display_result()
            top.destroy()
        else:
            self.display_question()
            self.display_options()

    def buttons(self):
        next_button = Button(top, text="Next",command=self.next_btn,
                             width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
        quit_button = Button(top, text="Quit", command=top.destroy,
                             width=5,bg="black", fg="white",font=("ariel",16," bold"))
        quit_button.place(x=700,y=50)


    def display_options(self):
        val=0
        self.opt_selected.set(0)
        for option in options3[self.q_no]:
            self.opts[val]['text']=option
            val+=1

    def display_question(self):
        q_no = Label(top, text=question3[self.q_no], width=60,
                     font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
        q_no.place(x=70, y=100)


    def radio_buttons(self):
        q_list = []
        y_pos = 150
        while len(q_list) < 4:
            radio_btn = Radiobutton(top,text=" ",variable=self.opt_selected,
                                    value = len(q_list)+1,font = ("ariel",14))
            q_list.append(radio_btn)
            radio_btn.place(x = 100, y = y_pos)
            y_pos += 40
        return q_list




def startsbotton():

    lbl = Label(text = "Select the level :",font = ("Times", 24) ,background="#ffffff")
    lbl.pack(pady=(100,30))
    labelimage.destroy()
    labeltext.destroy()
    btnStart.destroy()

    b1 = Button(
        top,
        text="EASY",
        pady = 10,
        bg="black",
        fg="white",
        font=("ariel",16," bold"),
        width=8,
        height=1,
        command=Easy,
    )
    b1.pack(side = TOP, ipady = 5)
    b2 = Button(
        top,
        text="MEDIUM",bg="black",
        fg="white",
        font=("ariel",16," bold"),
        width=8,
        height=1,
        command=Medium
    )
    b2.pack(side = TOP, ipady = 5)
    b3 = Button(
        top,
        text="HARD",
        bg="black",
        fg="white",
        font=("ariel",16," bold"),
        width=8,
        height=1,
        command=Hard
    )
    b3.pack(side = TOP, ipady = 5)







top = Tk()
top.geometry("800x450")
top.title("Quiz Game")
title = Label(top, text="QUIZ GAME",width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
title.place(x=0, y=2)

img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    top,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    top,
    text = "Quiz Game",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")
btnStart = Button(
    top,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startsbotton,
)
btnStart.pack()
quit_button = Button(top, text="Quit", command=top.destroy,
                     width=5,bg="black", fg="white",font=("ariel",16," bold"))
quit_button.place(x=700,y=50)

top.config(background="#ffffff")
top.resizable(0,0)


top.mainloop()