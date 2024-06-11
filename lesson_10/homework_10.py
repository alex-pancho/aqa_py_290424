# Початкові дані імперії
imperial_citizens = ["John", "Jane", "Bob", "Alice"]
resources = {"gold": 100, "wood": 50, "stone": 30}


# Додати нового жителя до імперії
# Додаткова умова: додавати лише з унікальним ім'ям
def add_citizen(name):
    if name not in imperial_citizens:
        imperial_citizens.append(name)
        print(f'{name} has been added to the list of imperial citizens.')
    else:
        print(f'{name} is already in the list of imperial citizens.')


# Видалити жителя з імперії
def remove_citizen(name):
    if name in imperial_citizens:
        imperial_citizens.remove(name)
        print(f'{name} has been removed from the list imperial citizens.')
    else:
        print(f'{name} is not in the list of imperial citizens.')


# Додати ресурси до імперії
def add_resources(resource, amount):
    if resource in resources:
        resources[resource] += amount
        print(f'{amount} units of {resource} have been added. New total: {resources[resource]}.')
    else:
        print(f"{resource} is not a recognized resource and cannot be added.")


def market_place(resource_in, resource_out):
    # Define exchange rates
    exchange_rates = {
        ('stone', 'gold'): 5,
        ('stone', 'wood'): 1,
        ('wood', 'gold'): 25
    }

    # Check the availability of the exchange rate
    if (resource_in, resource_out) not in exchange_rates:
        print(f"Exchange rate from {resource_in} to {resource_out} is not available.")
        return

    # Determine the amount of resources needed for exchange
    exchange_rate = exchange_rates[(resource_in, resource_out)]

    # Check the sufficient number of resources for exchange
    if resources[resource_in] < exchange_rate:
        print(f"Not enough {resource_in} to exchange for {resource_out}.")
        return

    # Perform the exchange
    if resource_in == "stone" and resource_out == "wood":
        required_resources = 1
        amount_received = 5
    else:
        required_resources = exchange_rate
        amount_received = 1

    resources[resource_in] -= required_resources
    resources[resource_out] += amount_received

    # Display a message about a successful exchange
    print(f"Exchanged {required_resources} {resource_in} for {amount_received} {resource_out}.")
    print(f"New resources: {resources}")


if __name__ == '__main__':
    print(add_citizen('John'))
    print(add_citizen('Serhii'))
    print(imperial_citizens)
    print(remove_citizen('John'))
    print(remove_citizen('Morkovka'))
    print(imperial_citizens)
    add_resources("gold", 50)
    add_resources("food", 20)
    print(resources)
    print(market_place("stone", "gold"))  # Exchanged 5 stone for 1 gold. New resources: {'gold': 101, 'wood': 50, 'stone': 25}
    print(market_place("stone", "wood"))  # Exchanged 1 stone for 5 wood. New resources: {'gold': 101, 'wood': 55, 'stone': 24}
    print(market_place("wood", "gold"))  # Exchanged 25 wood for 1 gold. New resources: {'gold': 102, 'wood': 30, 'stone': 24}
    print(market_place("gold", "stone"))  # Exchange rate from gold to stone is not available.
    print(resources)
