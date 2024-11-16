import money_monitor as mm
import os

amount = int(input("Enter the total amount: "))

balance = int(input("Enter the balance amount: "))

spent_amount = amount - balance

# print("Total Spent Amount: ",used_amount)

l1 = [0]

while True:

    print ("1) Grocery")
    print ("2) Food")
    print ("3) others")

    select= int(input("select options from above: "))
    
    spent = 0

    if select == 1:
        groceries_amount = int(input("Amount spent on Groceries: "))
        spent = spent + groceries_amount
        add = input("Do you want to add something else: (y)es or (n)o")

        try:
            y=l1.append(spent)

            if add == "Y" or add == "y":
                os.system("cls")
                print("spent as of now: ",spent)
                print("Stored: ",l1)
                
                
            elif add == "N" or add == "n":
                x=sum(l1)
                print("Stored: ",l1)
                print("Amount you had: ", amount)
                print("Total spent amount: ",x)

                if x>spent_amount:
                    print("Over charged: ",amount - x)
                    print("Spent too much!")
                else:
                    print("saved: ",amount-x)
                break

            else:
                print("Invalid!")

        except:
            print("Out of bound!")
    

    elif select == 2:
        food_amount = int(input("Amount spent on Food: "))
        spent = spent + food_amount
        add = input("Do you want to add something else: (y)es or (n)o ")
        
        try:
            y = l1.append(spent)

            if add == "Y" or add == "y":
                os.system("cls")
                print("spent as of now: ",spent)
                print("Stored: ",l1)
                
                
            elif add == "N" or add == "n":
                x=sum(l1)
                print("Stored: ",l1)
                print("Amount you had: ", amount)
                print("Total spent amount: ",x)

                if x>spent_amount:
                    print("Over charged: ",amount - x)
                    print("Spent too much!")
                else:
                    print("saved: ",amount-x)
                break

            else:
                print("Invalid!")
        

        except:
            print("Out of bound!")

    elif select == 3:
        other_amount = int(input("Amount spent on Others(like petrol): "))
        spent = spent + other_amount
        add = input("Do you want to add something else: (y)es or (n)o")
        
        try:
            y=l1.append(spent)

            if add == "Y" or add == "y":
                os.system("cls")
                print("spent as of now: ",spent)
                print("Stored: ",l1)
                
                
            elif add == "N" or add == "n":
                x=sum(l1)
                print("Stored: ",l1)
                print("Amount you had: ", amount)
                print("Total spent amount: ",x)
                if x>spent_amount:
                    print("Over spent: ",amount - x)
                    print("Spent too much!")
                else:
                    print("saved: ",amount-x)
                break
            
            else:
                print("Invalid!")
            

        except:
            print("Out of bound!")

    else:
        print("invalid!")
        exit()


