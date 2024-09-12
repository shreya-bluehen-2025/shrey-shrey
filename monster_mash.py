#################################################
# Do not modify this section
# You must place 'monster_mash.json' in the same
# directory as this file.
from cisc108 import assert_equal
import json

with open('monster_mash.json') as data_file:
    MONSTER_MASH = json.load(data_file)

#################################################

'''
A Party is a dictionary with four fields:
* "type": The type of party that it is
* "werewolves": The number of werewolves in attendance
* "vampires": The number of vampires in attendance
* "witches": The number of witches in attendance
'''

Party = {"werewolves": int, "vampires": int, "witches": int,
         "type": str}

'''
P1. Define a function `sum_guests` that consumes a Party and
produces an integer representing the total number of
guests attending (including werewolves, vampires, and witches).
'''

def sum_guests(party: Party) -> int:
    
    '''
    This function adds up all the guests at the party.
    
    Args:
    party (Party): A dictionary is taken for this function.
    
    Returns:
    int: The total number of guests is returned.
    '''
    
    werewolves = party['werewolves']
    vampires = party['vampires']
    witches = party['witches']
    return werewolves + vampires + witches

assert_equal(sum_guests(MONSTER_MASH['party 1']), 20)
assert_equal(sum_guests(MONSTER_MASH['party 2']), 25)
assert_equal(sum_guests(MONSTER_MASH['party 3']), 19)
assert_equal(sum_guests(MONSTER_MASH['party 4']), 33)
assert_equal(sum_guests(MONSTER_MASH['party 5']), 50)

'''
P2. Define a function `were_only_werewolves` that consumes a Party and
produces a boolean indicating whether or not the only guests were
werewolves.
'''

def were_only_werewolves(party: Party) -> bool:
    
    '''
    This function checks if all the guests are werewolves.
    
    Args:
    party (Party): A dictionary is taken for this function.
    
    Returns:
    bool: If all guests are werwolves than True, or else False.
    '''
    
    if party["witches"] != 0 or party["vampires"] != 0:
        return (False)
    else:
        return (True)

assert_equal(were_only_werewolves(MONSTER_MASH['party 1']), True)
assert_equal(were_only_werewolves(MONSTER_MASH['party 2']), False)
assert_equal(were_only_werewolves(MONSTER_MASH['party 3']), False)
assert_equal(were_only_werewolves(MONSTER_MASH['party 4']), True)
assert_equal(were_only_werewolves(MONSTER_MASH['party 5']), False)

'''
P3. Witches and vampires always bring a date, but werewolves prefer to
come to parties alone (because they're lone wolves). Define a function
`total_folks` that consumes a Party and produces an integer representing
the total number of folks who were present.
'''

def total_folks(party: Party) -> int:
    
    '''
    This function adds up all the folks at the party.
    
    Args:
    party (Party): A dictionary is taken for this function.
    
    Returns:
    int: The total number of folks is returned.
    '''
    
    werewolves = party["werewolves"]
    vampires = party["vampires"] * 2
    witches = party["witches"] * 2
    return werewolves + vampires + witches

assert_equal(total_folks(MONSTER_MASH['party 1']), 20)
assert_equal(total_folks(MONSTER_MASH['party 2']), 45)
assert_equal(total_folks(MONSTER_MASH['party 3']), 38)
assert_equal(total_folks(MONSTER_MASH['party 4']), 33)
assert_equal(total_folks(MONSTER_MASH['party 5']), 85)

'''
P4. A "small" party has 20 or fewer guests, a "big" party has 40 or more,
and otherwise the party is "medium". Define a function `check_party_size`
that consumes a Party and produces a string indicating whether the party
is "small", "medium", or "big". Note that we're counting guests, not folks,
so don't include witches' and vampires' dates.
'''

def check_party_size(party: Party) -> str:
    '''
    This function gets size of the party, based on the number of guests.
    
    Args:
    party (Party): A dictionary is taken for this function.
    
    Returns:
    str: The size of the party is returned.
    '''
    
    if sum_guests(party) <= 20:
        return ("small")
    elif sum_guests(party) >= 40:
        return ("big")
    else:
        return("medium")

assert_equal(check_party_size(MONSTER_MASH['party 1']), "small")
assert_equal(check_party_size(MONSTER_MASH['party 2']), "medium")
assert_equal(check_party_size(MONSTER_MASH['party 3']), "small")
assert_equal(check_party_size(MONSTER_MASH['party 4']), "medium")
assert_equal(check_party_size(MONSTER_MASH['party 5']), "big")

'''
P5. If a party has both werewolves and vampires, there should be
more werewolves than vampires. Define a function `check_party_ratio`
that consumes a Party and produces a float indicating the number of
werewolves divided by the number of vampires. If there are no vampires
or no werewolves, produce the value 0.
'''

