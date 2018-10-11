# Imports date and time
import datetime

#Current date and time
# Declare variable
today = datetime.datetime.today()
dayofweek = today.weekday()

print("Let's check it it's Tuesday")
if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday")
else:
    print("Unfortuanetly, it's not Tuesday")

print("Thanks for checking f it's Tuesday")