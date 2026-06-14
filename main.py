from openfoodfacts_client import OpenFoodFactsClient
from food_product import FoodProduct
from nutrition_analyzer import NutritionAnalyzer
from ai_explainer import AIExplainer
from meal_suggestion_generator import MealSuggestionGenerator
from food_logger import FoodLogger
from validators import validate_barcode
from exceptions import InvalidBarcodeError, ProductNotFoundError

try:

    barcode = input("Enter Product Barcode: ")

    if not validate_barcode(barcode):
        raise InvalidBarcodeError("Invalid Barcode")

    client = OpenFoodFactsClient()

    data = client.get_product(barcode)

    if data is None:
        raise ProductNotFoundError("Product Not Found")

    product = FoodProduct(
        data["name"],
        barcode,
        data["ingredients"],
        data["nutrients"],
        data["allergens"]
    )

    product.display()

    analyzer = NutritionAnalyzer()
    analyzer.analyze(product)

    ai = AIExplainer()
    ai.explain(product)

    meal = MealSuggestionGenerator()
    meal.generate(product)

    logger = FoodLogger()
    logger.save(product)

except Exception as e:
    print("Error:", e)