def check_party_ratio(party: Party) -> float:
    
    '''
    This function checks that ratio between vampires and werewolves.
    
    Args:
    party (Party): A dictionary is taken for this function.
    
    Returns:
    float: The ratio is returned.
    '''
    
    if party["werewolves"] == 0 or party["vampires"] == 0:
        return (0)
    else:
        return party["werewolves"] / party["vampires"]

assert_equal(check_party_ratio(MONSTER_MASH['party 1']), 0)
assert_equal(check_party_ratio(MONSTER_MASH['party 2']), 0.25)
assert_equal(check_party_ratio(MONSTER_MASH['party 3']), 0)
assert_equal(check_party_ratio(MONSTER_MASH['party 4']), 0)
assert_equal(check_party_ratio(MONSTER_MASH['party 5']), 3.0)


'''
A Monster is a dictionary with four fields:
* "name": The name of this particular monster (string)
* "kind": A str representing the type of the monster (e.g., "vampire", "werewolf")
* "spookyiness": An integer from 0-4 indicating its spookiness
* "undead?": A boolean indicating whether or not this monster is undead.
'''

Monster = {"name": str, "kind": str, "spookiness": int, "undead?": bool}

'''
M1. Define a function `count_monsters` that consumes a list of monsters and
produces an integer indicating how many monsters there are.
'''

def count_monsters(monster: Monster) -> int:
    
    '''
    This function counts all the monsters that are there.
    
    Args:
    monster (Monster): A dictionary is taken for this function.
    
    Returns:
    int: The total number of monsters is returned.
    '''
    
    total = 0
    for mons in monster:
        total = total + 1
    return (total)

assert_equal(count_monsters(MONSTER_MASH['monsters 1']), 4)
assert_equal(count_monsters(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_monsters(MONSTER_MASH['monsters 3']), 5)
assert_equal(count_monsters(MONSTER_MASH['monsters 4']), 5)
assert_equal(count_monsters(MONSTER_MASH['monsters 5']), 5)

'''
M2. Define a function `count_undead_monsters` that consumes a list
of monsters and produces an integer indicating how many undead
monsters there are.
'''

def count_undead_monsters(monster: Monster) -> int:
    
    '''
    This function counts all the monsters that are alive.
    
    Args:
    monster (Monster): A dictionary is taken for this function.
    
    Returns:
    int: The total number of alive monsters is returned.
    '''
    
    total = 0
    for mons in monster:
        if mons["undead?"] == True:
            total = total + 1
    return (total)

assert_equal(count_undead_monsters(MONSTER_MASH['monsters 1']), 0)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 3']), 2)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 4']), 4)
assert_equal(count_undead_monsters(MONSTER_MASH['monsters 5']), 3)

'''
M3. Define a function `average_spookiness` that consumes a list of monsters
and produces a float representing their average spookiness. If the list
is empty, produce the special value `None` instead.
'''

def average_spookiness(monster: Monster) -> float:
    
    '''
    This function calculates the average sppokiness of all the monsters.
    
    Args:
    monster (Monster): A dictionary is taken for this function.
    
    Returns:
    float: The average spookiness is returned.
    '''
    
    total = 0
    spookiness = 0
    if monster == []:
        return None
    for mons in monster:
        total = total + 1
        spookiness = spookiness + mons["spookiness"]
    return spookiness / total

assert_equal(average_spookiness(MONSTER_MASH['monsters 1']), 0.0)
assert_equal(average_spookiness(MONSTER_MASH['monsters 2']), 1.0)
assert_equal(average_spookiness(MONSTER_MASH['monsters 3']), 1.8)
assert_equal(average_spookiness(MONSTER_MASH['monsters 4']), 1.6)
assert_equal(average_spookiness(MONSTER_MASH['monsters 5']), 0.4)

'''
M4. Define a function `average_undead_spookiness` that consumes a list of monsters
and produces a float representing the average spookiness of the undead monsters
in the list. If there are no undead monsters, produce the special value `None`
instead.
'''

def average_undead_spookiness(monster: Monster) -> float:
    
    '''
    This function calculates the average spookiness of alive monsters.
    
    Args:
    monster (Monster): A dictionary is taken for this function.
    
    Returns:
    float: The alive spookiness is returned.
    '''
    
    if count_undead_monsters(monster) == 0:
        return None
    spookiness = 0
    for mons in monster:
        if mons["undead?"] == True:
            spookiness = spookiness + mons["spookiness"]
    return spookiness / count_undead_monsters(monster)

assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 1']), None)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 2']), 1.0)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 3']), 1.5)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 4']), 2.0)
assert_equal(average_undead_spookiness(MONSTER_MASH['monsters 5']), 0.6666666666666666)

'''
M5. Define a function `count_spooky_monsters` that consumes a list of monsters
and produces an integer indicating how many monsters have a spookiness of
2 or more.
'''

