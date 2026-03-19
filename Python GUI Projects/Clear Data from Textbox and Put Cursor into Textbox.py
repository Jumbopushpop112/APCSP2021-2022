import tkinter as tk

def calculateArea(event):
    weightEntered = float(txtWidth.get())
    print(weightEntered)

def reset(event): 
    txtWidth.delete("0", tk.END)

#make main window
mainWindow = tk.Tk()
      
#set size of main window
mainWindow.geometry("600x400+600+300")
#set title of window
mainWindow.title("Tutorials on creating GUIs in Python")
#create label and textbox (Entry widget)
labelWidth = tk.Label(mainWindow, text="Enter width: ")
labelWidth.grid(row=1, column=1, pady=10, padx=10)
txtWidth = tk.Entry(mainWindow, width=50)
txtWidth.grid(row=1, column=2, pady=10, padx=0)

#create button
btnCalculate = tk.Button(mainWindow, text="Calculate")
btnCalculate.grid(row=2, column=1)
#bind the button 
btnCalculate.bind("<ButtonPress-1>", calculateArea)
btnCalculate.bind("<Return>", calculateArea)
 
#create reset button
btnReset = tk.Button(mainWindow, text="Reset")
btnReset.grid(row=2, column=2)
#bind the button
btnReset.bind("<ButtonPress-1>", reset)
btnReset.bind("<Return>", reset)

mainWindow.mainloop() 
