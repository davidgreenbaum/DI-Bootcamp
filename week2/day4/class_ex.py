# Exercise

# 1st function - get_price_car
# receive the age of the user 
# and if the user is > 40
#     --> 200
# if the user is < 40
#     --> 300

# 2nd function - get_price_flight
# receive a destination from the user
# if the destinatation is Paris
#     --> 400
# if the destinatation is Paris
#     --> 600

# 3rd function
# is going to use the result from the 2 functions above
# and inform the user of the total price of the vacation


def car_price_calc (age):
    if age > 40 :
        return 200
    else:
        return 300
        
    


def flight_calc (dest):
    if dest == "Paris" :
        return 400
    else :
        return 600

flight_calc (dest)

def inform_user_vacation () :
    price_car = get_price_car(45)
    flight_price = get_flight_price("NY")
    total = price_car + flight_price
    print(f"your vacation will cost {total}")