def count_spooky_monsters(monster: Monster) -> int:
    
    '''
    This function tells us how many monsters have more spookiness than 2.
    
    Args:
    monster (Monster): A dictionary is taken for this function.
    
    Returns:
    int: The number of monsters is returned.
    '''
    
    spookiness = 0
    for mons in monster:
        if mons["spookiness"] >= 2:
            spookiness = spookiness + 1
    return spookiness

assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 1']), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 2']), 0)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 3']), 3)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 4']), 3)
assert_equal(count_spooky_monsters(MONSTER_MASH['monsters 5']), 0)

'''
M6. Define the function `count_vampires` that consumes a list of monsters
and produces an integer indicating how many monsters are of the kind
"vampire".
'''

def count_vampires(monster: Monster) -> int:
    
    '''
    This function count all the vampires.
    
    Args:
    monster (Monster): A dictionary is taken for this function.
    
    Returns:
    int: The total number of vampires.
    '''
    
    total = 0
    for mons in monster:
        if mons["kind"] == "vampire":
            total = total + 1
    return total

assert_equal(count_vampires(MONSTER_MASH['monsters 1']), 0)
assert_equal(count_vampires(MONSTER_MASH['monsters 2']), 4)
assert_equal(count_vampires(MONSTER_MASH['monsters 3']), 0)
assert_equal(count_vampires(MONSTER_MASH['monsters 4']), 0)
assert_equal(count_vampires(MONSTER_MASH['monsters 5']), 2)


## Costumes

'''
A Costume is a dictionary with 3 keys:
* 'label': A string representing the name of the costume.
* 'price': An integer representing the cost of the costume in dollars.
* 'sizes': A list of strings representing the available sizes ('S', 'M', 'L').
'''

Costume = {'label': str, 'price': int, 'sizes': [str]}

'''
C1. Define a function `count_costumes` that consumes a list of costumes
and produces an integer representing the number of costumes in the list.
'''

def count_costumes(costume: Costume) -> int:
    
    '''
    This function totals up all the costumes.
    
    Args:
    costumes (Costume): A dictionary is taken for this function.
    
    Returns:
    int: The total number of costumes is returned.
    '''
    
    costumes = 0
    for cost in costume:
        costumes = costumes + 1
    return costumes 

assert_equal(count_costumes(MONSTER_MASH['costumes 1']), 4)
assert_equal(count_costumes(MONSTER_MASH['costumes 2']), 3)
assert_equal(count_costumes(MONSTER_MASH['costumes 3']), 4)
assert_equal(count_costumes(MONSTER_MASH['costumes 4']), 5)
assert_equal(count_costumes(MONSTER_MASH['costumes 5']), 4)
assert_equal(count_costumes(MONSTER_MASH['costumes 6']), 0)

'''
C2. Define a function `total_price` that consumes a list of costumes
and produces an integer representing the total price of all the
costumes in the list.
'''

def total_price(costume: Costume) -> int:
    
    '''
    This function adds up the total value of all the costumes.
    
    Args:
    costume (Costume): A dictionary is taken for this function.
    
    Returns:
    int: The total price of all the costumes.
    '''
    
    costume_price = 0
    for prices in costume:
        costume_price = prices["price"] + costume_price
    return costume_price

assert_equal(total_price(MONSTER_MASH['costumes 1']), 180)
assert_equal(total_price(MONSTER_MASH['costumes 2']), 105)
assert_equal(total_price(MONSTER_MASH['costumes 3']), 21)
assert_equal(total_price(MONSTER_MASH['costumes 4']), 340)
assert_equal(total_price(MONSTER_MASH['costumes 5']), 120)
assert_equal(total_price(MONSTER_MASH['costumes 6']), 0)

'''
C3. Define a function `count_sizes` that consumes a list of costumes and
produces an integer indicating the total number of sizes that are
available across all the costumes.
'''

def count_sizes(costume: Costume) -> int:
    
    ''''
    This function totals up all the sizes the costumes have.
    
    Args:
    costume (Costume): A dictionary is taken for this function.
    
    Returns:
    int: The total number of sizes.
    '''
    
    sizes = 0
    for cost in costume:
        sizes = len(cost["sizes"]) + sizes
    return sizes
    
assert_equal(count_sizes(MONSTER_MASH['costumes 1']), 9)
assert_equal(count_sizes(MONSTER_MASH['costumes 2']), 0)
assert_equal(count_sizes(MONSTER_MASH['costumes 3']), 12)
assert_equal(count_sizes(MONSTER_MASH['costumes 4']), 9)
assert_equal(count_sizes(MONSTER_MASH['costumes 5']), 4)
assert_equal(count_sizes(MONSTER_MASH['costumes 6']), 0)

'''
C4. Define a function `max_price` that consumes a list of costumes
and produces an integer indicating the price of the most expensive
costume. If there are no costumes in the list, produce the special
value `None`.
'''

