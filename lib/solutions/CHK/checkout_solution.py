
PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50
}

BUNDLE_OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "F": [(3, 20)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 150)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "U": [(4, 120)],
    "V": [(3, 130), (2, 90)] 
}

def apply_bonus_offers(item, num_item, sku_map):
    ## If we have Es in the basket then we can take away Bs
    if item == "E" and "B" in sku_map:
        ## For each 2 Es we can take a B
        num_bs_rem = num_item // 2
        ## Make sure if 2 Es are bought but no Bs are that we don't give store credit
        sku_map["B"] = max(sku_map["B"] - num_bs_rem, 0)

    ## If we have Ns in the basket then we can take away Ms
    if item == "N" and "M" in sku_map:
        ## For each 3 Ns we can take a B
        num_bs_rem = num_item // 2
        ## Make sure if 2 Es are bought but no Bs are that we don't give store credit
        sku_map["B"] = max(sku_map["B"] - num_bs_rem, 0)

def sku_ordering(sku_map):
    sku_keys = list(sku_map.keys())
    
    ## Allow us to test Es first so that we can remove Bs before their prices are added
    if "E" in sku_keys:
        sku_keys.remove("E")
        sku_keys.insert(0, "E")

    ## Allow us to test Ns first so that we can remove Ms before their prices are added    
    if "N" in sku_keys:
        sku_keys.remove("N")
        sku_keys.insert(0, "N")

    ## Allow us to test Rs first so that we can remove Qs before their prices are added
    if "R" in sku_keys:
        sku_keys.remove("R")
        sku_keys.insert(0, "R")

    return sku_keys

def convert_skus_to_map(skus):
    out = {}

    for item in skus:
        out[item] = out.get(item, 0) + 1

    return out

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_map = convert_skus_to_map(skus)
    price = 0
    
    ## Iterate through each item type bought
    for item in sku_ordering(sku_map):
        num_item = sku_map[item]
        item_price = PRICES.get(item)

        ## If we don't recognise an item then return -1
        if not item_price:
            return -1

        apply_bonus_offers(item, num_item, sku_map)

        offers = BUNDLE_OFFERS.get(item)

        ## If we have bundle offers then for each offer check if it applies
        ## and then apply it
        if offers:
            for offer in offers:
                bundle_num, new_price = offer
                num_offer_claimed, num_item = divmod(num_item, bundle_num)
                price += num_offer_claimed * new_price

        price += num_item * item_price

    return price


