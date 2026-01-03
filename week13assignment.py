import requests
def user_ask():
    country = input("Which coumtry do you need inform about? ")
    t = country.strip()
    return t
def country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()[0]
            return data
        elif response.status_code == 404:
            print("Not FOUND")
            return None
        else:
            print(f"Wrong server: {response.status_code}")
            return None
    except requests.exceptions.RequestException:
        print("Error with internet connection")
        return None
def country_data(country):
    if not country:
        return
    name = country["name"]["common"]
    capital = country.get("capital", ["Unknown"])[0]
    region = country.get("region", "Unknown")
    population = country.get("population", "Unknown")
    currencies = country.get("currencies")
    if currencies:
        currency = []
        for code, info in currencies.items():
            currency.append(f"{code} ({info.get('name', 'Unknown')})")
            str_currency = ", ".join(currency)
    else:
        str_currency = "Unknown"
    print("Information about the State: ")
    print("Name: ", name)
    print("Capital: ", capital)
    print("Region: ", region)
    print("Population: ", population)
    print("Currency: ", str_currency)
def main():
    country_name = user_ask()
    data = country_info(country_name)
    country_data(data)
main()