def max_price(costume: Costume) -> int:
    
    '''
    This function finds the costume with the most expensive price.
    
    Args:
    costume (Costume): A dictionary is taken for this function.
    
    Returns:
    int: The price of the most expensive costume.
    '''
    
    if costume == []:
        return None
    expensive = 0
    for cost in costume:
        if cost["price"] > expensive:
            expensive = cost["price"]
    return expensive

assert_equal(max_price(MONSTER_MASH['costumes 1']), 90)
assert_equal(max_price(MONSTER_MASH['costumes 2']), 50)
assert_equal(max_price(MONSTER_MASH['costumes 3']), 8)
assert_equal(max_price(MONSTER_MASH['costumes 4']), 80)
assert_equal(max_price(MONSTER_MASH['costumes 5']), 40)
assert_equal(max_price(MONSTER_MASH['costumes 6']), None)

'''
C5. Define a function `most_expensive_costume` that consumes
a list of costumes and produces a string representing the label
of the costume with the highest price. In the event of a tie,
give the label of the item later in the list. If there are no
costumes, return the special value None.
'''

def most_expensive_costume(costume: Costume) -> str:
    
    '''
    This function gets the brand of the most expensive costume.
    
    Args:
    costume (Costume): A dictionary is taken for this function.
    
    Returns:
    str: The brand of the most expensive costume.
    '''

    if costume == []:
        return None
    expensive = 0
    name = ""
    for cost in costume:
        if expensive <= cost["price"]:
            expensive = cost["price"]
            name = cost["label"]
    return name


assert_equal(most_expensive_costume(MONSTER_MASH['costumes 1']), "Pirate Zombie Ghost")
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 2']), "Wardrobe")
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 3']), "Ghost")
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 4']), "Thor")
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 5']), "Rogue")
assert_equal(most_expensive_costume(MONSTER_MASH['costumes 6']), None)

'''
C6. Define a function `find_last_medium` that consumes a list of costumes
and produces the label of the last costume that is available in a medium.
If no medium costumes are found, produce the special value `None`.
'''

def find_last_medium(costume: Costume) -> str:
    
    '''
    This function finds the last brand in the list that has a size medium.
    
    Args:
    costume (Costume): A dictionary is taken for this function.
    
    Returns:
    str: The brand name is returned.
    '''
    
    last_medium = None
    for cost in costume:
        for size in cost["sizes"]:
            if size == "M":
                last_medium = cost["label"]
    return last_medium

assert_equal(find_last_medium(MONSTER_MASH['costumes 1']), "Ghost")
assert_equal(find_last_medium(MONSTER_MASH['costumes 2']), None)
assert_equal(find_last_medium(MONSTER_MASH['costumes 3']), "Ghost")
assert_equal(find_last_medium(MONSTER_MASH['costumes 4']), "Captain America")
assert_equal(find_last_medium(MONSTER_MASH['costumes 5']), "Rogue")
assert_equal(find_last_medium(MONSTER_MASH['costumes 6']), None)

'''
C7. Define a function `find_first_small` that consumes a list of costumes
and produces the label of the first costume that is available in a small.
If no small costumes are found, produce the special value `None`.
'''

def find_first_small(costume: Costume) -> str:
    
    '''
    This function finds the first costume that has a size small.
    
    Args:
    costume (Costume): A dictionary is taken for this function.
    
    Returns:
    str: The brand name is returned.
    '''
    
    if costume == []:
        return None
    for cost in costume:
        if "S" in cost["sizes"]:
            return cost["label"]

assert_equal(find_first_small(MONSTER_MASH['costumes 1']), "Pirate")
assert_equal(find_first_small(MONSTER_MASH['costumes 2']), None)
assert_equal(find_first_small(MONSTER_MASH['costumes 3']), "Mummy")
assert_equal(find_first_small(MONSTER_MASH['costumes 4']), "Spiderman")
assert_equal(find_first_small(MONSTER_MASH['costumes 5']), "Knight")
assert_equal(find_first_small(MONSTER_MASH['costumes 6']), None)


## Tombstones

'''
A Grave is a dictionary with two keys:
* 'Name': A string value with the grave's occupant's name
* 'Message': A string value with the grave's message
'''

Grave = {'name': str, 'Message': str}

'''
G1. Define the function `count_grave_all` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Include spaces and new lines.
'''

def count_grave_all(grave: Grave) -> int:
    
    '''
    This function counts all the charcters for the grave message.
    
    Args:
    grave (Grave): A dictionary is taken for this function.
    
    Returns:
    int: The number of charcters needed is returned.
    '''
    
    length = 0
    for charcter in grave:
        length = length + len(charcter["message"])
    return length 

assert_equal(count_grave_all(MONSTER_MASH['graves 1']), 149)
assert_equal(count_grave_all(MONSTER_MASH['graves 2']), 105)
assert_equal(count_grave_all(MONSTER_MASH['graves 3']), 108)
assert_equal(count_grave_all(MONSTER_MASH['graves 4']), 0)

