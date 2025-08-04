from datetime import datetime

def calculate_fare(pickup_stop, dropoff_stop):
    """
    calculate the fare to pay depending on  location

    and the time of the day
    """

    route = pickup_stop.route


    # Determine the first and last stops of the route by sorting the the route which 
    # is an integer given to identify the route from source to destination
    first_stop_on_route = route.stops.order_by('order').first()
    last_stop_on_route = route.stops.order_by('order').last()

    # check if its a full journey
    # example: path_to_destination = nairobi -> thika,
    # path_from_destination thika -> nairobi
    path_to_destination = (pickup_stop == first_stop_on_route) and (dropoff_stop == last_stop_on_route)
    path_from_destination = (pickup_stop == last_stop_on_route) and (dropoff_stop == first_stop_on_route)
    # A full journey can be either to and from
    is_full_journey = path_from_destination or path_to_destination


    # check for peak hours (7-9am and 4-7pm)
    # start by finding out what is the time now
    now = datetime.now().time()
    is_peak_hour = (datetime.strptime("07:00", "%H:%M").time() <= now <= datetime.strptime("09:00", "%H:%M").time()) or \
            (datetime.strptime("16:00", "%H:%M").time() <= now <= datetime.strptime("19:00", "%H    :%M").time())

    # apply the fare rules
    # only pay 100 if its a full journey on peak hours
    # pay 80 bob for any other stop durring peak hours
    # pay 80 for a full journey on off-peak hours 

    if is_peak_hour:
        return 100 if is_full_journey else 80
    else:
        return 80 if is_full_journey else 50
    #base_fare = 100 # this is in KES

    #if is_peak_hour:
     #   return base_fare
    #else:
    #    return base_fare * 0.5
