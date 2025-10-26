a = 12
b = 10
c = 0

if a and b and c :
    print("All the variables are true values.")
else :
    print("At least one value is a false value.")
    
a = 10
b = -10
c = 0

if (a > 0) or (b > 0) : 
    print("That either of the numbers are greater than 0.")
else :
    print("None of the values are positive.")
    
if (b > 0) or (c > 0) :
    print("That either of the numbers are greater than 0.")
else : 
    print("None of the valuse are positive.")
    
if a!=10 and b!=3 : 
    print("Both conditions are true.")
    
d = int(input("Enter a number : "))

if d%2 == 0 :
    print("That number is even.")
else :
    print("Number is odd.") 