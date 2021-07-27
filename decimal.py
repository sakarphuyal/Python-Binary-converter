# Decimal to binary:
#initializing the empty list
answer=[]
def decimalconversion(num):# defining Function
   
    l=[]#initializing the Empty list

    while num>0:#While condition
        if num%2==0:#checking the condition
            l.append(0)#adding the value in list
        else:
            l.append(1)#adding the value in list
        num =num//2#num2 is the quotient of the division of num by 2
    l2=l[::-1]#reverse the list
    
    
    for i in range(8-len(l2)):#for loop to make 8 bit
         l2.insert(0,0)#inserting 0
    print(l2)
    return l2#returning the value of l2
    
