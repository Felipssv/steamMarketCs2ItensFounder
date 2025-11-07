from steam_api import get_item_price, search_itens

def main():
    print("===== Steam Market Item Price Fetcher =====")
    user_input = input("Enter the name of the item: ")

    print("Looking for itens...")
    try:
        results = search_itens(appid=730, query=user_input)
    except Exception as e:
        print(f"Error searching for items: {e}")
        return

    if not results:
        print("No items found matching your query.")
        return


    print("Items found:")
    for i, item in enumerate(results, start=1):
        print(f"{i}. {item['name']} — {item['price']}")

    choice = int(input("Select an item by number: "))
    try:
       choice = int(choice)
       item_name = results[choice - 1]['name']
    except (ValueError, IndexError):
        print(f"Error: Invalid selection '{choice}'.")
        return

    print(f"Fetching price for '{item_name}'...")
    try:
        result = get_item_price(appid=730, item_name=item_name)
    except Exception as e:
        print(f"Error fetching item price: {e}")
        return
    
    print("===== Item Price Details =====")
    print(f"Lowest Price: {result['lowest_price']}")
    print(f"Median Price: {result['median_price']}")
    print(f"Volume: {result['volume']}")


if __name__ == "__main__":
    main()