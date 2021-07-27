#import Binary_addition
import decimal
from Binary_addition import adder
play = True#set play as True
while play == True:#while condition 
    sucess  = False#set sucess as False
    while sucess == False:#checlkin for the condition
        try:
            num1=int(input("Enter the 1st Decimal number: "))
            if(num1>0 and num1<=255):#Checking if condition
                sucess=True#set sucess as true
                break
        except:
            print("Opps!!!Invalid input type")
    sucess = False
    while sucess ==False:
        try:
            num2=int(input("Enter the 2nd Decimal number: "))
            if(num2>0 and num2<=255):
                sucess=True
                break
        except:
            print("opps!!! Invalid input type")


    print("\n")  
    print("first decimal number is: "+str(num1))  
    print("first decimal number is: "+str(num2))
    print("\n")
    print("Binary value of"" " +str(num1)+" " "is:")
    b_c1 = decimal.decimalconversion(num1)# calling the Function
    print("Binary value of" " "+str(num2)+" ""is:")
    b_c2 = decimal.decimalconversion(num2)# calling the Function 

    #set the first carryover value to 0
    cin = 0
    sums = ''
    for i in range(7,-1,-1):#loop to check the list from last
        value1 = adder(b_c1[i],b_c2[i],cin)#invoke the value in function 
        sums = sums +str(value1[0])
        cin = value1[-1]
    print()
    print('The sum is',sums[::-1])#loop to reserve List

    print("\n")
    continue_calculation=input("Do you want to continue or exit???Enter 'no' for exit (i)").lower()
    if continue_calculation=="no":
        play = False
        print("Thank you!!!! ")
