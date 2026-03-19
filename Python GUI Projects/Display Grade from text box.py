import tkinter as tk

def calculateGrade(event):
    grade = txtWidth.get()
    grade = int(grade) 
    if grade <= 59 and grade >= 0:
        print("Grade is an F")
    elif grade <= 69 and grade >= 60:
        print("Grade is a D")
    elif grade <= 79 and grade >= 70:
        print("Grade is a C")
    elif grade <= 89 and grade >= 89:
        print("Grade is a B")
    else:   
        print("Grade is an A")   
    
#make main window 
mainWindow = tk.Tk()   

#set size of main window
mainWindow.geometry("600x400+600+300")  
#set title of window
mainWindow.title("Tutorials on creating GUIs in Python")

#create label
labelWidth = tk.Label(mainWindow, text="Enter grade: ")
labelWidth.grid(row=1, column=1, pady=10, padx=10)
txtWidth = tk.Entry(mainWindow, width=20) 
txtWidth.grid(row=1, column=2, pady=10, padx=50)

#create button
btnCalculate = tk.Button(mainWindow, text = "Calculate Grade")
btnCalculate.grid(row=2, column=1)
#bind the button
btnCalculate.bind("<ButtonPress-1>", calculateGrade)
btnCalculate.bind("<Return>", calculateGrade)  
  
#start an infinite loop used to wait for user interaction with GUI and respond to interaction
mainWindow.mainloop() 
