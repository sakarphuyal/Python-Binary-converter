#Binary Addition:

import logicalgates
#defining the function
def adder(a,b,cin):
    #Carrying out the logical Operation
    sum1 = logicalgates.xorgate(a,b)
    sum_value=logicalgates.xorgate(sum1,cin)

    carryout = logicalgates.andgate(a,b)
    carryout1 =logicalgates.andgate(sum1,cin)
    carryout_value = logicalgates.orgate(carryout,carryout1)
    # Returning the value
    return(sum_value,carryout_value)


