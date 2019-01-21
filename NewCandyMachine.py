def choose_candy_fun():
    mango_avail = 20
    orange_avail = 20
    lemon_avail = 20
    emli_avail = 20
    cont = "y"
    total_mango=0
    total_orange=0
    total_lemon=0
    total_emli=0

    while cont!="n" or cont!="N":
        if cont == "y" or cont == "Y":
            choose_candy = input("Choose flavour : \n1.  Mango(Available = "+str(mango_avail)+
            ")   2.  Orange(Available = "+str(orange_avail)+
            ")   3.  Lemon(Available = "+str(lemon_avail)+
            ")   4.  Emli(Available = "+str(emli_avail)+")\n(2 Rs./candy).\n")

            if choose_candy == "1":
                if mango_avail==0:
                    print("Sorry, We have no stock of Mango Candy.")
                else:
                    mango = int(input("How many Mango candies you want?\n"))
                    i=1
                    while i<=mango:
                        total_mango += 1
                        print("Mango Candy "+str(total_mango))
                        i+=1
                        mango_avail-=1

            elif choose_candy == "2":
                if orange_avail==0:
                    print("Sorry, We have no stock of Orange Candy.")
                else:
                    orange = int(input("How many Orange candies you want?\n"))
                    j=1
                    while j<=orange:
                        total_orange += 1
                        print("Orange Candy "+str(total_orange))
                        j += 1
                        orange_avail-=1

                if orange < orange_avail:
                    print("Sorry, We have no stock of Orange Candy.")

            elif choose_candy == "3":
                if lemon_avail==0:
                    print("Sorry, We have no stock of Lemon Candy.")
                else:
                    lemon = int(input("How many Lemon candies you want?\n"))
                    k = 1
                    while k <= lemon:
                        total_lemon += 1
                        print("Lemon Candy "+str(total_lemon))
                        k += 1
                        lemon_avail-=1


            elif choose_candy == "4":
                if emli_avail==0:
                    print("Sorry, We have no stock of Emli Candy.")
                else:
                    emli = int(input("How many Emli candies you want?\n"))
                    l = 1
                    while l <= emli:
                        total_emli += 1
                        print("Emli Candy " +str(total_emli))
                        l += 1
                        emli_avail-=1

            else:
                print("Ohh!! You entered wrong input.")
        print("We have "+str(mango_avail)+" Mango candies, "+str(orange_avail)+" Orange candies, "+str(lemon_avail)+" Lemon candies, "+str(emli_avail)+" Emli Candies in stock.")
        cont = input("Do you want to continue?:(Y/N)\n")

        if cont =="n" or cont == "N":
            total_amount = (total_mango + total_orange + total_lemon + total_emli) * 2
            print("You got total "+str(total_mango)+" Mango, "+str(total_orange)+" Orange, "+str(total_lemon)+" Lemon, "+str(total_emli)+" Emli Candies.\nTotal amount you need pay is: "+str(total_amount))
            tata = input("Thank You for visit!")
            exit()
        elif cont == "y" or cont=="Y":
            pass
        else:
            print("Ohh!!!. You entered wrong input.")
ctn = ""
while ctn!="n" or ctn!="n":
    x =input("Welcome to Chatpatti Candy shop!!!\n\nIf you want to buy candies enter 'Y'.\nOtherwise enter 'N':\n")
    if x=="y" or x=="Y":
        choose_candy_fun()
    elif x=="n" or x=="N":
        break
    else:
        print("Sorry,Invalid Entry!!!")
        ctn = input("Do you want to buy candy?: (Y/N)\n")

tata= input("Thank You for visit!")