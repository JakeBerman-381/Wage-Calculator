full_hrs = None
hrs_worked = input("Did you fulfill your 40 hours for the week? ")

# function used to check if full work week fulfilled
def reg_hrs():
    if hrs_worked is "Yes":
        full_hrs = 40
    if hrs_worked is "No":
        full_hrs = input("How many hours did you work? ")

        
        
    else:
        full_hrs = input()