'''
G2. Define the function `count_grave_characters` that consumes a list of graves
and produces an integer representing the number of characters needed to
write all of the message of the grave. Do not count spaces and new lines.
'''

def count_grave_characters(grave: Grave) -> int:
    
    '''
    This function counts all the charcters excluding space and new lines
    for the grave message.
    
    Args:
    grave (Grave): A dictionary is taken for this function.
    
    Returns:
    int: The number of charcters.
    '''
    
    length = 0
    for character in grave:
        message = character["message"]
        edit_message = message.replace(" ", "")
        final_message = edit_message.replace("\n", "")
        length = length + len(final_message)
    return length

assert_equal(count_grave_characters(MONSTER_MASH['graves 1']), 120)
assert_equal(count_grave_characters(MONSTER_MASH['graves 2']), 90)
assert_equal(count_grave_characters(MONSTER_MASH['graves 3']), 95)
assert_equal(count_grave_characters(MONSTER_MASH['graves 4']), 0)

'''
G3. Define a function named `estimate_grave_cost` that consumes a list of graves
and produces an integer representing the total estimate lettering cost by
multiplying the number of letters on the grave (ignoring spaces and newlines) by
the cost of writing a letter ($2).
'''

def estimate_grave_cost(grave: Grave) -> int:
    
    '''
    This function gets the total cost of the message on the grave.
    
    Args:
    grave (Grave): A dictionary is taken for this function.
    
    Returns:
    int: The total cost of the messages is returned.
    '''
    
    length = count_grave_characters(grave)
    total = length * 2
    return total
    
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 1']), 240)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 2']), 180)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 3']), 190)
assert_equal(estimate_grave_cost(MONSTER_MASH['graves 4']), 0)

"""
G4. Define a function named `count_shouters` that consumes a list of graves
and produces an integer representing the number of graves that had their
messages in all capital letters. Hint: use the `.upper()` method.
"""

def count_shouters(grave: Grave) -> int:
    
    '''
    This function counts the all uppercase messages.
    
    Args:
    grave (Grave): A dictionary is taken for this function.
    
    Returns:
    int: The total number of shouting graves.
    '''
    
    total = 0
    for loud in grave:
        if loud["message"] == loud["message"].upper():
            total = total + 1
    return total

assert_equal(count_shouters(MONSTER_MASH['graves 1']), 3)
assert_equal(count_shouters(MONSTER_MASH['graves 2']), 1)
assert_equal(count_shouters(MONSTER_MASH['graves 3']), 1)
assert_equal(count_shouters(MONSTER_MASH['graves 4']), 0)


## Treats

'''
A Treat is a dictionary with the following keys
* "name": A string value indicating the name of the treat
* "chocolate?": A boolean indicating whether the treat involves chocolate
* "calories": An integer representing how many calories are in the treat
* "quantity": An integer indicating the typical serving size of the treat.
'''

Treat = {'name': str, 'chocolate?': bool, 'calories': int, 'quantity': int}

'''
T1. You are going through a series of houses and you get a treat from
each one. Define a function `eat_candy` that consumes a list of treats and
produces the total number of calories in all the treats.
'''

def eat_candy(treat: Treat) -> int:
    
    '''
    This function gets the total number of calories from all the treats.
    
    Args:
    treat (Treat): A dictionary is taken for this function.
    
    Returns:
    int: The total number of calories.
    '''
    
    calories = 0
    for sweet in treat:
        calories = calories + sweet["calories"]
    return calories

assert_equal(eat_candy(MONSTER_MASH['treats 1']), 563)
assert_equal(eat_candy(MONSTER_MASH['treats 2']), 280)
assert_equal(eat_candy(MONSTER_MASH['treats 3']), 407)
assert_equal(eat_candy(MONSTER_MASH['treats 4']), 464)
assert_equal(eat_candy(MONSTER_MASH['treats 5']), 213)
assert_equal(eat_candy(MONSTER_MASH['treats 6']), 0)

'''
T2. Define a function `find_most_calorific_ratio` that consumes a list
of treats and produces a float representing the treat with the
highest calories per quantity. If the list is empty, return
the special value None.
'''

def find_most_calorific_ratio(treat: Treat) -> float:
    
    '''
    This function finds the most amount of calories in a treat.
    
    Args:
    treat (Treat): A dictionary is taken for this function.
    
    Returns:
    float: The highest amount of calories per quantity.
    '''
    
    quantity = 0
    highest = 0
    if len(treat) == 0:
        return None
    for sweet in treat:
        if quantity < sweet["calories"] / sweet["quantity"]:
            quantity = sweet["calories"] / sweet["quantity"]
    return quantity

assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 1']), 35.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 2']), 35.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 3']), 214.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 4']), 214.0)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 5']), 7.368421052631579)
assert_equal(find_most_calorific_ratio(MONSTER_MASH['treats 6']), None)

