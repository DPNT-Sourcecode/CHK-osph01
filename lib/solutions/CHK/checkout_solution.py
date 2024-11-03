
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
    {}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    ## TODO: find out format of skus input
    ##       turn into map of items needed
    ##       if any unknown items then return -1
    ##       (suspected stock check in next few rounds)
    ##       have knowledge of prices
    ##       use map of sales to work out total price (divmod)

    sku_map = convert_skus_to_useful(skus)
    price = 0
    
    for item in sku_map:
        num_item = sku_map[item]
        price = PRICES.get(item)

        if not price:
            return -1

        offer = OFFERS.get(item)

        if offer:
            bundle_num, new_price = offer
            num_offer_claimed, num_item = divmod(num_item, bundle_num)
            

    return price

