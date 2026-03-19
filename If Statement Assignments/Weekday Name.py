import tkinter as tk

def weekDayName(event):
    #get the text from the box and type cast
    day = txtWidth.get()
    day = int(day)
    #if statements that check the number and match it to the day.  
    if(day == 0 or day == 7):  
        print("Number entered is",str(day),"and day is Saturday") 
    elif (day == 1):
        print("Number entered is",str(day),"and day is Sunday") 
    elif (day == 2):
        print("Number entered is",str(day),"and day is Monday") 
    elif (day == 3):
        print("Number entered is",str(day),"and day is Tuesday")  
    elif (day == 4):
        print("Number entered is",str(day),"and day is Wednesday")  
    elif (day == 5):
        print("Number entered is",str(day),"and day is Thursday") 
    elif (day == 6):
        print("Number entered is",str(day),"and day is Friday") 
    else:
        print("Error") 
         
#make main window
mainWindow = tk.Tk()     

#set size of main window
mainWindow.geometry("600x400+600+300")
#set title of window
mainWindow.title("Tutorials on creating GUIs in Python")

#create label
labelWidth = tk.Label(mainWindow, text="Enter a number from 0-7 and I will display the day: ")
labelWidth.grid(row=1, column=1, pady=10, padx=10)
txtWidth = tk.Entry(mainWindow, width=20) 
txtWidth.grid(row=1, column=2, pady=10, padx=50)

#create button
btnCalculate = tk.Button(mainWindow, text = "Calculate")
btnCalculate.grid(row=2, column=1)
#bind the button
btnCalculate.bind("<ButtonPress-1>", weekDayName)
btnCalculate.bind("<Return>", weekDayName)  
  
#start an infinite loop used to wait for user interaction with GUI and respond to interaction
mainWindow.mainloop() 
 
