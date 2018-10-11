#Greatest common divisor
a = 50
b = 20

while b > 0:
    #store temporary value
    a, b = b, a % b
    # overwrite value of a
   # a = b
   # b = tmp % b

    print(a)

  