'''
T3. Define a function `find_most_calorific` that consumes a list
of treats and produces a string representing the name of the treat with the
highest calories per quantity. If the list is empty, return
the special value None. In the event of a tie, give the name of the
treat later in the list.
'''

def find_most_calorific(treat: Treat) -> str:
    
    '''
    This function gets the treat with the most number of calories per quantity.
    
    Args:
    treat (Treat): A dictionary is taken for this function.
    
    Returns:
    str: The treat with the highest number of calories is returned.
    '''
    
    if treat == []:
        return None
    calorific = 0
    sweet_name = ""
    for sweet in treat:
        if calorific <= sweet["calories"] / sweet["quantity"]:
            calorific = sweet["calories"] / sweet["quantity"]
            sweet_name = sweet["name"]
    return sweet_name
    

assert_equal(find_most_calorific(MONSTER_MASH['treats 1']), "Snickers")
assert_equal(find_most_calorific(MONSTER_MASH['treats 2']), "Snickers")
assert_equal(find_most_calorific(MONSTER_MASH['treats 3']), "Candy Apple")
assert_equal(find_most_calorific(MONSTER_MASH['treats 4']), "Candy Apple")
assert_equal(find_most_calorific(MONSTER_MASH['treats 5']), "Candy Corn")
assert_equal(find_most_calorific(MONSTER_MASH['treats 6']), None)

'''
T4. Define a function named `count_chocolates` that consumes a list of treats
and produces the number of treats that are made of chocolate.
'''

def count_chocolates(treat: Treat) -> int:
    
    '''
    This function counts all the treats that are chocolate.
    
    Args:
    treat (Treat): A dictionary is taken for this function.
    
    Returns:
    int: The total number of chocolates is returned.
    '''
    
    chocos = 0
    for sweet in treat:
        if sweet["chocolate?"]:
            chocos = chocos + 1
    return chocos

assert_equal(count_chocolates(MONSTER_MASH['treats 1']), 2)
assert_equal(count_chocolates(MONSTER_MASH['treats 2']), 4)
assert_equal(count_chocolates(MONSTER_MASH['treats 3']), 2)
assert_equal(count_chocolates(MONSTER_MASH['treats 4']), 0)
assert_equal(count_chocolates(MONSTER_MASH['treats 5']), 1)
assert_equal(count_chocolates(MONSTER_MASH['treats 6']), 0)

'''
T5. Define a function named `get_choco_quantity` that consumes a list
of treats and produces an integer representing the total quantities
of all the chocolate treats.
'''

def get_choco_quantity(treat: Treat) -> int:
    
    '''
    This function adds up all the chocolate quantities.
    
    Args:
    treat (Treat): A dictionary is taken for this function.
    
    Returns:
    int: The total number of chocolate quanitites is returned.
    '''
    
    chocos = 0
    for sweet in treat:
        if sweet["chocolate?"]:
            chocos = chocos + sweet["quantity"]
    return chocos

assert_equal(get_choco_quantity(MONSTER_MASH['treats 1']), 19)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 2']), 8)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 3']), 19)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 4']), 0)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 5']), 17)
assert_equal(get_choco_quantity(MONSTER_MASH['treats 6']), 0)


## Media

'''
A Media is a dictionary with the following keys:
* "name": The name of this media
* "kind": Either "movie", "song", or "game"
* "duration": The length of this media in minutes
'''

Media = {'name': str, 'kind': str, 'duration': int}

'''
E1. Define a function `total_duration` that consumes a list of Media
and produces their total duration.
'''

def total_duration(media: Media) -> int:
    
    '''
    This function gets the total time for all media.
    
    Args:
    media (Media): A dictionary is taken for this function.
    
    Returns:
    int: The total duration.
    '''
    
    total = 0
    for med in media:
        total = total + med["duration"]
    return total

assert_equal(total_duration(MONSTER_MASH['media 1']), 383)
assert_equal(total_duration(MONSTER_MASH['media 2']), 146)
assert_equal(total_duration(MONSTER_MASH['media 3']), 1440)
assert_equal(total_duration(MONSTER_MASH['media 4']), 216)
assert_equal(total_duration(MONSTER_MASH['media 5']), 0)

'''
E2. Define the function `count_not_long` that consumes a list of media
and produces the number of items that are less than 100 minutes long.
'''

def count_not_long(media: Media) -> int:
    
    '''
    This function counts all the items that are less than 100 minutes.
    
    Args:
    media (Media): A dictionary is taken for this function.
    
    Returns:
    int: The total of all the shorter medias.
    '''
    
    total = 0
    for med in media:
        if med["duration"] < 100:
            total = total + 1
    return total

