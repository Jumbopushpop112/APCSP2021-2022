#input variables and type casting
name = input("Hey, what's your name?")
strAge = input("Ok,"+ name + ", how old are you?")  
age = int(strAge)
#statements that check for the age and print what the user can and can't do
if age < 16: 
    print("You can't drive" + name)  
elif age == 16 or age == 17: 
    print("You can drive" + name + " but you can't vote")     
elif age >=18 and age <=24:
    print("You can vote" + name + " but you can't rent a car")
elif age >= 25:  
    print("You can pretty much do anything" + name)            
else:  
    print("Error")                      
