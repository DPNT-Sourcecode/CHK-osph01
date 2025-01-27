
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
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21
}

BUNDLE_OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "F": [(3, 20)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 120)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "U": [(4, 120)],
    "V": [(3, 130), (2, 90)] 
}

def apply_group_offers(sku_map):
    ## Group1: (S, T, X, Y, Z)
    num_s = sku_map.get("S", 0)
    num_t = sku_map.get("T", 0)
    num_x = sku_map.get("X", 0)
    num_y = sku_map.get("Y", 0)
    num_z = sku_map.get("Z", 0)

    group1_total = num_s + num_t + num_x + num_y + num_z
    additional_price = 0
    
    if group1_total >= 3:
        ## Number of group1s is the amount of times the offer applies
        ## Remaining group1s are to be take off the total amount to leave us with the amount accounted for by offers
        num_group1s, remaining_group1s = divmod(group1_total, 3)
        group1_total -= remaining_group1s

        additional_price = num_group1s * 45
        ## Order Z, Y, S, T, X so that expensive is taken off first, as that favours the customer
        
        if num_z > 0:
            num_to_take = min(num_z, group1_total)
            group1_total -= num_to_take
            sku_map["Z"] -= num_to_take

        if num_y > 0:
            num_to_take = min(num_y, group1_total)
            group1_total -= num_to_take
            sku_map["Y"] -= num_to_take

        if num_s > 0:
            num_to_take = min(num_s, group1_total)
            group1_total -= num_to_take
            sku_map["S"] -= num_to_take

        if num_t > 0:
            num_to_take = min(num_t, group1_total)
            group1_total -= num_to_take
            sku_map["T"] -= num_to_take

        if num_x > 0:
            num_to_take = min(num_x, group1_total)
            group1_total -= num_to_take
            sku_map["X"] -= num_to_take

    return additional_price

def apply_bonus_offers(item, num_item, sku_map):
    ## If we have Es in the basket then we can take away Bs
    if item == "E" and "B" in sku_map:
        ## For each 2 Es we can take a B
        num_bs_rem = num_item // 2
        ## Make sure if 2 Es are bought but no Bs are that we don't give store credit
        sku_map["B"] = max(sku_map["B"] - num_bs_rem, 0)

    ## If we have Ns in the basket then we can take away Ms
    if item == "N" and "M" in sku_map:
        ## For each 3 Ns we can take a M
        num_ms_rem = num_item // 3
        ## Make sure if 3 Ns are bought but no Ms are that we don't give store credit
        sku_map["M"] = max(sku_map["M"] - num_ms_rem, 0)
    
    ## If we have Rs in the basket then we can take away Qs
    if item == "R" and "Q" in sku_map:
        ## For each 3 Rs we can take a Q
        num_qs_rem = num_item // 3
        ## Make sure if 3 Rs are bought but no Qs are that we don't give store credit
        sku_map["Q"] = max(sku_map["Q"] - num_qs_rem, 0)

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
    price = apply_group_offers(sku_map)
    
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
