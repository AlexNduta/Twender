from datetime import datetime

def calculate_fare(pickup_location, drop_off_location):
    """
    calculate the fare to pay depending on the time of the day
    """

    now = datetime.now().time()

    # peak hours (7-9am and 4-7pm)
    is_peak_hour = (datetime.strptime("07:00", "%H:%M").time() <= now <= datetime.strptime("09:00", "%H:%M").time()) or \
            (datetime.strptime("16:00", "%H:%M").time() <= now <= datetime.strptime("19:00", "%H    :%M").time()) 


    base_fare = 100 # this is in KES

    if is_peak_hour:
        return base_fare
    else:
        return base_fare * 0.5
