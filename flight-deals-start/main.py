from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

flight_data = FlightData()
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve
# the
# program requirements.
start_date = datetime.today() + timedelta(days=1)
end_date = start_date + timedelta(days=180)  # Approx. 6 months


table = data_manager.data['prices']
print(table)

for row in table:
    destination = row['iataCode']
    # max_price = row['lowestPrice']
    for i in range((end_date - start_date).days + 1):
        date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
        print(date)
        cheap_flight = flight_search.cheapest_flight(destination_iata=destination, date=date, )   #price=max_price
        if not cheap_flight or "error" in cheap_flight:
            print(f"Error fetching flights: {cheap_flight.get('error', 'Unknown error')}")
        else:
            print(f"Flight found: {cheap_flight}")