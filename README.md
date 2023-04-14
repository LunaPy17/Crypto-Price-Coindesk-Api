Crypto-Price-Coindesk-Api
[![CodeFactor](https://www.codefactor.io/repository/github/lunapy17/crypto-price-coindesk-api/badge/main)](https://www.codefactor.io/repository/github/lunapy17/crypto-price-coindesk-api/overview/main)
=======


This is a simple Flask-based API that provides the current price, percentage change, and change in value of a given cryptocurrency. It retrieves data from the Coindesk API and returns it in a JSON format.

# Requirements

* Python 3.x
* Flask
* Requests

# Installation

1. Clone the repository: git clone https://github.com/LunaPy17/Crypto-Price-Coindesk-Api.git
2. Install the required packages: pip install -r requirements.txt

# Usage

To run the application, execute the following command in your terminal:

```
python app.py
```

This will start the Flask application on your local machine. You can access the API at http://localhost:5000.

# EndPoints

`/price/<coin>`

Returns the current price, percentage change, and change in value of the specified coin. The endpoint accepts a single parameter, which is the coin symbol (e.g., "BTC").

If the coin symbol is not valid, the API will return a JSON response with success=False and a message that the coin was not found, along with a 404 status code (Not Found).

Example response for `/price/BTC`:

```json
{
  "success": true,
  "data": {
    "coinName": "Bitcoin",
    "price": "$57,103.04",
    "percentChange": "-0.23%",
    "changeValue": "$-128.49",
    "date": "2023-04-14 07:25:34"
  }
}
```

`/`

Displays a welcome message in HTML format. 🌹

# License

This project is licensed under the GPL-3.0 [License](https://github.com/LunaPy17/Crypto-Price-Coindesk-Api/blob/main/LICENSE). See the LICENSE file for details.
