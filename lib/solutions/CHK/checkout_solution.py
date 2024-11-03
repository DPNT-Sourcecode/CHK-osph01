
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
    price = 0
    
    for item in sku_map:
        num_item = sku_map[item]
        item_price = PRICES.get(item)
        if not item_price:
            return -1

        offer = OFFERS.get(item)

        if offer:
            bundle_num, new_price = offer
            num_offer_claimed, num_item = divmod(num_item, bundle_num)
            price += num_offer_claimed * new_price

        price += num_item * item_price

    return price
