# Початкові дані імперії
imperial_citizens = ["John", "Jane", "Bob", "Alice"]
resources = {"gold": 100, "wood": 50, "stone": 30}

# Додати нового жителя до імперії
# Додаткова умова: додавати лише з унікальним ім'ям
def add_citizen(name):
    if name in imperial_citizens:
        raise ValueError(f"Citizen {name} already exists.")
    imperial_citizens.append(name)

# Видалити жителя з імперії
def remove_citizen(name):
    if name not in imperial_citizens:
        raise ValueError(f"Citizen {name} does not exist.")
    imperial_citizens.remove(name)

# Додати ресурси до імперії
def add_resources(resource, amount):
    if resource in resources:
        resources[resource] += amount
    else:
        resources[resource] = amount

# Обмін ресурсів
def market_place(resource_in, resource_out):
    exchange_rates = {
        ("stone", "gold"): 5,
        ("stone", "wood"): 0.2,
        ("wood", "gold"): 25
    }

    if (resource_in, resource_out) not in exchange_rates:
        raise ValueError("Invalid exchange")

    rate = exchange_rates[(resource_in, resource_out)]
    if resources[resource_in] < rate:
        raise ValueError("Not enough resources for exchange")

    resources[resource_in] -= rate
    resources[resource_out] += 1
