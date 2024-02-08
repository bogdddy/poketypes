import itertools
from type_chart import *

def get_x4_weak():
    """
    Returns an array of all combinations of x4 weakness and the type its weak to
    [[(type1, type2), opp_type], ...]
    """

    #all possible combinations of types
    all_combinations = list(itertools.combinations(TYPES, 2))

    all_x4_weakness = []

    for type in TYPES:
        for comb in all_combinations:
            
            att = TYPES.index(type)
            opp1 = TYPES.index(comb[0])
            opp2 = TYPES.index(comb[1])
            
            if type_chart[att][opp1]*type_chart[att][opp2] == 4:
                all_x4_weakness.append([comb, type])

    return all_x4_weakness

def get_double_x4_weak():
    """
    Returns a dict of all type combinations that are weak against 1+ types
    [[(type1, type2), [weak1, weak2]], ...]
    """
    
    x4_weak_count = {}
    x4_weak = get_x4_weak()

    #count number of weaknesses of type comb.
    for w in x4_weak:
        type_comb = w[0]
        opp_attck = w[1]

        if type_comb not in x4_weak_count: 
            x4_weak_count[type_comb] = [opp_attck]
        else:
            x4_weak_count[type_comb].append(opp_attck)

    # get only type comb weak > 1
    double_x4_weak = {key: value for key, value in x4_weak_count.items() if len(value) > 1}

    return double_x4_weak

# print results
for comb, weak in get_double_x4_weak().items():
    print(comb, weak)