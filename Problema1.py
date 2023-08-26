import requests

def bitcoinprecio():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print("Error making API request:", e)
        return None

try:
     n_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
except ValueError:
    print("Cantidad inválida.")

bitcoin_p = bitcoinprecio()

if bitcoin_p is not None:
    total_value_usd = n_bitcoins * bitcoin_p
    print(f"El valor actual de {n_bitcoins:.4f} bitcoins es ${total_value_usd:,.4f} USD.")
