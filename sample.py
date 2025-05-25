print("WELCOME TO NITHI'S FRUIT SHOP")
fruits=[]
sold_fruits=[]
collected_amount=0
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
            # print("2-exchange")
            # print("3-refund")
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
                        price=0
                        print(f"BILL - {len(sold_fruits)}")
                        if len(basket)>0:
                            print("BILL")
                            for x in range(len(basket)):
                                price += basket[x]["amount"]
                                print(f"{x+1} - {basket[x]["fruit"]} - {basket[x]["weight"]} * {basket[x]["amount_per_kg"]} = {basket[x]["amount"]}")  
                            print(f"TOTAL AMOUNT={price}")
                            sold_fruits.append(basket)
                            collected_amount += price
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
                                    "amount_per_kg": fruits[pin-1]["amount_sold"],
                                    "weight": weight
                                }
                                basket.append(item)
                                print(basket)
                            else:
                                print("Sorry quantity is not avalible")

            if options==4:
                print(basket)
                print(f"collected_amount - {collected_amount}")
                break
    if key==3:
        break