assert_equal(count_not_long(MONSTER_MASH['media 1']), 2)
assert_equal(count_not_long(MONSTER_MASH['media 2']), 4)
assert_equal(count_not_long(MONSTER_MASH['media 3']), 0)
assert_equal(count_not_long(MONSTER_MASH['media 4']), 2)
assert_equal(count_not_long(MONSTER_MASH['media 5']), 0)

'''
E3. Define the function `take_until_long` that consumes a list of media
and counts elements until it encounters something that is 100 minutes
longer or more, and then stops and returns the number counted so far.
'''

def take_until_long(media: Media) -> int:
    
    '''
    This function takes items until an item is above or at 100 minutes.
    
    Args:
    media (Media): A dictionary is taken for this function.
    
    Returns:
    int: THe number of medias, before a really long media.
    '''
    
    total = 0
    taking = True
    for med in media:
        if med["duration"] >= 100:
            taking = False
        elif taking:
            total = total + 1
    return total

assert_equal(take_until_long(MONSTER_MASH['media 1']), 2)
assert_equal(take_until_long(MONSTER_MASH['media 2']), 2)
assert_equal(take_until_long(MONSTER_MASH['media 3']), 0)
assert_equal(take_until_long(MONSTER_MASH['media 4']), 2)
assert_equal(take_until_long(MONSTER_MASH['media 5']), 0)

'''
E4. Define the function `longest_kind` that consumes a list of Media
and produces a string value representing the kind that had the highest
duration. If the list is empty, return the value None.
'''

def longest_kind(media: Media) -> str:
    
    '''
    This function gives the media with the highest duration.
    
    Args:
    media (Media): A dictionary is taken for this function.
    
    Returns:
    str: The kind with the highest duration.
    '''
    
    if media == []:
        return None
    longest_media = media[0]["duration"]
    media_kind = media[0]["kind"]
    for med in media:
        if med["duration"] > longest_media:
            longest_media = med["duration"]
            media_kind = med["kind"]
    return media_kind

assert_equal(longest_kind(MONSTER_MASH['media 1']), "movie")
assert_equal(longest_kind(MONSTER_MASH['media 2']), "song")
assert_equal(longest_kind(MONSTER_MASH['media 3']), "game")
assert_equal(longest_kind(MONSTER_MASH['media 4']), "game")
assert_equal(longest_kind(MONSTER_MASH['media 5']), None)

'''
E5. Define the function `same_kind_of_media` that consumes a list
of Media and produces a boolean indicating whether all of the
kinds of media are the same as each other. If the list is empty,
the result is True.
'''

def same_kind_of_media(media: Media) -> bool:
    
    '''
    This function tests if all kind of media is the same.
    
    Args:
    media (Media): A dictionary is taken for this function.
    
    Returns:
    bool: If the kinds are all the same than true, or else false.
    '''
    
    if media == []:
        return True
    same = True
    media_kind = media[0]["kind"]
    for med in media:
        if med["kind"] == media_kind:
            same = True
        else:
            same = False
    return same
   # return True

assert_equal(same_kind_of_media(MONSTER_MASH['media 1']), True)
assert_equal(same_kind_of_media(MONSTER_MASH['media 2']), True)
assert_equal(same_kind_of_media(MONSTER_MASH['media 3']), True)
assert_equal(same_kind_of_media(MONSTER_MASH['media 4']), False)
assert_equal(same_kind_of_media(MONSTER_MASH['media 5']), True)


## Brewing Potions

'''
An Ingredient has the following keys:
* 'name': The name of the ingredient
* 'rare?': Whether the ingredient is rare

A Potion has the following keys:
* 'effect': The effect of the potion
* 'ingredients': The required ingredients of the potion
* 'time required': How many minutes it takes to brew the potion
'''

Ingredient = {'name': str, 'rare?': bool}
Potion = {'effect': str, 'ingredients': [Ingredient], 'time required': int}

'''
B1. Define the function `total_ingredients` that consumes a list
of potions and produces the total number of required ingredients.
Include duplicates in your total.
'''

def total_ingredients(potion: Potion) -> int:
    
    '''
    This function gives the total number of ingredients for any potions.
    
    Args:
    ingredient (Ingredient): A dictionary is taken for this function.
    potion (Potion): A dictionary is taken for this function.
    
    Returns:
    int: Number of ingredients for any potion.
    '''
    
    total = 0
    for pot in potion:
        for ingredient in pot["ingredients"]:
            total = total + 1
    return total

assert_equal(total_ingredients(MONSTER_MASH['brewing 1']), 9)
assert_equal(total_ingredients(MONSTER_MASH['brewing 2']), 5)
assert_equal(total_ingredients(MONSTER_MASH['brewing 3']), 8)
assert_equal(total_ingredients(MONSTER_MASH['brewing 4']), 0)

'''
B2. Define the function `count_rare_ingredients` that consumes a list
of potions and produces the total number of required ingredients that
are rare.
'''

