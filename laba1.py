import requests

print(f'Актуальная цена BTC: {round(float((requests.get("https://blockchain.info/ticker")).json()["USD"]["sell"]))}$')
