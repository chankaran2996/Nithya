print("Wellcome to Nithi's Friuths")
fruits=[]
while 1:
    print("options")
    print("1 - Add friuts")
    print("2 - open shop")
    print("3 - Exit program")
    key=int(input("Enter the key"))
    if key==1:
        fruit = input("Enter fruit name:")
        fruitQunatity = int(input("Enter the fruit quanty in kg you brought"))
        amtBuyed=int(input("Enter the amount in rupees"))
        amtSell=int(input("Enter the amount in rupees at per kg of fruit"))
        obj={
            "fruit":fruit,
            "fruitQuantity":fruitQunatity,
            "amtBuyed":amtBuyed,
            "amtSell":amtSell
        }
        fruits.append(obj)
        # print(fruits)
    
    if key ==2:
        while 1:
            print("Options")
            print("1 - New buyer")
            print("2 - Exchange")
            print("3 - refund")
            print("4 - shop close")
            option = int(input("Enter the option"))
            
            if option == 1:
                while 1:
                    basket=[]
                    print("PIN options")
                    for i in range(0 , len(fruits)):
                        print(f"{i+1} - {fruits[i]["fruit"]}")
                    print("404 - Bill")
                    pin=int(input("Enter the PIN:"))
                    if pin==404:
                        break
                    else:
                        weigth
            
            if option == 4:
                break
    if key == 3:
        break
    

        