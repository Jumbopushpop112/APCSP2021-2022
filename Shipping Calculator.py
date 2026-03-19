#determine shipping cost of items and find the price
def shippingCost(items):
    shippingPrice = 0
    if items == 1:
        shippingPrice = 10.95
        print("Shipping price is " + str(shippingPrice)) 
    else:
        shippingPrice = 10.95 + (2.95*(items-1))
        shippingPrice = round(shippingPrice, 2)
        print("Shipping price is " + str(shippingPrice))
#get number of items and sent to function
def main():
    items = int(input("Enter the amount of items"))
    shippingCost(items)
main() 
