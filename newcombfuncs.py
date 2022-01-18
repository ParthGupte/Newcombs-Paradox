import random as rd
def genie(choice,prob):
    k=rd.random()*100
    if k<=prob:
        if choice=="M":
            M=1000000
        else:
            M=0
    else:
        if choice=="M":
            M=0
        else:
            M=1000000
    return M
def newcomb(choice,prob):
    S=0
    n=1000000
    for i in range(n):
        M=genie(choice,prob)
        if choice=="M":
            earn=M
        else:
            earn=1000+M
        S+=earn
    avg=S/n
    return avg

    


        
        
    
    
    
