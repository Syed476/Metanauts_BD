
import requests
def get_data():


	url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US"

	headers = {
    	'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
    	'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
    	}

	response = requests.request("GET", url, headers=headers)
	result= response.json()
	return result


if  __name__ == "__main__":
   
	get_data()


