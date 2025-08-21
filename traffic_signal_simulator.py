from tkinter import *
import time
from threading import Thread

totalTime = 152
secondsA = 1
secondsB = 1
secondsC = 1
secondsD = 1

def updateA():
    global secondsA, totalTime    
    if secondsA == 1 or totalTime == 152:
        red_signle_A.create_oval(50, 25, 150, 125, fill="white")
        green_signle_A.create_oval(50, 25, 150, 125, fill="green")
        signleA.config(text=secondsA, bg="green")        
        secondsA += 1
        totalTime -= 1
    elif secondsA != 1 and secondsA <= 35:
        red_signle_A.create_oval(50, 25, 150, 125, fill="white")
        green_signle_A.create_oval(50, 25, 150, 125, fill="green")
        signleA.config(text=secondsA, bg="green")
        secondsA += 1
        totalTime -= 1
    elif secondsA >=36 and secondsA < 39:
        green_signle_A.create_oval(50, 25, 150, 125, fill="white")
        yellow_signle_A.create_oval(50, 25, 150, 125, fill="yellow")
        signleA.config(text=(secondsA-35), bg="yellow")
        secondsA += 1
        totalTime -= 1
    elif secondsA == 39 or totalTime <= 114 and totalTime >0:
        signleA.config(text=totalTime, bg="red")
        totalTime -= 1
        yellow_signle_A.create_oval(50, 25, 150, 125, fill="white")
        red_signle_A.create_oval(50, 25, 150, 125, fill="red")
    signleA.after(1000,updateA)

def updateB():
    global secondsB, totalTime
    if totalTime <= 152 and totalTime >114:
        signleB.config(text=(totalTime-114), bg="red")       
    elif totalTime == 114:
        # signleB.config(text=secondsB)
        red_signle_B.create_oval(50, 25, 150, 125, fill="white")
        green_signle_B.create_oval(50, 25, 150, 125, fill="green")
        signleB.config(text=secondsB, bg="green")
        secondsB += 1
    elif secondsB <= 35 and secondsB != 1:
        red_signle_B.create_oval(50, 25, 150, 125, fill="white")
        green_signle_B.create_oval(50, 25, 150, 125, fill="green")
        signleB.config(text=secondsB, bg="green")
        secondsB += 1
    elif secondsB >=36 and secondsB < 39:
        green_signle_B.create_oval(50, 25, 150, 125, fill="white")
        yellow_signle_B.create_oval(50, 25, 150, 125, fill="yellow")
        signleB.config(text=(secondsB-35), bg="yellow")
        secondsB += 1
    else:
        yellow_signle_B.create_oval(50, 25, 150, 125, fill="white")
        red_signle_B.create_oval(50, 25, 150, 125, fill="red")
        signleB.config(text=totalTime+38, bg="red")

    signleB.after(1000,updateB)

def updateC():
    global secondsC, totalTime
    if totalTime <= 152 and totalTime >76:
        signleC.config(text=(totalTime-76), bg="red")       
    elif totalTime == 76:
        red_signle_C.create_oval(50, 25, 150, 125, fill="white")
        green_signle_C.create_oval(50, 25, 150, 125, fill="green")
        signleC.config(text=secondsC, bg="green")
        secondsC += 1
    elif secondsC <= 35 and secondsC != 1:
        red_signle_C.create_oval(50, 25, 150, 125, fill="white")
        green_signle_C.create_oval(50, 25, 150, 125, fill="green")
        signleC.config(text=secondsC, bg="green")
        secondsC += 1
    elif secondsC >=36 and secondsC < 39:
        green_signle_C.create_oval(50, 25, 150, 125, fill="white")
        yellow_signle_C.create_oval(50, 25, 150, 125, fill="yellow")
        signleC.config(text=(secondsC-35), bg="yellow")
        secondsC += 1
    else:
        yellow_signle_C.create_oval(50, 25, 150, 125, fill="white")
        red_signle_C.create_oval(50, 25, 150, 125, fill="red")
        signleC.config(text=totalTime+76, bg="red")

    signleC.after(1000,updateC)

def updateD():
    global secondsA,secondsB,secondsC,secondsD, totalTime
    if totalTime <= 152 and totalTime > 38:
        signleD.config(text=(totalTime-38), bg="red")       
    elif totalTime == 38:
        red_signle_D.create_oval(50, 25, 150, 125, fill="white")
        green_signle_D.create_oval(50, 25, 150, 125, fill="green")
        signleD.config(text=secondsD, bg="green")
        secondsD += 1
    elif secondsD <= 35 and secondsD != 1:
        red_signle_D.create_oval(50, 25, 150, 125, fill="white")
        green_signle_D.create_oval(50, 25, 150, 125, fill="green")
        signleD.config(text=secondsD, bg="green")
        secondsD += 1
    elif secondsD >=36 and secondsD < 39:
        green_signle_D.create_oval(50, 25, 150, 125, fill="white")
        yellow_signle_D.create_oval(50, 25, 150, 125, fill="yellow")
        signleD.config(text=(secondsD-5), bg="yellow")
        secondsD += 1
    elif totalTime==0:
        signleD.config(text=114, bg="red")
        yellow_signle_D.create_oval(50, 25, 150, 125, fill="white")
        red_signle_D.create_oval(50, 25, 150, 125, fill="red")
        totalTime = 152
        secondsD=1
        secondsC=1
        secondsB=1
        secondsA=1
    signleD.after(1000,updateD)


