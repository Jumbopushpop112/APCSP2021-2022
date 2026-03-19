def computeBonusThreshold(listSoldItems):
    minWage = min(listSoldItems)
    maxWage = max(listSoldItems)
    sumNums = sum(listSoldItems)
    return ((sumNums) - minWage-maxWage)/(len(listSoldItems)-2)
def displayWages(listWages):
    for x in range(len(listWages)):
        text = "Wage for employee " + str(x) + " are {:.2f}"
        print(text.format(listWages[x]))
def computeWages(fixedWage, perItemWage, curItem, listWages,bonusThreshold):
    wage = fixedWage + perItemWage * curItem
    if curItem > bonusThreshold:
        wage = wage * 1.1
    listWages.append(wage)
def main():
    listWages = []
    soldItems = [48, 50, 37, 62, 38, 70, 55, 37, 64, 60]
    # call method to compute wages
    fixedWage = 10.0
    perItemWage = 1.5
    bonusThreshold = computeBonusThreshold(soldItems)
    print("Bonus threshold for this payroll is:",bonusThreshold)
    print("Wages for employees are as follows:")
    for x in range(len(soldItems)):
        computeWages(fixedWage,perItemWage, soldItems[x], listWages, bonusThreshold)
    displayWages(listWages)
    print("Testing wages stored in listWages")
    seven = listWages[7]
    text = "Wage for employee " + str(7) + " are {:.2f}"
    print(text.format(seven))
main()

