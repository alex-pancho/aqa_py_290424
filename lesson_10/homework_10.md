**Управління Імперією (завдання підвищеної складності)**

Створити міні гру "Управління Імперією":

```python
# Початкові дані імперії
imperial_citizens = ["John", "Jane", "Bob", "Alice"]
resources = {"gold": 100, "wood": 50, "stone": 30}
def add_citizen(name):
    new_citizen = name
    for i in imperial_citizens = new_citizen:
        print(f"The {name} already exists")

# Видалити жителя з імперії
def remove_citizen(name):
```

```python
# Додати ресурси до імперії
def add_resources(resource, amount):
```

Напишіть для цієї гри функцію market_place (resource_in, resource_out)
де здійсюється обмін ресурсів
5 stone = 1 gold
1 stone = 5 wood
25 wood = 1 gold

не забудьте додати перевірки і зміну наявних resources після обміну

# my answer:
imperial_citizens = ["John", "Jane", "Bob", "Alice"]
resources = {"gold": 100, "wood": 50, "stone": 30}
def add_citizen(name):
    for i in imperial_citizens:
        if i == name:
         print(f"The name already exists")
         return False
        else:
           imperial_citizens.append(name)
           print(imperial_citizens)
           return True
name = "Job"
add_citizen(name)


def remove_citizen(name):
   if name in imperial_citizens:
      imperial_citizens.remove(name)
      print(imperial_citizens)
      return True
   else:
      print(f"The {name} name is not found")
      return False
name = 'Jobbb'
remove_citizen(name)

def add_resources(resource, amount):
   if resource in resources:
      resources[resource] += amount


def market_place (resource_in, resource_out):
    if resources["gold"] < 1:
      print("No enough golds in resources")
    else:
     if resource_in == "stone"and resource_out == "gold":
        resources["stone"] += 5
        resources["gold"] -= 1
        print("You get 1 gold")
     elif resources["wood"] < 5:
         print("No enough woods in resources")
     else:
        if resource_in == "stone" and resource_out == "wood":
           resources["stone"] += 1
           resources["wood"] -= 5
           print("You get 5 woods")
        elif resources["gold"] < 1:
         print("No enough woods in resources")
        else:
         if resource_in == "wood" and resource_out == "gold":
           resources["wood"] += 25
           resources["gold"] -= 1
           print("You get 1 gold")cd