#Calculation the value of fuel

def main():
    Crude_Oil=eval(input("What is the value of Crude Oil?"))
    Petrol=(Crude_Oil*0.56)
    Diesel=(Crude_Oil*0.32)
    Kerosene=((Petrol+Diesel)/23)
    print("The value of Petrol is",Petrol,"Kes")
    print("The value of Diesel is",Diesel,"Kes")
    print("The value os Kerosene is",Kerosene,"Kes")

main()
          
    
