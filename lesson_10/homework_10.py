# Початкові дані імперії
imperial_citizens = ["John", "Jane", "Bob", "Alice"]
resources = {"gold": 100, "wood": 50, "stone": 30}


# Додати нового жителя до імперії
def add_citizen(name):
    if name not in imperial_citizens:
        imperial_citizens.append(name)
        print(f"{name} був доданий до імперії.")
    else:
        print(f"{name} вже існує в імперії.")


# Видалити жителя з імперії
def remove_citizen(name):
    if name in imperial_citizens:
        imperial_citizens.remove(name)
        print(f"{name} був видалений з імперії.")
    else:
        print(f"{name} не знайдений в імперії.")


# Додати ресурси до імперії
def add_resources(resource, amount):
    if resource in resources:
        resources[resource] += amount
        print(f"Додано {amount} {resource} до ресурсів імперії.")
    else:
        print(f"Ресурс {resource} не знайдений.")


# Обмін ресурсів
def market_place(resource_in, resource_out, amount_in):
    if resource_in not in resources or resource_out not in resources:
        print("Некоректний ресурс.")
        return

    if resource_in == "stone" and resource_out == "gold":
        rate = 5
    elif resource_in == "stone" and resource_out == "wood":
        rate = 1 / 5
    elif resource_in == "wood" and resource_out == "gold":
        rate = 25
    else:
        print("Некоректний обмін.")
        return

    if resources[resource_in] < amount_in:
        print(f"Недостатньо {resource_in} для обміну.")
        return

    amount_out = amount_in // rate if resource_in == "stone" and resource_out == "gold" else amount_in * rate
    resources[resource_in] -= amount_in
    resources[resource_out] += int(amount_out)

    print(f"Обміняно {amount_in} {resource_in} на {int(amount_out)} {resource_out}.")


# Приклади використання:
print("Початкові дані:", imperial_citizens, resources)

add_citizen("Eve")
add_citizen("John")  # Додавання вже існуючого жителя

remove_citizen("Alice")
remove_citizen("Tom")  # Видалення неіснуючого жителя

add_resources("gold", 50)
add_resources("iron", 20)  # Додавання неіснуючого ресурсу

market_place("stone", "gold", 10)
market_place("stone", "wood", 5)
market_place("wood", "gold", 50)
market_place("gold", "stone", 10)  # Некоректний обмін

print("Кінцеві дані:", imperial_citizens, resources)