def steps(number):
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    while(number!=1):
        #print(f"{step}. {number}")                
        if is_even(number):
            number = number // 2
            step +=1
        else:
            number = odd_calc(number)
            step += 1
        #print(f"{step}. {number}")        
    return step        
        
        
def is_even(number):
    if number%2 == 0:
        return True
    return False

def odd_calc(number):
    return (number * 3)+1

print(steps(12))