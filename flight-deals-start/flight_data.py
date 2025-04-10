import requests


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        amadeus_api = "LQC9M8AYhKLSmCQSuGh2uTnJ7cOZAHsW"
        amadeus_secret = "iUoUzUagrNDwxAQq"
        amadeus_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        amadeus_params = {
            "grant_type": "client_credentials",
            "client_id": amadeus_api,
            "client_secret": amadeus_secret
        }
        amadeus_response = requests.post(url=amadeus_endpoint, data=amadeus_params, headers={
            "Content-Type":
                "application/x-www-form-urlencoded"
        })

        amadeus_data = amadeus_response.json()
        self.amadeus_token = amadeus_data["access_token"]
        self.iata_code = ''
        self.header = {"Authorization": f"Bearer {self.amadeus_token}"}

    def data_finder(self, location):
        url2_params = {
            'keyword': location,
        }
        url2 = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        response = requests.get(url=url2, params=url2_params, headers=self.header)
        data = response.json()
        exact_match = [city for city in data.get("data", []) if city["name"].lower() == location.lower()]
        if exact_match:
            self.iata_code = exact_match[0]["iataCode"]

        else:
            self.iata_code = data['data'][0]['iataCode']

        return self.iata_code



