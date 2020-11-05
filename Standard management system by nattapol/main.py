import sqlite3


TypeList = []
PriceList = []
QuantityList = []
MenuSelected = 0
####### welcome #######


def HomePage():
        print("Welcome to Carrier Gas Management System")
        print("----------------------------------------")
        print("          Please select the menu        ")
        print("----------------------------------------")
        print("[1] Add new item")
        print("[2] Remove item")
        print("[3] Edit item")
        print("[4] Show all items")
        print("[5] Exit Program")
        ChooseMenu()

def ChooseMenu():
        MenuSelected = int(input("Please Select Menu : "))
        if MenuSelected == 1:
            Menu1()
        if MenuSelected == 2:
            Menu2()
        if MenuSelected == 3:
            Menu3()
        if MenuSelected == 4:
            Menu4()
        if MenuSelected == 5:
            Menu5()



def Menu5():
    ExitConfirm = input("Do you want to exit (Yes/No) : ")
    while True:
        if (ExitConfirm.lower() == "yes"):
            break
        else: HomePage()

def Menu1():
     while True:
        CarrierGasType = input("Enter Standard gas type :")
        if (CarrierGasType.lower() == "yes"):
            break
        else:
            CarrierGasPrice = input("Enter Price :")
            CarrierGasQty = input("Enter Quantity :")
            TypeList.append(CarrierGasType)
            PriceList.append(CarrierGasPrice )
            QuantityList.append(CarrierGasQty)
            c.execute("INSERT INTO `CARRIER_GAS` (gas_name, gas_qty, gas_price) VALUES(?, ?, ?)",
                           (str(CarrierGasType.get()), int(CarrierGasQty.get()), int(CarrierGasPrice.get())))
            conn.commit()
            print("Add new item Successfully !!!")
            HomePage()
def Menu4():
    print("---- Standard Gas List ----")
    for number in range(len(TypeList)):
        print(TypeList[number], PriceList[number])
    ExitConfirm = input("Do you want to back to menu (Yes/No) : ")
    while True:
        if (ExitConfirm.lower() == "yes"):
            HomePage()
        else:
            break

def Menu2():
    itemdelete = 1 - int(input("What number of Item You want to delete : "))
    TypeList.pop(itemdelete)
    PriceList.pop(itemdelete)
    print("Delete Item Successfully !!!")
    HomePage()

def Menu3():
    Edit_Number = 1 - int(input("What number of Item you want to edit"))
    print("[1] Edit Type")
    print("[2] Edit Price")
    Edit_menu = int(input("What do you want to edit [1] or [2]"))
    if Edit_menu == 1:
        TypeList[Edit_Number] = input("Enter new edit data : ")
        print("Edit Successfully !!!")
        HomePage()
    elif Edit_menu == 2:
        PriceList[Edit_Number] = input("Enter new edit data : ")
        print("Edit Successfully !!!")
        HomePage()
    else:
        print("Wrong Input !!!")

conn = sqlite3.connect('test1.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS `CARRIER_GAS2` (gas_name TEXT, gas_qty TEXT, gas_price TEXT)")
c.execute("INSERT INTO CARRIER_GAS2 VALUES('Oxygen', '10', '500')")
conn.commit()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()