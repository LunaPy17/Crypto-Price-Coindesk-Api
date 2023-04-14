from flask import Flask  # Importing Flask to create web application
from requests import get  # Importing get method from requests module to make HTTP requests
from datetime import datetime  # Importing datetime module to work with date and time

app = Flask(__name__) # Creating an instance of Flask class, '__name__' is the name of the current module

def get_coin_price(coin):  # Defining a function to get price data of a coin
    url = f"https://production.api.coindesk.com/v2/tb/price/ticker?assets={coin}"  # URL to get price data of a coin from API
    response = get(url)  # Making an HTTP GET request to the API
    if response.status_code != 200:  # If the response status code is not 200 (OK)
        return None  # Return None
    data = response.json()["data"][coin]  # Extracting price data of the requested coin from the API response
    name = data["name"]  # Extracting name of the coin from the price data
    price = round(data["ohlc"]["c"], 2)  # Extracting the current price of the coin from the price data and rounding it to 2 decimal places
    percent = round(data["change"]["percent"], 2)  # Extracting the percentage change of the coin's price from the price data and rounding it to 2 decimal places
    change_value = round(data["change"]["value"], 2)  # Extracting the change in value of the coin's price from the price data and rounding it to 2 decimal places
    timestamp = int(str(data["ts"])[:-3])  # Extracting the timestamp of the price data and converting it to integer
    date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')  # Converting the timestamp to date and time in a specific format
    return {"coinName": name, "price": f"${price}", "percentChange": f"{percent}%", "changeValue": f"${change_value}", "date": date}  # Returning the coin name, current price, percentage change, change in value, and date in a dictionary format

@app.route("/price/<coin>")  # A decorator that binds a URL to a function, to get price data of a coin
def get_price(coin):  # Defining a function to get price data of a coin
    coin = coin.upper()  # Converting the coin symbol to uppercase
    coin_data = get_coin_price(coin)  # Getting price data of the coin
    if coin_data is None: 
        return {"success": False, "message": f"Coin '{coin}' not found."}, 404  # Return a JSON response with success=False and message that the coin was not found, along with a 404 status code (Not Found)
    return {"success": True, "data": coin_data} # Return a JSON response with success=True and the coin price data

@app.route("/") # A decorator that binds a URL to a function, to display a welcome message
def welcome():
    with open("cDesk\welcome.html", "r") as html: # Opening a HTML file and reading its content
        return html.read()

if __name__ == '__main__': # If the current script is being run as the main program
    app.run(host="0.0.0.0") # Start the Flask application with the IP address of the host set to 0.0.0.0 (accessible from any network interface)
