import random


def add_new_pet_request_body_template():
    return {
      "id": random.randint(1, 1_000_000_000_000),
      "category": {
        "id": 100,
        "name": "Dinosaur"
      },
      "name": "Tyrannosaurus",
      "photoUrls": [
        "http://en.wikipedia.org/wiki/Tyrannosaurus#/media/File:Tyrannosaurus_rex_mmartyniuk.png"
      ],
      "tags": [
        {
          "id": 100,
          "name": "reptile"
        }
      ],
      "status": "available"
    }
