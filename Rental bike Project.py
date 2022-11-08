class Bikeshop:
    def __init__(self,stock) :
        self.stock = stock
    def displayBikes(self) :
        print("Total Bikes", self.stock)
    def rentforBike(self,q) :

        if q<=0 :
            print("Enter the positive value or greater than zero")
        elif q>=self.stock :
            print("Enter the valur(Less than stock")

        else :
            self.stock = self.stock - q
            print ("Total Prices", q*100)
            print ("Total Bikes" , self.stock)

while True:
    obj = Bikeshop(100)
    UC = int(input('''
    
    1 Display Stocks
    2 Rent a Bike
    3 Exit
    
    '''))

    if UC == 1 :
        obj.displayBikes()
    elif UC == 2 :
        n = int(input("Enter the Qty :--- "))
        obj.rentforBike(n)
    else:
        break        
