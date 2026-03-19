import tkinter as tk
def calculateWeight(event):
    print("Calc weight method")
    weight = weightEntered.get() + 1
    print(weight) 

mainWindow = tk.Tk()
mainWindow.geometry("500x300+150+150")
mainWindow.title("Space Boxing GUI")

labelWeight = tk.Label(mainWindow, text="Enter your Earth weight")
labelWeight.grid(row=1, column=1, pady=5, sticky = tk.E)
weightEntered = tk.IntVar() 
spinWeight = tk.Spinbox(mainWindow, width=5, from_=50, to=300, textvariable = weightEntered)  
spinWeight.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
#binding the spinner trace event to method calculateWeight
spinWeight.bind("<Button-1>", calculateWeight) 
