def calcTaxiFare(totalKM):
    baseFare = 4.00 +((1000*totalKM)//140)*0.25
    return baseFare
def main():
    totalKM = int(input("Enter the number of kilometers you went slacker"))
    calcTaxiFare(totalKM)
main()