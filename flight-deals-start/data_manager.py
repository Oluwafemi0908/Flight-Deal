import requests
from flight_data import FlightData

flight_data = FlightData()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        bearer_headers = {"Authorization": f"Bearer hharevvx246873"}
        flight_info = flight_data.data_finder("Lagos")

        self.url = "https://api.sheety.co/df3797fff716dd2337a79ceb1838a4b2/flightDeals/prices"

        self.response = requests.get(url=self.url, headers=bearer_headers)
        self.data = self.response.json()
        print(self.data)
        for location in self.data['prices']:
            iata_url = f"https://api.sheety.co/df3797fff716dd2337a79ceb1838a4b2/flightDeals/prices/{location['id']}"
            iata = flight_data.data_finder(location['city'])
            params = {
                'price': {
                    'iataCode': iata
                }
            }
            iata_put = requests.put(url=iata_url, json=params, headers=bearer_headers)

x = DataManager()
