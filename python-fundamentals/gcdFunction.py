# Function with two arguments
def gcd(a, b):
    """ Returns the greatest common divisor of a and b """



    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b

        return a

print(gcd(50, 20))
print(gcd(22, 143))

    
    #LCM with two numbers 
   
def lcm(a, b):
   if a > b:
       a, b = b, a
       for x in range(b, a * b + 1, b):
        if x % a == 0:
           return x
print(lcm(2, 4))   




