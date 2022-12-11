''' 
Ethan Perry
April 10, 2022
'''
#------------------------ start ------------------------

def greeter():
    print(f"\nHello, welcome to the Prime Numbers and More.")
    name = input("Please enter your name to start: ")
    bool_enter = input(f"Are you ready to start, {name}? (Y/N) ")
    if bool_enter == "y" or bool_enter == "Y":
        num= 1
        # initialized num variable to avoid having two prompts for index value
        directory(num)
    else:
        greeter()
    
    
def directory(num):
    
    while (num> -1):
        print(f"\nPlease enter a option below. (Enter 0 to quit.)")
        print(f"{'1) Unique Factorization' :<10}")
        print(f"{'2) Coprime' :<10}")
        print(f"{'3) Least Common Multiple' :<10}")
        print(f"{'-'*55}")
        
        num= int(input('Enter index value: '))
        
        if num== 1:
            print(fact('num'))
            
        if num== 2: 
            print(coprime('num1', 'num2'))
            
        if num== 3:        
            print(lcm('num1', 'num2'))
            
        if num> 3:
            print("error, try again")
        
        if num== 0:
            print(f"Thanks for playing.\n", f"{'-'*55}")
            break

# --------------------- unique fact --------------------------
 
def fact(num):
    # had to initiliaze a bunch of variable unfortunately
    count2s = 0
    count3s = 0
    count5s = 0
    count7s = 0
    countLarge = 0
    filler = 0
    
    facts = []
    uniques = []
    
    num = int(input("Please enter a positive integer: "))

#-----weeding out invalid inputs--------  
    if num == 1:
        return (f"1's factor is not clearly definable. 1^1")
    
    input_num = num
        
    while num <= 0:
        print(f'Error: invalid input. Please try again.\n')
        num = int(input("Please enter a positive integer: "))
    # below assumes num > 0
    
# start of program 
    # even numbers
    while num % 2 == 0:
        uniques.append(2)
        num = num // 2
        count2s = count2s + 1 
        
    # catches everything else after even numbers
    for i in range(3, input_num, 2):
        while (num % i == 0):
            uniques.append(i)
            num = num // i
    uniques.append(num) # this grabs left over factors.

# exponent values
    
    for i in range(len(uniques)):
        if uniques[i] == 1:
            del uniques[i] 
    for i in range(len(uniques)):       
        if uniques[i] == 3:
            count3s += 1
    for i in range(len(uniques)):
        if uniques[i] == 5:
            count5s += 1
    for i in range(len(uniques)):
        if uniques[i] == 7:
            count7s += 1
    for i in range(len(uniques)):
        if uniques[i] > 10:
            countLarge += 1
            valLarge = uniques[i]

#---appending facts list to get output string formatting ready--

    if count2s > 0:
        print2s = f"2^{count2s}"
        facts.append(print2s)
    else:
        filler = 1
    
    if count3s > 0:
        print3s = f"3^{count3s}" 
        facts.append(print3s)
    else:
        filler = 2
        
    if count5s > 0:
        print5s = f"5^{count5s}"
        facts.append(print5s)
    else:
        filler = 1
        
    if count7s > 0:
        print7s = f"7^{count7s}"
        facts.append(print7s)
    else:
        filler = 0
        
    if countLarge > 0:
        printLarge = f"{valLarge}^1"
        facts.append(printLarge)
    else:
        filler = 1
    
# ---------formatting output and then returning---------  
    
    output_str = f"{input_num} = "
    for i in facts:
        output_str += str(i) + " + "
    output_str = output_str[0:-3]    
    
    if ((len(uniques)) == 1 or input_num == 2 or input_num == 1):
        return(f"{input_num} cannot be factored.")
    else:
        return(output_str)

# ---------------- test factorization -----------------------

def test_fact(num, expected):
    
    input_num = num
    uniques = []
    
    if num > 1:
        input_num = num
        # even numbers
        while num % 2 == 0:
            uniques.append(2)
            num = num // 2
            
        # catches everything else after even numbers
        for i in range(3, input_num, 2):
            while (num % i == 0):
                uniques.append(i)
                num = num // i
        uniques.append(num) # this grabs left over factors.
        
        for i in range(len(uniques)):
            if uniques[i] == 1:
                del uniques[i]
                
                
        if input_num == 2:
            prime_status = 'prime'
                
        if uniques[-1] == input_num:
            prime_status = 'prime'
        else:
            prime_status = 'unique factors'               
    else:
        prime_status = 'invalid'
            
    
    if expected == prime_status:
        return 1
    else:
        return 0
 

# ---------------- coprime --------------------

def coprime(num1, num2):
    
    if num1 == 'num1' and num2 == 'num2':
        num1 = int(input("First integer: "))
        num2 = int(input("Second integer: "))
    common_divs = []
    
    if num1 < 1 or num2 < 1:
        print("Invalid input, please try again.")
        num1 = int(input("First integer: "))
        num2 = int(input("Second integer: "))        
    
    if num1 > num2:
        num1, num2 = num2, num1
        
    num1divs = []
    num2divs = []
    
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            num1divs.append(i)
            
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            num2divs.append(i)    
            
    len_longer = len(num1divs)
    len_shorter = len(num2divs)
    
    if len_shorter > len_longer:
        len_longer, len_shorter = len_shorter, len_longer    
    
    
    count = 0
    while (count < len_longer):
        for i in range(len_shorter):
            if num1divs[i] == num2divs[count]:
                common_divs.append(num2divs[count])
        count += 1
    
    if (len(common_divs) == 1 and common_divs[0] == 1):
        return(f"\nYes, {num1} and {num2} are coprime.")
    else: 
        return(f"\nNo, {num1} and {num2} are not coprime.\n They share this list of common divisors: {common_divs}.")

