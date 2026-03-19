#main function that asks the user for the planet they are visiting and their earth weight. The function is called and is sent the weight and the planet number
def main():
    earthWeight = int(input("Enter your Earth weight please!"))
    message = f"I have information for the following planets:\n\t" \
              f"1. Venus\t2. Mars\t\t3. Jupiter\n\t" \
              f"4. Saturn\t5. Uranus\t6. Neptune\n"
    planetNum = int(input(message + "Which planet are you visiting? "))
    displayPlanetWeight(earthWeight,planetNum)
#function that displays the planet weight and multiplites the weight times the relative gravity of the planet.
def displayPlanetWeight(earthWeight, planetNum):
    if planetNum == 1:
        print("Your weight on Venus is",earthWeight*0.78)
    if planetNum == 2:
        print("Your weight on Mars is",earthWeight*0.39)
    if planetNum == 3:
        print("Your weight on Jupiter is",earthWeight*2.65)
    if planetNum == 4:
        print("Your weight on Saturn is",earthWeight*1.17)
    if planetNum == 5:
        print("Your weight on Uranus is",earthWeight*1.05)
    if planetNum == 6:
        print("Your weight on Neptune is",earthWeight*1.23)
main()
