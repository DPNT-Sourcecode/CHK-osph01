
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

OFFERS = {
    "A": (3, 130),
    "B": (2, 45)
}

def convert_skus_to_useful(skus):
    out = {}

    for item in skus:
        out[item] = out.get(item, 0) + 1

    return out

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_map = convert_skus_to_useful(skus)
    print(sku_map)
    price = 0
    
    for item in sku_map:
        print(f"PRICE BEFORE ITEM {item} {price}")
        num_item = sku_map[item]
        price = PRICES.get(item)
        print(f"ITEM {item} NUM {num_item} PRICE {price}")
        if not price:
            return -1

        offer = OFFERS.get(item)
        print(f"OFFER {offer}")

        if offer:
            bundle_num, new_price = offer
            num_offer_claimed, num_item = divmod(num_item, bundle_num)
            print(f"NUM OFFER {num_offer_claimed} NUM ITEM {num_item}")
            price += num_offer_claimed * new_price
            print(f"PRICE AFTER OFFER {price}")

        price += num_item * price
        print(f"PRICE AFTER REM ITEMS {price}")

    print(f"FINAL PRICE {price}")

    return price
