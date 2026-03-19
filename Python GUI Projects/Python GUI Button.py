import tkinter as tk

def calculateArea(event):
    print("calculateArea")
#make main window
mainWindow = tk.Tk()

#set size of main window
mainWindow.geometry("600x400+600+300")
#set title of window
mainWindow.title("Tutorials on creating GUIs in Python")

#create label
labelWidth = tk.Label(mainWindow, text="Enter width: ")
labelWidth.grid(row=1, column=1, pady=10, padx=10)
txtWidth = tk.Entry(mainWindow, width=20) 
txtWidth.grid(row=1, column=2, pady=10, padx=50)

#create button
btnCalculate = tk.Button(mainWindow, text = "Calculate")
btnCalculate.grid(row=2, column=1)
#bind the button
btnCalculate.bind("<ButtonPress-1>", calculateArea)
btnCalculate.bind("<Return>", calculateArea)  
  
#start an infinite loop used to wait for user interaction with GUI and respond to interaction
mainWindow.mainloop() 
