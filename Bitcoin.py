import requests
import csv

response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
bitcoin_price = response.json()["bitcoin"]["usd"]
timestamp = response.headers['date']

with open("bitcoin_price.txt", "w") as txt_file:
    
    txt_file.write(f"Precio de Bitcoin (USD): {bitcoin_price}\n")

print("Datos almacenados en bitcoin_price.txt")

csv_data = [{"Precio (USD)": bitcoin_price}]
csv_file = "bitcoin_price.csv"
csv_columns = ["Precio (USD)"]

with open(csv_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(csv_data)

print("Datos almacenados del precio del bitcoin")