def start():
    print("started...")
    threadA = Thread(target=updateA,daemon=True).start()
    threadB = Thread(target=updateB,daemon=True).start()
    threadC = Thread(target=updateC,daemon=True).start()
    threadD = Thread(target=updateD,daemon=True).start()
    

# GUI setup
GUI = Tk()
GUI.title("Traffic Signal")
GUI.geometry("950x600")
GUI.config(background="WHITE")

# Signal A
signleA = Label(GUI, text="0", font=('Ariel', 40), relief="solid", bd=2, padx=35, pady=15)
signleA.config(fg="BLACK")
signleA.place(x=50, y=10)

traffic_signal_body_A = Canvas(GUI, height=450, width=200, relief="solid", bd=2)
traffic_signal_body_A.place(x=50, y=100)

red_signle_A = Canvas(traffic_signal_body_A, bg="black", height=150, width=200, relief="solid", bd=2)
red_signle_A.create_oval(50, 25, 150, 125, fill="red")
red_signle_A.place(x=0, y=0)

yellow_signle_A = Canvas(traffic_signal_body_A, bg="black", height=150, width=200, relief="solid", bd=2)
yellow_signle_A.create_oval(50, 25, 150, 125, fill="white")
yellow_signle_A.place(x=0, y=150)

green_signle_A = Canvas(traffic_signal_body_A, bg="black", height=150, width=200, relief="solid", bd=2)
green_signle_A.create_oval(50, 25, 150, 125, fill="white")
green_signle_A.place(x=0, y=300)

# Signal B
signleB = Label(GUI, text="0", font=('Ariel', 40), relief="solid", bd=2, padx=35, pady=15)
signleB.config(fg="BLACK")
signleB.place(x=280, y=10)

traffic_signal_body_B = Canvas(GUI, height=450, width=200, relief="solid", bd=2)
traffic_signal_body_B.place(x=280, y=100)

red_signle_B = Canvas(traffic_signal_body_B, bg="black", height=150, width=200, relief="solid", bd=2)
red_signle_B.create_oval(50, 25, 150, 125, fill="red")
red_signle_B.place(x=0, y=0)

yellow_signle_B = Canvas(traffic_signal_body_B, bg="black", height=150, width=200, relief="solid", bd=2)
yellow_signle_B.create_oval(50, 25, 150, 125, fill="white")
yellow_signle_B.place(x=0, y=150)

green_signle_B = Canvas(traffic_signal_body_B, bg="black", height=150, width=200, relief="solid", bd=2)
green_signle_B.create_oval(50, 25, 150, 125, fill="white")
green_signle_B.place(x=0, y=300)

# Signal C
signleC = Label(GUI, text="0", font=('Ariel', 40), relief="solid", bd=2, padx=35, pady=15)
signleC.config(fg="BLACK")
signleC.place(x=510, y=10)

traffic_signal_body_C = Canvas(GUI, height=450, width=200, relief="solid", bd=2)
traffic_signal_body_C.place(x=510, y=100)

red_signle_C = Canvas(traffic_signal_body_C, bg="black", height=150, width=200, relief="solid", bd=2)
red_signle_C.create_oval(50, 25, 150, 125, fill="red")
red_signle_C.place(x=0, y=0)

yellow_signle_C = Canvas(traffic_signal_body_C, bg="black", height=150, width=200, relief="solid", bd=2)
yellow_signle_C.create_oval(50, 25, 150, 125, fill="white")
yellow_signle_C.place(x=0, y=150)

green_signle_C = Canvas(traffic_signal_body_C, bg="black", height=150, width=200, relief="solid", bd=2)
green_signle_C.create_oval(50, 25, 150, 125, fill="white")
green_signle_C.place(x=0, y=300)

# Signal D
signleD = Label(GUI, text="0", font=('Ariel', 40), relief="solid", bd=2, padx=35, pady=15)
signleD.config(fg="BLACK")
signleD.place(x=740, y=10)

traffic_signal_body_D = Canvas(GUI, height=450, width=200, relief="solid", bd=2)
traffic_signal_body_D.place(x=740, y=100)

red_signle_D = Canvas(traffic_signal_body_D, bg="black", height=150, width=200, relief="solid", bd=2)
red_signle_D.create_oval(50, 25, 150, 125, fill="red")
red_signle_D.place(x=0, y=0)

yellow_signle_D = Canvas(traffic_signal_body_D, bg="black", height=150, width=200, relief="solid", bd=2)
yellow_signle_D.create_oval(50, 25, 150, 125, fill="white")
yellow_signle_D.place(x=0, y=150)

green_signle_D = Canvas(traffic_signal_body_D, bg="black", height=150, width=200, relief="solid", bd=2)
green_signle_D.create_oval(50, 25, 150, 125, fill="white")
green_signle_D.place(x=0, y=300)

# Buttons at the bottom
ss_button = Button(text="START", font=('Ariel', 20), command=start)
ss_button.place(x=300, y=550)

quit_button = Button(text="Quit", font=('Ariel', 20), command=exit)
quit_button.place(x=500, y=550)
GUI.mainloop()