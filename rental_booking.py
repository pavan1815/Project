class AddCustomer:
    def getDetails(self):
        self.customerName = input("Enter Customer Name : ")
        self.phoneNo = input("Enter Customer Phone Number : ")
        self.email = input("Enter Customer Email Id : ")
    def printDetails(self):
        print("----------------------------------------------------")
        print("            customer details                        ")
        print("----------------------------------------------------")
        print("Customer Name : ",self.customerName)
        print("Customer Phone Number : ",self.phoneNo)
        print("Customer Email Id : ",self.email)

class RentalBooking(AddCustomer):
    def __init__(self):
        AddCustomer.__init__(self)
    def getDetails(self,):
        self.rentalDate = str(input('Enter rental date(yyyy-mm-dd): '))
        self.returnDate = str(input('Enter return date(yyyy-mm-dd): '))
        
def booking(vehicleType,inventory):
    if vehicleType == 1:
        if inventory["bikes"]>0:
            inventory["bikes"]-=1
            return 1
        else:
            print("bikes cannot be rented as it is already booked")
            return 0
    elif vehicleType==2:
        if inventory["cycles"]>0:
            inventory["cycles"]-=1
            return 1
        else:
            print("bikes cannot be rented as it is already booked")
            return 0
    elif vehicleType==3:
        if inventory["cars"]>0:
            inventory["cars"]-=1
            return 1
        else:
            print("bikes cannot be rented as it is already booked")
            return 0
    elif vehicleType==4:
        if inventory["boats"]>0:
            inventory["boats"]-=1
            return 1
        else:
            print("bikes cannot be rented as it is already booked")
            return 0


customers = []
rent_bookings = []
inventory = {"bikes" : 2,"cycles":3,"cars" : 1,"boats" : 2}
exit = False
print("----------------------------------------------------")
print("            Welcome to Rental Booking               ")
print("----------------------------------------------------")
while(not exit):
    choice = int(input("""
enter the below options to do tasks
-->1 . Add Customer 
-->2 . Add Rental Booking
-->3 . view customers list
-->4 . view rental booking
-->5 . show inventory
-->6 . Exit 
  >>"""))
    if(choice == 1):
        customer = AddCustomer()
        customer.getDetails()
        customers.append([customer.customerName,customer.phoneNo,customer.email])
        print("Below customer details are added")
        customer.printDetails()
    elif(choice == 2):
        rent = RentalBooking()
        print("enter a customer name from the available customers shown below")
        print(customers)
        custName = input("Enter customer name : ")
        vehicleType = int(input("""
Enter : -->1 for bike
        -->2 for cycle
        -->3 for car
        -->4 for boat
  >>"""))
        vehicle = {1 : "bike",2 : "cycle",3 : "car",4 : "boat"}
        rent.getDetails()
        res = booking(vehicleType,inventory)
        if(res == 1):
            print("Booking succesfully")
            rent_bookings.append([custName,vehicle[vehicleType],rent.rentalDate,rent.returnDate])
        else:
            print("Booking unsuccesfully")
    elif(choice==3):
        print("----------------------------------------------------")
        print("            Available customers are                 ")
        print("----------------------------------------------------")
        j=1
        for i in customers:
            print(j," : ",i[0])
            j+=1
    elif(choice == 4):
        print("Currrent rental bookings are : ")
        j = 1
        for i in rent_bookings:
            print(j," : ",*i)
            j+=1
    elif(choice == 5):
        print("Vehicles available in the inventory are : ")
        print(inventory)
        print("bikes available : " ,inventory["bikes"])
        print("cycles available : " ,inventory["cycles"])
        print("cars available : " ,inventory["cars"])
        print("boats available : " ,inventory["boats"])
    elif(choice == 6):
        exit = True
    else:
        print("Please enter correct choice : ")
        choice = int(input("""
Welcome to Rental Booking 
enter the below options to do tasks
1 . Add Customer 
2 . Add Rental Booking
3 . view customers list
4 . view rental booking
5 . show inventory
6 . Exit 
>>"""))
        exit = False
