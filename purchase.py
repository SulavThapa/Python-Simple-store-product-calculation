def purchasing(List):
    list_=List
    customer=input("Enter the customers name: ")
    dict_={}
    ans="y"
    while ans=="y":
        pro_=input("Enter the product you want to purchase: ")
        products_=pro_.upper()
        if products_==list_[0][0].upper() or products_==list_[1][0].upper() or products_==list_[2][0].upper():     
            a=True
            while a==True:
                try:
                    product_number=int(input("enter product number: "))
                    a=False
                except:
                    print("Enter the value of integer:")
            if products_==list_[0][0].upper() and product_number<=int(list_[0][2]):
                dict_[products_]=product_number
            elif products_==list_[1][0].upper() and product_number<=int(list_[1][2]):
                dict_[products_]=product_number
            elif products_==list_[2][0].upper() and product_number<=int(list_[2][2]):
                dict_[products_]=product_number
            else:
                print("The product is not availabe!")
            ans=input("Do you want to buy anything more? ")
        else:
            print("Sorry!! This product not available")

    price_=0
    for key_ in dict_.keys():
        if key_=="PHONE":
            price1_Phone=int(list_[0][1])
            numA=int(dict_["PHONE"])
            price_A=(price1_Phone*numA)
            price_ += (price1_Phone*numA)
            print("the price of the phone is: ", price_)
        elif key_=="LAPTOP":
            price2_Laptop=int(list_[1][1])
            numB=int(dict_["LAPTOP"])
            price_B=(price2_Laptop*numB)
            price_ += (price2_Laptop*numB)
            print("the price of laptop is: ", price_)
        else:
            price3_HDD=int(list_[1][2])
            numC=int(dict_["HDD"])
            price_C=(price3_HDD*numC)
            price_ +=(price3_HDD*numC)
            print("the price of HDD is; ", price_)
    print("The total price of products is: ", price_)
    disc_=float(input("discounts available(%): "))
    Total_=float(price_-(disc_*price_)/100)
    print("Final cost: ", Total_)
    print("\n")

    import datetime
    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    a=str(t)
    file=open(a+".txt","w")
    file.write("--------------------------------INVOICE--------------------------------")
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write(str("Name: "+str(customer)+"                                      date: "+a))
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("________________________________________________________________________")
    file.write("\n")
    file.write("\tproducts \t Quantity \t Rate \t Price")
    file.write("\n")
    file.write("\n")

    for key_ in dict_.keys():
        if key_=="PHONE":
            file.write(str("\t"+str(key_)+" \t "+str(dict_["PHONE"])+"\t\t"+str(list_[0][1]+" \t "+str(price_A))))
            file.write("\n")
        elif key_=="LAPTOP":
            file.write(str("\t"+str(key_)+" \t "+str(dict_["LAPTOP"])+"\t\t"+str(list_[1][1]+" \t "+str(price_B))))
            file.write("\n")
        else:
            file.write(str("\t"+str(key_)+" \t "+str(dict_["HDD"])+"\t\t"+str(list_[1][1]+" \t "+str(price_C))))
            file.write("\n")

    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    file.write("\n")
    file.write("\t Total: "+str(price_))
    file.write("\n")
    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    file.write("\n")
    file.write("\t Discount: "+str(disc_))
    file.write("\n")
    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    file.write("\n")
    file.write("\t Net Total: "+str(Total_))
    file.write("\n")
    file.write("___________________________________________________________________")
    file.write("\n")
    file.write("\n")
    file.write("                              THANK YOU!                              ")
    file.write("\n")
    file.write("                            VISIT AGAIN                                ")
    file.write("\n")
    file.close()
    return dict_


