
def lemonadeChange(bills):
    """return True if we can return change to each customer"""

    num_5s = 0
    num_10s = 0

    for bill in bills:
        if bill == 5:
            num_5s += 1
            print("PLUS 5, num 5s", num_5s, "num 10s", num_10s)
        
        if bill == 10:
            if num_5s == 0:
                return False
            else:
                num_10s += 1
                num_5s -= 1
                print("PLUS 10, num 5s", num_5s, "num 10s", num_10s)
                
        if bill == 20:
            #no 5s
            if num_5s == 0:
                return False
            #no 5s and no 10s
            if num_10s == 0 and num_5s < 3:
                return False
            #no 10s, all 5s
            if num_10s == 0 and num_5s >=3:
                num_5s -= 3
                print("MINUS 3 5's, num 5s", num_5s, "num 10s", num_10s)
            #one 10, one 5
            if num_10s >=1 and num_5s >= 1:
                num_10s -= 1
                num_5s -= 1
                print("MINUS one 5 one 10, num 5s", num_5s, "num 10s", num_10s)
        
        return True

print(lemonadeChange([5,5,10,10,20]))

                    
                    