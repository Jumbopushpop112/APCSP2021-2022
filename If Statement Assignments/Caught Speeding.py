#enter speed and cast to an int
speed = int(input("Enter your speed"))
#enter birthday 
birthday = input("Is it your birthday?")
#if statements that deal with the cases. If birthday is yes speed is equal to speed - 5. We check to see if the string is equal to Yes or No. Results are displayed accordingly. 
if birthday == " Yes": 
    speed -= 5
    if speed <= 60:    
        print("No ticket")
    if speed >= 61 and speed <= 80:
        print("Small ticket")
    if speed >= 81:
        print("Big Ticket")

if birthday == " No": 
    if speed <= 60: 
        print("No ticket")
    if speed >= 61 and speed <= 80:
        print("Small ticket") 
    if speed >= 81:  
        print("Big Ticket") 
     
