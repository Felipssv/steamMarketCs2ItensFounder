import requests
import urllib.parse

def get_item_price(appid: int, item_name: str, currency: int = 7):

    base_url = "https://steamcommunity.com/market/priceoverview/"
    encoded_item = urllib.parse.quote(item_name)
    
    url = f"{base_url}?appid={appid}&currency={currency}&market_hash_name={encoded_item}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if not data.get("success"):
        raise ValueError("Item not found or API request failed.")
    
    return {
        "lowest_price": data.get("lowest_price"),
        "median_price": data.get("median_price"),
        "volume": data.get("volume")
    }

def search_itens(appid: int, query: str, count: int = 5):
    base_url = "https://steamcommunity.com/market/search/render/"
    params = {
        "appid": appid,
        "norender": 1,
        "count": count,
        "query": query
        
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    results = data.get("results", [])
    items = []

    for r in results:
        name = r.get("hash_name")
        sell_price = r.get("sell_price_text", "Sold Out")

        if name:
            items.append({
                "name": name,
                "price": sell_price
            })
    return items
  