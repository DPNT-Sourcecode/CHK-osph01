
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

BUNDLE_OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)]
}

def sku_ordering(sku_map):
    keys = sku_map.keys
    if "E" in keys:
        keys.remove("E")
        keys.insert(0, "E")
    
    return keys

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
    
    for item in sku_ordering(sku_map):
        num_item = sku_map[item]
        item_price = PRICES.get(item)
        if not item_price:
            return -1

        offers = BUNDLE_OFFERS.get(item)

        if offers:
            for offer in offers:
                bundle_num, new_price = offer
                num_offer_claimed, num_item = divmod(num_item, bundle_num)
                price += num_offer_claimed * new_price

        price += num_item * item_price

    return price


