import requests
from flight_data import FlightData

class FlightSearch(FlightData):
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        super().__init__()
        self.header = {"Authorization": f"Bearer {self.amadeus_token}"}
        self.flight_offer_params = {}

    def cheapest_flight(self, **kwargs):
        flight_offer_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        origin = kwargs.get("origin", "LOS")  # Default to LOS if not provided
        destination = kwargs.get("destination_iata")
        departure_date = kwargs.get("date")
        max_price = kwargs.get("price", 1000)

        self.flight_offer_params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "adults": 1,
            # "maxPrice": max_price
        }

        try:
            response = requests.get(url=flight_offer_url, params=self.flight_offer_params, headers=self.header)
            response.raise_for_status()  # Raises an error for HTTP errors (4xx, 5xx)
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
