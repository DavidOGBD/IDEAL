import json
import os


class FoodLogger:

    def save(self, product):

        data = {
            "name": product.name,
            "barcode": product.barcode
        }

        filename = "food_log.json"

        if not os.path.exists(filename):

            with open(filename, "w") as file:
                json.dump([], file)

        with open(filename, "r") as file:
            logs = json.load(file)

        logs.append(data)

        with open(filename, "w") as file:
            json.dump(
                logs,
                file,
                indent=4
            )

        print("Food Logged Successfully")