# ----------------- test coprime ------------------

def test_coprime(num1, num2, expected):
    common_divs = [1]
    coprime = ''
    
    if num1 > num2:
        num1, num2 = num2, num1
        
    num1divs = []
    num2divs = []
    
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            num1divs.append(i)
            
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            num2divs.append(i)    
            
    len_longer = len(num1divs)
    len_shorter = len(num2divs)
    
    if len_shorter > len_longer:
        len_longer, len_shorter = len_shorter, len_longer    
     
    count = 0
    while (count < len_longer):
        for i in range(len_shorter):
            if num1divs[i] == num2divs[count]:
                common_divs.append(num2divs[count])
        count += 1
    
    if (num1 < 1 or num2 < 1):
        coprime = 'invalid'
    elif common_divs[-1] == 1:
        coprime = 'coprime'
    else:
        coprime = 'not coprime'
    
        
    if expected == coprime:
        return 1
    else:
        return 0


# ---------------------lcm-----------------------

def lcm(num1, num2):

    if num1 == 'num1' and num2 == 'num2':
        num1 = int(input("First integer: "))
        num2 = int(input("Second integer: "))
    
    if num1 < 1 or num2 < 1:
        print("Invalid input, please try again.")
        num1 = int(input("First integer: "))
        num2 = int(input("Second integer: "))      

    if num1 > num2:
        num1, num2 = num2, num1
    
    num1factors = []
    num2factors = []
    factors = []
    
    for i in range(num1, (num1 * num2) + 1 , num1):
        num1factors.append(i)
    for i in range(num2, (num1 * num2) + 1, num2):
        num2factors.append(i)   
        
    len_longer = len(num1factors)
    len_shorter = len(num2factors)
        
    if len_shorter > len_longer:
        len_longer, len_shorter = len_shorter, len_longer        
    
    count = 0
    while (count < len_shorter):
        for i in range(len_longer):
            if num1factors[i] == num2factors[count]:
                factors.append(num1factors[i])
        count += 1
        
    return (f"The least commonummultiple of {num1} and {num2} is {factors[0]}.")

# ---------------------- test lcm -----------------------

def test_lcm(num1, num2, expected):
    
    input_num1 = num1
    input_num2 = num2
    
    if num1 > num2:
        num1, num2 = num2, num1
    
    invalid = 'empty'
    num1range = 1
    num1factors = []
    num2factors = []
    factors = []
    
    if num1 == 0:
        num1 = 1
        
    if num2 == 0:
        num2 = 1
        
    for i in range(num1, (num1 * num2) + 1 , num1):
        num1factors.append(i)
    for i in range(num2, (num1 * num2) + 1, num2):
        num2factors.append(i)  
        
    len_longer = len(num1factors)
    len_shorter = len(num2factors)
        
    if len_shorter > len_longer:
        len_longer, len_shorter = len_shorter, len_longer        
    
    count = 0
    while (count < len_shorter):
        for i in range(len_longer):
            if num1factors[i] == num2factors[count]:
                factors.append(num1factors[i])
        count += 1
        
    if input_num1 < 1 or input_num2 < 1:
        factors.append('invalid')
    else:
        invalid = "continue"
    
    if expected == factors[0]:
        return 1
    elif input_num1 == 0 and input_num2 == 0 and expected == 'invalid':
        return 1
    else:
        return 0
 
#------------------------unit test---------------------

def unit_test():
    '''the return value for the test functions, if passed, are 1
       and if failed, 0. This means the sum should equal the length
       of the sum list and if not, the test fails. '''
    # coprime = 1
    
    sum = []
    
    sum.append(test_fact(71, 'prime'))
    sum.append(test_fact(-1, 'invalid'))
    sum.append(test_fact(3, 'prime'))
    sum.append(test_fact(2, 'prime'))
    sum.append(test_fact(0, 'invalid'))
    sum.append(test_fact(56, 'unique factors'))
     
    sum.append(test_coprime(85, 17, 'not coprime'))
    sum.append(test_coprime(12, 11, 'coprime'))
    sum.append(test_coprime(8, 0, 'invalid'))
    sum.append(test_coprime(100, -1, 'invalid'))    
    sum.append(test_coprime(17, 13, 'coprime'))
    sum.append(test_coprime(20, 8, 'not coprime'))
    
    sum.append(test_lcm(-1, -2, 'invalid'))
    sum.append(test_lcm(4, 15, 60))
    sum.append(test_lcm(2, 6, 6))
    sum.append(test_lcm(0, -20, 'invalid'))
    sum.append(test_lcm(0, 0, 'invalid'))
    sum.append(test_lcm(5, 9, 45))
    sum.append(test_lcm(3, 4, 12))
    
    sub_sum = 0
    for i in range(len(sum)):
        sub_sum = sum[i] + sub_sum

    if len(sum) ==  sub_sum:
        return f"\nAll tests passed."
    else:
        return f"\nFailed!"
            
# --------------------------------------

def main():
    print(unit_test())
    greeter()
    return ''
    
main()