import sys
import re
import string

def main():
    
    print("Make sure you follow this syntax: (x1,x2) and make sure ")
    print("Input first line:")
    input_str = sys.stdin.readline().strip().strip("()").split(",")
    print("Input second line:")
    input_str2 = sys.stdin.readline().strip().strip("()").split(",")
   
    x1 = int(input_str[0])
    x2 = int(input_str[1])
    x3 = int(input_str2[0])
    x4 = int(input_str2[1])
    if checkOverlap(x1,x2,x3,x4):
        print("Points "+"("+str(x1)+","+str(x2)+")"+ " overlap with " +"("+str(x3)+","+str(x4)+")")
    else:
        print("Points "+"("+str(x1)+","+str(x2)+")"+ " do not overlap with " +"("+str(x3)+","+str(x4)+")")
    
def checkOverlap(x1:int,x2:int,x3:int,x4:int) ->bool:
     #swap if the numbers are not in ascending order
    
    if(x1>x2):
        x1,x2=x2,x1   
    if(x3>x4):
        x3,x4=x4,x3

    # Assumed if at least one point are the same it is an overlap
    if (x1<=0 and x2<=0) and (x3<=0 and x4<=0):
        x1=abs(x1)
        x2=abs(x2)
        x3=abs(x3)
        x4=abs(x4)
        if (x1<x3 and x2<x4 and x2<x3 and x1<x4) or (x2>x4 and x1>x3 and x2<x3 and x1<x4) :    
            return False
        return True
    else:
        if (x1<x3 and x2<x4 and x2<x3 and x1<x4) or (x2>x4 and x1>x3 and x2<x3 and x1<x4) :    
            return False
        return True
    return True

if __name__ == '__main__':
    main()