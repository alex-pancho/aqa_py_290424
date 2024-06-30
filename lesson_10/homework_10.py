# Початкові дані імперії
imperial_citizens = ["John", "Jane", "Bob", "Alice"]
resources = {"gold": 100, "wood": 50, "stone": 30}

# Додати нового жителя до імперії
# Додаткова умова: додавати лише з унікальним ім'ям
def add_citizen(name):
    """Adds new citizen with unique name to empire"""
    if not name in imperial_citizens:
        imperial_citizens.append(name)

add_citizen("Bibi")
print(imperial_citizens)
add_citizen("Alice")
print(imperial_citizens)

# Видалити жителя з імперії
def remove_citizen(name):
    """Removes citizen from empire"""
    if name in imperial_citizens:
        imperial_citizens.remove(name)

remove_citizen("Bob")
print(imperial_citizens)
remove_citizen("Bulochka")
print(imperial_citizens)

# Додати ресурси до імперії
def add_resources(resource, amount):
    """Adds resources to empire"""
    if resource in resources:
        new_amount = resources[resource] + amount
        if new_amount < 0:
            print("There is no enough resources")
        else:
           resources[resource] = new_amount

    else:
        resources.update({resource: amount})

add_resources("gold", 10)
print(resources)
add_resources("tree", 60)
print(resources)
add_resources("gold", -200)
print(resources)


"""Напишіть для цієї гри функцію market_place (resource_in, resource_out)
де здійсюється обмін ресурсів
5 stone = 1 gold
1 stone = 5 wood
25 wood = 1 gold"""

def market_place (resource_in, resource_out):
    """Exchanges resources, ratio is based on 1 gold"""
    resource_to_gold_ratio = {"gold": 1, "stone": 0.2, "wood": 0.04}
    if resource_in in resource_to_gold_ratio and resource_out in resource_to_gold_ratio:
        resource_in_amount = 1 / resource_to_gold_ratio[resource_in]
        resource_out_amount = 1 / resource_to_gold_ratio[resource_out]
        if resources[resource_out] >= resource_out_amount:
            add_resources(resource_in, int(resource_in_amount))
            add_resources(resource_out, int(-resource_out_amount))
        else:
            print("There is no enough resources")

market_place("gold", "wood")
print(resources)
market_place("gold", "wood")
print(resources)
market_place("gold", "wood")
print(resources)
market_place("wood", "stone")
print(resources)

#check if we have recources 
# how much resource_in cost 1 gold
# how much resource_out cost 1 gold
#check if we have enough of resource_out
#if yes exchange 
        