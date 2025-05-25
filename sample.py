print("WELCOME TO NITHI'S FRUIT SHOP")
fruits=[]
while 1:
    print("options")
    print("1-Add fruits")
    print("2-open shop")
    print("3- exit program")
    key=int(input("enter the key"))
    if key==1:
        fruit=input("enter the fruit ")
        fruit_quantity= int(input("enter the quantity in kg: "))
        amount_buyed = int(input("enter the amount for fruits buyed"))
        amount_sold = int(input("enter the amount of fruit per kg: "))
        obj={
            "fruit":fruit,
            "fruit_quantity": fruit_quantity,
            "amount_buyed": amount_buyed,
            "amount_sold": amount_sold
        }
        fruits.append(obj)
        print(fruits)
    if key==2:
        while 1:
            print("options")
            print("1-new buyer")
            print("2-exchange")
            print("3-refund")
            print("4-shop close")
            options=int(input("enter the options"))
            if options==1:
                basket=[]
                while 1:
                    print("PIN OPTIONS")
                    for i in range(0,len(fruits)):
                        print(f"{i+1} - {fruits[i]["fruit"]}")
                    print("404 - Bill")
                    pin=int(input("enter the pin"))
                    if pin==404:
                        break 
                    else:
                        if (pin>len(fruits)):
                            print("Enter the correct pin")
                        else:
                            weight = int(input("Enter weigth going to buy"))
                            if(weight <= fruits[pin-1]["fruit_quantity"]):
                                print("Fruit available ")
                                fruits[pin-1]["fruit_quantity"]-= weight
                                amount=weight*fruits[pin-1]["amount_sold"]
                                item={
                                    "fruit":fruits[pin-1]["fruit"],
                                    "amount": amount,
                                    "weight": weight
                                }
                                basket.append(item)
                                print(basket)
                            else:
                                print("Sorry quantity is not avalible")
                            
            if options==4:
                break
    if key==3:
        break