from tkinter import *

def num_click(target, label, res_label):
    expression = label['text'] + target
    result = str(eval(expression))
    label.configure(text=expression)
    res_label.configure(text=result)

def operator_click(target, ex_label, res_label):
    expression = ex_label['text']
    if target == "=":
        result = str(eval(expression))
        ex_label.configure(text=result)
        res_label.configure(text="")
    else :
        expression += target
        ex_label.configure(text=expression)

def init_calcul(ex_label, res_label):
    ex_label.configure(text="")
    res_label.configure(text="")

class NumBtn:
    def __init__(self, window, width, height, text):
        self.name = text
        self.button = Button(window, width=width, height=height, text=text, command=lambda: num_click(self.name, expr_label, result_label))

    def get_name(self):
        return self.name
    
    def place(self, x, y):
        self.button.place(x=x, y=y)

class OperBtn:
    def __init__(self, window, width, height, text):
        self.name = text
        self.button = Button(window, width=width, height=height, text=text, command=lambda: operator_click(self.name, expr_label, result_label))

    def get_name(self):
        return self.name
    
    def place(self, x, y):
        self.button.place(x=x, y=y)

numberBtn = []
xStep = 80
yStep = 80

def set_operatorBtn(window):
    operatorBtn = []
    operatorBtn.append(OperBtn(window, width=5, height=3, text="*"))
    operatorBtn[0].place(x = 240, y = 80)
    operatorBtn.append(OperBtn(window, width=5, height=3, text="+"))
    operatorBtn[1].place(x = 240, y = 80 * 2)
    operatorBtn.append(OperBtn(window, width=5, height=3, text="-"))
    operatorBtn[2].place(x = 240, y = 80 * 3)
    operatorBtn.append(OperBtn(window, width=5, height=3, text="/"))
    operatorBtn[3].place(x = 240, y = 80 * 4)
    operatorBtn.append(OperBtn(window, width=5, height=3, text="="))
    operatorBtn[4].place(x = 160, y = 80 * 4)

window = Tk()

window.title("계산기") # window name
window.geometry("410x410") # size of window
window.resizable(0, 0) # 0 - cannot resize window 1 - can resize window

expr_label = Label(window, bg="light green", width=400, height=2)
expr_label.pack()
result_label = Label(window, bg="pink", width=400, height=2)
result_label.pack()

for i in range(0, 10):
    num = str(i)
    numberBtn.append(NumBtn(window, width=5, height=3, text=num))
    if i == 0:
        numberBtn[i].place(x=0, y= 80 * 4)
    else :
        numberBtn[i].place(x=((i - 1)%3)*xStep, y=((i - 1)//3 + 1) * yStep)

set_operatorBtn(window)

execBtn = Button(window, width=5, height=3, text="C", command=lambda: init_calcul(expr_label, result_label))
execBtn.place(x = 80 * 4, y = 80)
dotBtn = NumBtn(window, width=5, height=3, text=".")
dotBtn.place(x = 80, y = 80 * 4)

window.mainloop()