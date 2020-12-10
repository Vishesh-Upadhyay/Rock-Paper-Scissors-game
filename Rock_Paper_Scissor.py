import random , pygame
def take_input():
    #print("ARE YOU READY ???")
    print("***************************************************************************************************")
    a= input("Please make your choice --> \n 1 --> ROCK \n 2 --> PAPER \n 3 --> SCISSORS \n \t \t")
    a= int(a)
    if a>3:
        print(" XX----INVALID VLAUE OF A----XX ")
    return a


def calculate(a):
    b= abs(random.randint(1,3))
    if ( a==b ):
        print("ITS A DRAW \n \t\t BETTER LUCK NEXT TIME ")
    elif((a==1 and b==2)or(a==2 and b==3)or(a==3 and b==1)):
        print("OOPS YOU LOST :,( ") 
    elif((a==1 and b==3) or (a==3 and b==2) or (a==2 and b==1)):
        print("!!!! CONRATULATIONS YOU WON !!!!") 
    else:
        print("XX--ITS AN INVALID CHOICE--XX")
    return b         


def setter(a,b):    
        if a==1:
            a1="ROCK"
        elif a==2:
            a1="PAPER"
        elif a==3:
            a1="SCISSORS"
        if (b==1):
            b1="ROCK"
        elif (b==2):
            b1="PAPER"
        elif (b==3):
            b1="SCISSORS"       
        print("YOU CHOSE : ",a1,"\n COMPUTER CHOSE : ",b1)
    
  
class main:
    print("Hey! Welcome Lets PLAY!!!!")  
    print("***************************************************************************************************")
    i = True
    while i:
        s=input(" --> START \n --> EXIT ")    
        if s == "START" or s == "start":  
            c = take_input()
            d = calculate(c)
            setter(c,d)
        elif s == "EXIT" or s == "exit":
            print("----THANKYOU FOR PLAYING---- ")
            i= False
        else:
             print(" || INVALID CHOICE || ")    
    

      