def count_rare_ingredients(potion: Potion) -> int:
    
    '''
    This function counts all of the rare ingredients that are required.
    
    Args:
    ingredient (Ingredient): A dictionary is taken for this function.
    potion (Potion): A dictionary is taken for this function.
    
    Returns:
    int: Number of rare ingredients needed for a potion.
    '''
    
    total = 0
    for pot in potion:
        for ingredient in pot["ingredients"]:
            if ingredient["rare?"] == True:
                total = total + 1
    return total

assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 1']), 1)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 2']), 4)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 3']), 4)
assert_equal(count_rare_ingredients(MONSTER_MASH['brewing 4']), 0)

'''
B3. Define the function `get_ingredients` that consumes a list of
potions and produces a list of strings (representing ingredient names)
in the order that the ingredients are listed in the potions.
Do not include duplicate ingredients.
'''

def get_ingredients(potion: Potion) -> [str]:
    
    '''
    This function lists all the ingredients needed for a potion.
    
    Args:
    ingredient (Ingredient): A dictionary is taken for this function.
    potion (Potion): A dictionary is taken for this function.
    
    Returns:
    [str]: A list of the ingredients names.
    '''
    
    ingredient_names = []
    for pot in potion:
        for ingredient in pot["ingredients"]:
            if ingredient["name"] not in ingredient_names:
                ingredient_names.append(ingredient["name"])
    return ingredient_names

assert_equal(get_ingredients(MONSTER_MASH['brewing 1']), ["Spider Webs", "Ant Hill", "Dragon Egg", "Moon Blooms", "Candy Leaf"])
assert_equal(get_ingredients(MONSTER_MASH['brewing 2']), ["Dream Petal", "Hens Teeth", "Ant Hill"])
assert_equal(get_ingredients(MONSTER_MASH['brewing 3']), ["Candy Leaf", "Moon Blooms", "Red Nightshade", "Werewolf Heart"])
assert_equal(get_ingredients(MONSTER_MASH['brewing 4']), [])

'''
B4. Define the function `get_brewing_time` that consumes a list of
potions and produces an integer representing the total time required
to brew all the potions.
'''

def get_brewing_time(potion: Potion) -> int:
    
    '''
    This function gets the total time to make the potion.
    
    Args:
    ingredient (Ingredient): A dictionary is taken for this function.
    potion (Potion): A dictionary is taken for this function.
    
    Returns:
    int: The total time. 
    '''
    
    time = 0
    for pot in potion:
        time = time + pot["time required"]
    return time

assert_equal(get_brewing_time(MONSTER_MASH['brewing 1']), 15)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 2']), 16)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 3']), 12)
assert_equal(get_brewing_time(MONSTER_MASH['brewing 4']), 0)

'''
B5. Define the function `brew_time_per_ingredient` that consumes a list
of potions and produces a float representing the average amount of
time spent brewing overall. To do so, add up the time spent brewing
and divide it by the number of ingredients. If there are no ingredients,
return the value None.
'''

def brew_time_per_ingredient(potion: Potion) -> float:
    
    '''
    This function gets the time for each ingredient to brew.
    
    Args:
    ingredient (Ingredient): A dictionary is taken for this function.
    potion (Potion): A dictionary is taken for this function.
    
    Returns:
    float: The time for each ingredient. 
    '''
    
    time = 0
    total = 0
    if len(potion) == 0:
        return None
    for pot in potion:
        for ingredient in pot["ingredients"]:
            total = total + 1
    for pot in potion:
        time = time + pot["time required"]
    average = time / total
    return average

assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 1']), 1.6666666666666667)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 2']), 3.2)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 3']), 1.5)
assert_equal(brew_time_per_ingredient(MONSTER_MASH['brewing 4']), None)

'''
B6. Define the function `get_rarest_potion` that consumes a list of potions
and returns the effect of the potion that requires the most rare ingredients.
If there are no rare ingredients in any of the potions, then return None instead.
'''

def get_rarest_potion(potion: Potion) -> str:
    
    '''
    This function gets the effect rarest potion has.
    
    Args:
    ingredient (Ingredient): A dictionary is taken for this function.
    potion (Potion): A dictionary is taken for this function.
    
    Returns:
    str: The effect of the rarest potion. 
    '''
    
    rarest = 0
    effect = None
    if len(potion) == 0:
        return effect
    for pot in potion:
        rare_ingredients = 0
        for ingredient in pot["ingredients"]:
            if ingredient["rare?"] == True:
                rare_ingredients = rare_ingredients + 1
            if rarest < rare_ingredients:
                rarest = rare_ingredients
                effect = pot["effect"]
    return effect

assert_equal(get_rarest_potion(MONSTER_MASH['brewing 1']), "Sweet Breathing Potion")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 2']), "Embiggening Potion")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 3']), "Delirious Tea")
assert_equal(get_rarest_potion(MONSTER_MASH['brewing 4']), None)
            